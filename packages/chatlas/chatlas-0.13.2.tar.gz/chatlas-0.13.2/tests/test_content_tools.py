from typing import Any, Optional, Union
from unittest.mock import Mock

import orjson
import pytest

from chatlas import ChatOpenAI
from chatlas._content import ToolInfo
from chatlas.types import ContentToolRequest, ContentToolResult


def test_register_tool():
    chat = ChatOpenAI()

    # -------------------------

    def add(x: int, y: int) -> int:
        return x + y

    chat.register_tool(add)

    assert len(chat._tools) == 1
    tool = chat._tools["add"]
    assert tool.name == "add"
    assert tool.func == add
    assert tool.schema["function"]["name"] == "add"
    assert "description" in tool.schema["function"]
    assert tool.schema["function"]["description"] == ""
    assert "parameters" in tool.schema["function"]
    assert tool.schema["function"]["parameters"] == {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"},
        },
        "required": ["x", "y"],
    }


def test_register_tool_with_complex_parameters():
    chat = ChatOpenAI()

    def foo(
        x: list[tuple[str, float, bool]],
        y: Union[int, None] = None,
        z: Union[dict[str, str], None] = None,
    ):
        """Dummy tool for testing parameter JSON schema."""
        pass

    chat.register_tool(foo)

    assert len(chat._tools) == 1
    tool = chat._tools["foo"]
    assert tool.name == "foo"
    assert tool.func == foo
    assert tool.schema["function"]["name"] == "foo"
    assert "description" in tool.schema["function"]
    assert (
        tool.schema["function"]["description"]
        == "Dummy tool for testing parameter JSON schema."
    )
    assert "parameters" in tool.schema["function"]
    assert tool.schema["function"]["parameters"] == {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "x": {
                "type": "array",
                "items": {
                    "type": "array",
                    "maxItems": 3,
                    "minItems": 3,
                    "prefixItems": [
                        {"type": "string"},
                        {"type": "number"},
                        {"type": "boolean"},
                    ],
                },
            },
            "y": {
                "anyOf": [
                    {"type": "integer"},
                    {"type": "null"},
                ],
            },
            "z": {
                "anyOf": [
                    {
                        "additionalProperties": {
                            "type": "string",
                        },
                        "type": "object",
                    },
                    {
                        "type": "null",
                    },
                ],
            },
        },
        "required": ["x", "y", "z"],
    }


@pytest.mark.filterwarnings("ignore")
def test_invoke_tool_returns_tool_result():
    chat = ChatOpenAI()

    def tool():
        return 1

    chat.register_tool(tool)

    def new_tool_request(
        name: str = "tool",
        args: Optional[dict[str, Any]] = None,
    ):
        tool_obj = chat._tools.get(name)
        return ContentToolRequest(
            id="id",
            name=name,
            arguments=args or {},
            tool=ToolInfo.from_tool(tool_obj) if tool_obj else None,
        )

    req1 = new_tool_request()
    results = list(chat._invoke_tool(req1))
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert res.error is None
    assert res.value == 1
    assert res.request == req1
    assert res.id == req1.id
    assert res.name == req1.name
    assert res.arguments == req1.arguments

    req2 = new_tool_request(args={"x": 1})
    results = list(chat._invoke_tool(req2))
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert res.error is not None
    assert "got an unexpected keyword argument" in str(res.error)
    assert res.value is None
    assert res.request == req2
    assert res.id == req2.id
    assert res.name == req2.name
    assert res.arguments == req2.arguments

    req3 = new_tool_request(
        name="foo",
        args={"x": 1},
    )
    results = list(chat._invoke_tool(req3))
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert "Unknown tool" in str(res.error)
    assert res.value is None
    assert res.request == req3
    assert res.id == req3.id
    assert res.name == req3.name
    assert res.arguments == req3.arguments


@pytest.mark.asyncio
@pytest.mark.filterwarnings("ignore")
async def test_invoke_tool_returns_tool_result_async():
    chat = ChatOpenAI()

    async def tool():
        return 1

    chat.register_tool(tool)

    def new_tool_request(
        name: str = "tool",
        args: Optional[dict[str, Any]] = None,
    ):
        tool_obj = chat._tools.get(name)
        return ContentToolRequest(
            id="id",
            name=name,
            arguments=args or {},
            tool=ToolInfo.from_tool(tool_obj) if tool_obj else None,
        )

    req1 = new_tool_request()
    results = []
    async for result in chat._invoke_tool_async(req1):
        results.append(result)
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert res.error is None
    assert res.value == 1
    assert res.request == req1
    assert res.id == req1.id
    assert res.name == req1.name
    assert res.arguments == req1.arguments

    req2 = new_tool_request(args={"x": 1})
    results = []
    async for result in chat._invoke_tool_async(req2):
        results.append(result)
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert res.error is not None
    assert "got an unexpected keyword argument" in str(res.error)
    assert res.value is None
    assert res.request == req2
    assert res.id == req2.id
    assert res.name == req2.name
    assert res.arguments == req2.arguments

    req3 = new_tool_request(
        name="foo",
        args={"x": 1},
    )
    results = []
    async for result in chat._invoke_tool_async(req3):
        results.append(result)
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, ContentToolResult)
    assert res.id == "id"
    assert "Unknown tool" in str(res.error)
    assert res.value is None
    assert res.request == req3
    assert res.id == req3.id
    assert res.name == req3.name
    assert res.arguments == req3.arguments


def test_tool_custom_result():
    chat = ChatOpenAI()

    class CustomResult(ContentToolResult):
        pass

    def custom_tool():
        return CustomResult(value=1, extra={"foo": "bar"})

    def custom_tool_err():
        return CustomResult(
            value=None,
            error=Exception("foo"),
            extra={"foo": "bar"},
        )

    chat.register_tool(custom_tool)
    chat.register_tool(custom_tool_err)

    tool_obj = chat._tools.get("custom_tool")
    req = ContentToolRequest(
        id="id",
        name="custom_tool",
        arguments={},
        tool=ToolInfo.from_tool(tool_obj) if tool_obj else None,
    )

    tool_err_obj = chat._tools.get("custom_tool_err")
    req_err = ContentToolRequest(
        id="id",
        name="custom_tool_err",
        arguments={},
        tool=ToolInfo.from_tool(tool_err_obj) if tool_err_obj else None,
    )

    results = list(chat._invoke_tool(req))
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, CustomResult)
    assert res.id == "id"
    assert res.error is None
    assert res.value == 1
    assert res.extra == {"foo": "bar"}
    assert res.request == req
    assert res.id == req.id
    assert res.name == req.name
    assert res.arguments == req.arguments

    results_err = list(chat._invoke_tool(req_err))
    assert len(results_err) == 1
    res_err = results_err[0]
    assert isinstance(res_err, CustomResult)
    assert res_err.id == "id"
    assert res_err.error is not None
    assert str(res_err.error) == "foo"
    assert res_err.value is None
    assert res_err.extra == {"foo": "bar"}
    assert res_err.request == req_err
    assert res_err.id == req_err.id
    assert res_err.name == req_err.name
    assert res_err.arguments == req_err.arguments


@pytest.mark.asyncio
async def test_tool_custom_result_async():
    chat = ChatOpenAI()

    class CustomResult(ContentToolResult):
        pass

    async def custom_tool():
        return CustomResult(value=1, extra={"foo": "bar"})

    async def custom_tool_err():
        return CustomResult(
            value=None,
            error=Exception("foo"),
            extra={"foo": "bar"},
        )

    chat.register_tool(custom_tool)
    chat.register_tool(custom_tool_err)

    tool_obj = chat._tools.get("custom_tool")
    req = ContentToolRequest(
        id="id",
        name="custom_tool",
        arguments={},
        tool=ToolInfo.from_tool(tool_obj) if tool_obj else None,
    )

    tool_err_obj = chat._tools.get("custom_tool_err")
    req_err = ContentToolRequest(
        id="id",
        name="custom_tool_err",
        arguments={},
        tool=ToolInfo.from_tool(tool_err_obj) if tool_err_obj else None,
    )

    results = []
    async for result in chat._invoke_tool_async(req):
        results.append(result)
    assert len(results) == 1
    res = results[0]
    assert isinstance(res, CustomResult)
    assert res.id == "id"
    assert res.error is None
    assert res.value == 1
    assert res.extra == {"foo": "bar"}
    assert res.request == req
    assert res.id == req.id
    assert res.name == req.name
    assert res.arguments == req.arguments

    results_err = []
    async for result in chat._invoke_tool_async(req_err):
        results_err.append(result)
    assert len(results_err) == 1
    res_err = results_err[0]
    assert isinstance(res_err, CustomResult)
    assert res_err.id == "id"
    assert res_err.error is not None
    assert str(res_err.error) == "foo"
    assert res_err.value is None
    assert res_err.extra == {"foo": "bar"}
    assert res_err.request == req_err
    assert res_err.id == req_err.id
    assert res_err.name == req_err.name
    assert res_err.arguments == req_err.arguments


def test_content_tool_request_serializable():
    """Test that ContentToolRequest with Tool instance is JSON serializable"""
    chat = ChatOpenAI()

    def add(x: int, y: int) -> int:
        """Add two numbers"""
        return x + y

    chat.register_tool(add)

    # Create a ContentToolRequest with the Tool info
    tool = chat._tools["add"]
    request = ContentToolRequest(
        id="test-123",
        name="add",
        arguments={"x": 1, "y": 2},
        tool=ToolInfo.from_tool(tool),
    )

    # Test that it can be serialized to JSON
    json_data = request.model_dump_json()
    assert isinstance(json_data, str)

    # Test that the JSON can be parsed
    parsed = ContentToolRequest.model_validate_json(json_data)
    assert parsed.id == "test-123"
    assert parsed.name == "add"
    assert parsed.arguments == {"x": 1, "y": 2}
    assert parsed.content_type == "tool_request"

    # Test that the tool is serialized (func is excluded from serialization)
    assert parsed.tool is not None
    assert parsed.tool.name == "add"
    assert parsed.tool.description == "Add two numbers"


def test_content_tool_result_pandas_dataframe():
    """Test ContentToolResult with pandas DataFrame using orient='records'"""
    pandas = pytest.importorskip("pandas")

    # Create a simple pandas DataFrame
    df = pandas.DataFrame(
        {"name": ["Alice", "Bob"], "age": [25, 30], "city": ["New York", "London"]}
    )

    # Create ContentToolResult with DataFrame value
    result = ContentToolResult(value=df).get_model_value()
    expected = df.to_json(orient="records")
    assert result == expected

    parsed = orjson.loads(str(result))
    assert isinstance(parsed, list)
    assert len(parsed) == 2
    assert parsed[0] == {"name": "Alice", "age": 25, "city": "New York"}
    assert parsed[1] == {"name": "Bob", "age": 30, "city": "London"}


def test_content_tool_result_object_with_to_pandas():
    """Test ContentToolResult with objects that have .to_pandas() method"""
    pandas = pytest.importorskip("pandas")

    # Create mock object with to_pandas method (like Polars, PyArrow)
    mock_df_lib = Mock()
    pandas_df = pandas.DataFrame({"x": [1, 2, 3], "y": ["a", "b", "c"]})
    mock_df_lib.to_pandas.return_value = pandas_df

    result = ContentToolResult(value=mock_df_lib).get_model_value()
    mock_df_lib.to_pandas.assert_called_once()
    expected = pandas_df.to_json(orient="records")
    assert result == expected


def test_content_tool_result_narwhals_dataframe():
    """Test ContentToolResult with narwhals DataFrame"""
    narwhals = pytest.importorskip("narwhals")
    pandas = pytest.importorskip("pandas")

    pandas_df = pandas.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    nw_df = narwhals.from_native(pandas_df)
    result = ContentToolResult(value=nw_df).get_model_value()
    expected = pandas_df.to_json(orient="records")
    assert result == expected


def test_content_tool_result_object_with_to_dict():
    """Test ContentToolResult with objects that have to_dict method"""
    # Mock object with to_dict method but no to_pandas or to_json
    mock_obj = Mock(spec=["to_dict"])
    mock_obj.to_dict.return_value = {"key": "value"}
    result = ContentToolResult(value=mock_obj).get_model_value()
    mock_obj.to_dict.assert_called_once()
    # Result should be JSON string representation (orjson format)
    assert result == '{"key":"value"}'


def test_content_tool_result_string_passthrough():
    """Test ContentToolResult with string values (special case - passed through as-is)"""
    result = ContentToolResult(value="plain string").get_model_value()
    assert result == "plain string"


def test_content_tool_result_fallback_serialization():
    """Test ContentToolResult fallback for objects without special methods"""
    # Regular object without to_json, to_pandas, or to_dict (non-string to avoid the string special case)
    result = ContentToolResult(value={"key": "value"}).get_model_value()
    assert result == '{"key":"value"}'


def test_content_tool_result_explicit_json_mode():
    """Test ContentToolResult with explicit JSON mode forces _to_json for non-strings"""
    # Test with non-string object and explicit JSON mode
    result = ContentToolResult(
        value={"key": "value"},
        model_format="json",
    ).get_model_value()
    # With explicit JSON mode, objects get JSON-encoded
    assert result == '{"key":"value"}'
    # Test that strings still get special treatment even in JSON mode
    string_result = ContentToolResult(
        value="plain string",
        model_format="json",
    ).get_model_value()
    # Strings are still returned as-is even in JSON mode (current behavior)
    assert string_result == "plain string"
