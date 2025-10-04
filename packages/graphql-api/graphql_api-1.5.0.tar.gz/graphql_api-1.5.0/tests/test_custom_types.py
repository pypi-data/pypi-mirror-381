import uuid
from datetime import date, datetime, timedelta
from typing import List
from uuid import UUID

from graphql import GraphQLID, GraphQLScalarType, StringValueNode

from graphql_api.api import GraphQLAPI
from graphql_api.types import JsonType


class TestCustomTypes:
    def test_id_type(self) -> None:
        api = GraphQLAPI()

        # noinspection PyUnusedLocal
        @api.type(is_root_type=True)
        class Root:
            @api.field
            def test(self, id: GraphQLID) -> GraphQLID:  # type: ignore[valid-type]
                return id

        executor = api.executor()

        test_name_query = 'query { test(id: "1") }'

        result = executor.execute(test_name_query)

        expected = {"test": "1"}
        assert not result.errors
        assert result.data == expected

        assert executor.schema.query_type.fields["test"].type.of_type == GraphQLID  # type: ignore[reportIncompatibleMethodOverride]

    def test_uuid_type(self) -> None:
        api = GraphQLAPI()

        user_id = uuid.uuid4()

        # noinspection PyUnusedLocal
        @api.type(is_root_type=True)
        class Root:
            @api.field
            def name(self, id: UUID) -> str:
                assert isinstance(id, UUID)
                assert id == user_id
                return "rob"

            @api.field
            def id(self) -> UUID:
                return user_id

        executor = api.executor()

        test_name_query = f'query GetName {{ name(id: "{user_id}") }}'

        result = executor.execute(test_name_query)

        expected = {"name": "rob"}
        assert not result.errors
        assert result.data == expected

        test_id_query = "query GetId { id }"

        result = executor.execute(test_id_query)

        expected = {"id": str(user_id)}

        assert not result.errors
        assert result.data == expected

        test_invalid_name_query = 'query GetName { name(id: "INVALID_UUID") }'

        result = executor.execute(test_invalid_name_query)

        assert result.errors

    def test_datetime_type(self) -> None:
        api = GraphQLAPI()

        now = datetime.now()

        @api.type(is_root_type=True)
        class Root:
            @api.field
            def add_one_hour(self, time: datetime) -> datetime:
                return time + timedelta(hours=1)

        executor = api.executor()

        test_time_query = f'query GetTimeInOneHour {{ addOneHour(time: "{now}") }}'

        result = executor.execute(test_time_query)

        expected = {"addOneHour": str(now + timedelta(hours=1))}
        assert not result.errors
        assert result.data == expected

    def test_date_type(self) -> None:
        api = GraphQLAPI()

        now = date.today()

        @api.type(is_root_type=True)
        class Root:
            @api.field
            def add_one_day(self, date: date) -> date:
                return date + timedelta(days=1)

        executor = api.executor()

        test_time_query = f'query GetTimeInOneHour {{ addOneDay(date: "{now}") }}'

        result = executor.execute(test_time_query)

        expected = {"addOneDay": str(now + timedelta(days=1))}
        assert not result.errors
        assert result.data == expected

    def test_json_type(self) -> None:
        api = GraphQLAPI()

        @api.type(is_root_type=True)
        class Root:
            @api.field
            def adapt_profile(self, profile: dict) -> dict:
                return {**profile, "location": "london"}

            @api.field
            def add_number(self, numbers: list) -> list:
                return [*numbers, 5]

            @api.field
            def send_json(self, json: JsonType) -> str:
                return str(type(json)) + str(json)

        executor = api.executor()

        test_profile_query = (
            r"query GetAdaptProfile {"
            r"     adaptProfile(profile: "
            r'     "{ \"name\": \"rob\", \"age\": 26 }") '
            r"}"
        )

        result = executor.execute(test_profile_query)

        expected = {
            "adaptProfile": '{"name": "rob", "age": 26, "location": "london"}'}
        assert not result.errors
        assert result.data == expected

        test_number_query = (
            r"query GetAddNumber {" r'     addNumber(numbers: "[1, 2, 3, 4]") ' r"}"
        )

        result = executor.execute(test_number_query)

        expected = {"addNumber": "[1, 2, 3, 4, 5]"}
        assert not result.errors
        assert result.data == expected

        test_json_query = (
            "query SendJson {"
            '     a: sendJson(json: "1") '
            "     b: sendJson(json: true) "
            '     c: sendJson(json: "true") '
            '     d: sendJson(json: "\\"test\\"") '
            '     e: sendJson(json: "{ \\"a\\": 1 }") '
            '     f: sendJson(json: "[ 1, 2, 3 ]") '
            '     g: sendJson(json: "1.01") '
            "}"
        )

        result = executor.execute(test_json_query)

        expected = {
            "a": "<class 'int'>1",
            "b": "<class 'bool'>True",
            "c": "<class 'bool'>True",
            "d": "<class 'str'>test",
            "e": "<class 'dict'>{'a': 1}",
            "f": "<class 'list'>[1, 2, 3]",
            "g": "<class 'float'>1.01",
        }
        assert not result.errors
        assert result.data == expected

    def test_bytes_type(self) -> None:
        api = GraphQLAPI()

        data_input = b"aW5wdXRfYnl0ZXM="
        data_output = b"b3V0cHV0X2J5dGVz"
        non_utf_output = "A".encode("utf-32")

        @api.type(is_root_type=True)
        class Root:
            @api.field
            def byte_data(self, value: bytes) -> bytes:
                assert value == data_input
                return data_output

            @api.field
            def non_utf_byte_data(self) -> bytes:
                return non_utf_output

        executor = api.executor()

        test_bytes_query = (
            f"query GetByteData {{ byteData(value: \"{data_input.decode('utf-8')}\") }}"
        )

        result = executor.execute(test_bytes_query)

        expected = {"byteData": data_output.decode("utf-8")}
        assert not result.errors
        assert result.data == expected

        test_non_utf_bytes_query = "query GetNonUtfByteData { nonUtfByteData }"
        result = executor.execute(test_non_utf_bytes_query)

        expected = {
            "nonUtfByteData": "UTF-8 ENCODED PREVIEW: \x00\x00A\x00\x00\x00"}
        assert not result.errors
        assert result.data == expected

    def test_custom_scalar_type(self) -> None:
        api = GraphQLAPI()

        def parse_value(value):
            return str(value) + "_parsed_value"

        def parse_literal(node):
            if isinstance(node, StringValueNode):
                return parse_value(node.value)

        GraphQLKey = GraphQLScalarType(
            name="Key",
            description="The `Key` scalar type represents a key.",
            serialize=lambda value: str(value) + "_serialized",
            parse_value=parse_value,
            parse_literal=parse_literal,  # type: ignore[reportIncompatibleMethodOverride]
        )

        @api.type(is_root_type=True)
        class Root:
            @api.field
            def return_key(self) -> GraphQLKey:  # type: ignore[valid-type]
                return "a_key_value"

            @api.field
            def set_key(self, key: GraphQLKey) -> str:  # type: ignore[valid-type]
                return key

            @api.field
            def test(self, key: List[GraphQLKey]) -> str:  # type: ignore[valid-type]
                return str(key)

        executor = api.executor()

        result = executor.execute("query { returnKey }")
        assert not result.errors
        assert result.data == {"returnKey": "a_key_value_serialized"}

        result = executor.execute('query { setKey(key: "test123") }')

        assert not result.errors
        assert result.data == {"setKey": "test123_parsed_value"}
