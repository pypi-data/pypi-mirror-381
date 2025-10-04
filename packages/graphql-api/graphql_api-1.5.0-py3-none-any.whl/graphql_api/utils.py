import ast
import asyncio
import enum
import inspect
import re
import textwrap
from json.decoder import JSONDecodeError

from graphql import (
    GraphQLError,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLSchema,
    build_client_schema,
    get_introspection_query,
)
from graphql.type.definition import GraphQLInterfaceType, GraphQLType


# From this response in Stackoverflow
# http://stackoverflow.com/a/19053800/1072990
def to_camel_case(snake_str, title=False):
    underscore_prefix = False
    if snake_str.startswith("_"):
        underscore_prefix = True
        snake_str = snake_str[1:]

    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    if not snake_str:
        return ""
    prefix = components[0].title() if title else components[0]
    value = prefix + "".join(x.title() if x else "_" for x in components[1:])
    return ("_" if underscore_prefix else "") + value


# From this response in Stackoverflow
# http://stackoverflow.com/a/1176023/1072990
def to_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_camel_case_text(text: str | None):
    if not text:
        return text
    for word in text.split():
        if "_" in word and word.islower():
            text = text.replace(word, to_camel_case(word))
    return text


def to_input_value(value):
    from graphql_api.mapper import is_scalar

    if value is None:
        return None

    python_type = type(value)

    if is_scalar(python_type):
        if isinstance(value, str):
            return '"' + value + '"'
        if isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    if isinstance(value, enum.Enum):
        return str(value.value)

    raise ValueError(f"Cannot map {value} to GraphQLInput")


def has_mutable(type, checked_types=None, interfaces_default_mutable=True):
    from .mapper import GraphQLMutableField, GraphQLTypeMapError

    while isinstance(type, (GraphQLNonNull, GraphQLList)):
        type = type.of_type

    if isinstance(type, (GraphQLObjectType, GraphQLInterfaceType)):
        if interfaces_default_mutable and isinstance(type, GraphQLInterfaceType):
            return True

        if not checked_types:
            checked_types = set()
        try:
            fields = type.fields
        except (AssertionError, GraphQLTypeMapError):
            return False

        for key, field in fields.items():
            if isinstance(field, GraphQLMutableField):
                return True
            if field.type not in checked_types:
                checked_types.add(field.type)
                if has_mutable(field.type, checked_types, interfaces_default_mutable):
                    return True

    return False


def iterate_fields(type: GraphQLType, done_fields=None):
    from .mapper import GraphQLTypeMapError

    while isinstance(type, (GraphQLNonNull, GraphQLList)):
        type = type.of_type

    if isinstance(type, GraphQLObjectType):
        if not done_fields:
            done_fields = set()

        try:
            type.fields
        except (AssertionError, GraphQLTypeMapError):
            pass
        else:
            for key, field in type.fields.items():
                field_id = type.name + "." + key
                if field_id not in done_fields:
                    done_fields.add(field_id)
                    yield type, key, field
                    yield from iterate_fields(field.type, done_fields)


def url_to_ast(url, http_method="GET", http_headers=None, verify=True) -> GraphQLSchema:
    _introspect_query = get_introspection_query()

    response = asyncio.run(
        http_query(
            url=url,
            query=_introspect_query,
            http_method=http_method,
            http_headers=http_headers,
            verify=verify,
        )
    )
    errors = response.get("errors")

    if errors:
        raise GraphQLError(f"RemoteSchema {url} Error: {str(errors)}")

    introspect_schema = response.get("data")
    return build_client_schema(introspect_schema)


def executor_to_ast(executor) -> GraphQLSchema:
    _introspect_query = get_introspection_query()
    response = executor.execute(_introspect_query)
    introspect_schema = response.data

    return build_client_schema(introspect_schema)


async def http_query(
    url,
    query,
    variable_values=None,
    operation_name=None,
    http_method="GET",
    http_headers=None,
    http_timeout=10,
    verify=True,
):
    import aiohttp
    from aiohttp import ClientTimeout

    params = {"query": query}

    if http_headers is None:
        http_headers = {}

    if variable_values:
        params["variables"] = variable_values

    if operation_name:
        params["operationName"] = operation_name

    async with aiohttp.ClientSession() as session:
        if http_method == "GET":
            r = await session.get(
                url,
                params=params,
                ssl=verify,
                headers={"Accept": "application/json", **http_headers},
                timeout=ClientTimeout(total=http_timeout),
            )

        elif http_method == "POST":
            r = await session.post(
                url,
                json=params,
                ssl=verify,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    **http_headers,
                },
                timeout=ClientTimeout(total=http_timeout),
            )

        else:
            raise AttributeError(f"Invalid HTTP method {http_method}")

        try:
            json = await r.json(content_type=None)
        except JSONDecodeError as e:
            text = await r.text()
            raise ValueError(
                f"{e}, unable to decode JSON from response: `{str(text)}`")
    return json


def get_function_def_node(func):
    """
    Parse the source of `func` and return its `ast.FunctionDef` or
    `ast.AsyncFunctionDef` node.
    Raises ValueError if we can't find it.
    """
    source = textwrap.dedent(inspect.getsource(func))
    module_node = ast.parse(source)

    for node in module_node.body:
        # Check for either a normal def or an async def
        if (
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == func.__name__
        ):
            return node

    raise ValueError(
        f"Could not find AST FunctionDef/AsyncFunctionDef for {func.__name__}"
    )


def has_single_type_union_return(func) -> bool:
    """
    Returns True if `func`'s return type annotation *literally* uses `Union[...]`
    with exactly one argument (e.g. `Union[int]`).
    """
    func_def = get_function_def_node(func)
    # This is the AST node for the return annotation
    annotation_node = func_def.returns

    # If there's no return annotation at all, we can stop
    if annotation_node is None:
        return False

    return is_union_of_single_type(annotation_node)


def is_union_of_single_type(annotation_node) -> bool:
    """
    Returns True if `annotation_node` is an AST node of the form:
    `Union[<single_type>]`
    """
    # Must be a Subscript node, like Union[int] or Union[int, str]
    if not isinstance(annotation_node, ast.Subscript):
        return False

    # Check if the 'value' part is "Union" or "typing.Union"
    union_name = None
    if isinstance(annotation_node.value, ast.Name):
        # e.g. "Union"
        union_name = annotation_node.value.id
    elif isinstance(annotation_node.value, ast.Attribute):
        # e.g. "typing.Union"
        if (
            isinstance(annotation_node.value.value, ast.Name)
            and annotation_node.value.value.id == "typing"
            and annotation_node.value.attr == "Union"
        ):
            union_name = "typing.Union"

    # If it's not recognized as Union, bail out
    if union_name not in ("Union", "typing.Union"):
        return False

    # Extract the subscript part. In older Python versions (<=3.8),
    # it might be wrapped in an ast.Index node.
    slice_node = annotation_node.slice
    slice_value = getattr(slice_node, "value", None)
    if slice_value is None:
        # Python 3.9+: "slice" is used directly, or it's not an Index node
        slice_value = slice_node

    # If the user wrote Union[int, str], we get an ast.Tuple in `slice_value`.
    # If it's just Union[int], we typically get a single name node.
    if isinstance(slice_value, ast.Tuple):
        # Means multiple arguments in the Union: e.g. Union[int, str]
        return False
    else:
        # A single argument in the Union
        return True
