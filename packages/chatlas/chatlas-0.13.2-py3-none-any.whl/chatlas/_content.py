from __future__ import annotations

import inspect
import warnings
from pprint import pformat
from typing import TYPE_CHECKING, Any, Literal, Optional, Union, cast

import orjson
from pydantic import BaseModel, ConfigDict

from ._typing_extensions import TypedDict

if TYPE_CHECKING:
    from ._tools import Tool


class ToolAnnotations(TypedDict, total=False):
    """
    Additional properties describing a Tool to clients.

    NOTE: all properties in ToolAnnotations are **hints**.
    They are not guaranteed to provide a faithful description of
    tool behavior (including descriptive properties like `title`).

    Clients should never make tool use decisions based on ToolAnnotations
    received from untrusted servers.
    """

    title: str
    """A human-readable title for the tool."""

    readOnlyHint: bool
    """
    If true, the tool does not modify its environment.
    Default: false
    """

    destructiveHint: bool
    """
    If true, the tool may perform destructive updates to its environment.
    If false, the tool performs only additive updates.
    (This property is meaningful only when `readOnlyHint == false`)
    Default: true
    """

    idempotentHint: bool
    """
    If true, calling the tool repeatedly with the same arguments
    will have no additional effect on the its environment.
    (This property is meaningful only when `readOnlyHint == false`)
    Default: false
    """

    openWorldHint: bool
    """
    If true, this tool may interact with an "open world" of external
    entities. If false, the tool's domain of interaction is closed.
    For example, the world of a web search tool is open, whereas that
    of a memory tool is not.
    Default: true
    """

    extra: dict[str, Any]
    """
    Additional metadata about the tool.
    """


ImageContentTypes = Literal[
    "image/png",
    "image/jpeg",
    "image/webp",
    "image/gif",
]
"""
Allowable content types for images.
"""


class ToolInfo(BaseModel):
    """
    Serializable tool information

    This contains only the serializable parts of a Tool that are needed
    for ContentToolRequest to be JSON-serializable. This allows tool
    metadata to be preserved without including the non-serializable
    function reference.

    Parameters
    ----------
    name
        The name of the tool.
    description
        A description of what the tool does.
    parameters
        A dictionary describing the input parameters and their types.
    annotations
        Additional properties that describe the tool and its behavior.
    """

    name: str
    description: str
    parameters: dict[str, Any]
    annotations: Optional[ToolAnnotations] = None

    @classmethod
    def from_tool(cls, tool: "Tool") -> "ToolInfo":
        """Create a ToolInfo from a Tool instance."""
        func_schema = tool.schema["function"]
        return cls(
            name=tool.name,
            description=func_schema.get("description", ""),
            parameters=func_schema.get("parameters", {}),
            annotations=tool.annotations,
        )


ContentTypeEnum = Literal[
    "text",
    "image_remote",
    "image_inline",
    "tool_request",
    "tool_result",
    "tool_result_image",
    "tool_result_resource",
    "json",
    "pdf",
]
"""
A discriminated union of all content types.
"""


class Content(BaseModel):
    """
    Base class for all content types that can be appear in a [](`~chatlas.Turn`)
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    content_type: ContentTypeEnum

    def __str__(self):
        raise NotImplementedError

    def _repr_markdown_(self):
        raise NotImplementedError

    def __repr__(self, indent: int = 0):
        raise NotImplementedError


class ContentText(Content):
    """
    Text content for a [](`~chatlas.Turn`)
    """

    text: str
    content_type: ContentTypeEnum = "text"

    def __init__(self, **data: Any):
        super().__init__(**data)

        if self.text == "" or self.text.isspace():
            self.text = "[empty string]"

    def __str__(self):
        return self.text

    def _repr_markdown_(self):
        return self.text

    def __repr__(self, indent: int = 0):
        text = self.text[:50] + "..." if len(self.text) > 50 else self.text
        return " " * indent + f"<ContentText text='{text}'>"


class ContentImage(Content):
    """
    Base class for image content.

    This class is not meant to be used directly. Instead, use
    [](`~chatlas.content_image_url`), [](`~chatlas.content_image_file`), or
    [](`~chatlas.content_image_plot`).
    """

    pass


class ContentImageRemote(ContentImage):
    """
    Image content from a URL.

    This is the return type for [](`~chatlas.content_image_url`).
    It's not meant to be used directly.

    Parameters
    ----------
    url
        The URL of the image.
    detail
        A detail setting for the image. Can be `"auto"`, `"low"`, or `"high"`.
    """

    url: str
    detail: Literal["auto", "low", "high"] = "auto"

    content_type: ContentTypeEnum = "image_remote"

    def __str__(self):
        return f"![]({self.url})"

    def _repr_markdown_(self):
        return self.__str__()

    def __repr__(self, indent: int = 0):
        return (
            " " * indent
            + f"<ContentImageRemote url='{self.url}' detail='{self.detail}'>"
        )


class ContentImageInline(ContentImage):
    """
    Inline image content.

    This is the return type for [](`~chatlas.content_image_file`) and
    [](`~chatlas.content_image_plot`).
    It's not meant to be used directly.

    Parameters
    ----------
    image_content_type
        The content type of the image.
    data
        The base64-encoded image data.
    """

    image_content_type: ImageContentTypes
    data: Optional[str] = None

    content_type: ContentTypeEnum = "image_inline"

    def __str__(self):
        return f"![](data:{self.image_content_type};base64,{self.data})"

    def _repr_markdown_(self):
        return self.__str__()

    def __repr__(self, indent: int = 0):
        n_bytes = len(self.data) if self.data else 0
        return (
            " " * indent
            + f"<ContentImageInline content_type='{self.image_content_type}' size={n_bytes}>"
        )


class ContentToolRequest(Content):
    """
    A request to call a tool/function

    This content type isn't meant to be used directly. Instead, it's
    automatically generated by [](`~chatlas.Chat`) when a tool/function is
    requested by the model assistant.

    Parameters
    ----------
    id
        A unique identifier for this request.
    name
        The name of the tool/function to call.
    arguments
        The arguments to pass to the tool/function.
    tool
        Serializable information about the tool. This is set internally by
        chatlas's tool calling loop and contains only the metadata needed
        for serialization (name, description, parameters, annotations).
    """

    id: str
    name: str
    arguments: object
    tool: Optional[ToolInfo] = None

    content_type: ContentTypeEnum = "tool_request"

    def __str__(self):
        args_str = self._arguments_str()
        func_call = f"{self.name}({args_str})"
        comment = f"# 🔧 tool request ({self.id})"
        return f"```python\n{comment}\n{func_call}\n```\n"

    def _repr_markdown_(self):
        return self.__str__()

    def __repr__(self, indent: int = 0):
        args_str = self._arguments_str()
        return (
            " " * indent
            + f"<ContentToolRequest name='{self.name}' arguments='{args_str}' id='{self.id}'>"
        )

    def _arguments_str(self) -> str:
        if isinstance(self.arguments, dict):
            return ", ".join(f"{k}={v}" for k, v in self.arguments.items())
        return str(self.arguments)

    def __repr_html__(self) -> str:
        return str(self.tagify())

    def tagify(self):
        "Returns an HTML string suitable for passing to htmltools/shiny's `Chat()` component."
        try:
            from htmltools import HTML, TagList, head_content, tags
        except ImportError:
            raise ImportError(
                ".tagify() is only intended to be called by htmltools/shiny, ",
                "but htmltools is not installed. ",
            )

        html = f"<p></p><span class='chatlas-tool-request'>🔧 Running tool: <code>{self.name}</code></span>"

        return TagList(
            HTML(html),
            head_content(tags.style(TOOL_CSS)),
        )


class ContentToolResult(Content):
    """
    The result of calling a tool/function

    A content type representing the result of a tool function call. When a model
    requests a tool function, [](`~chatlas.Chat`) will create, (optionally)
    echo, (optionally) yield, and store this content type in the chat history.

    A tool function may also construct an instance of this class and return it.
    This is useful for a tool that wishes to customize how the result is handled
    (e.g., the format of the value sent to the model).

    Parameters
    ----------
    value
        The return value of the tool/function.
    model_format
        The format used for sending the value to the model. The default,
        `"auto"`, first attempts to format the value as a JSON string. If that
        fails, it gets converted to a string via `str()`. To force
        `orjson.dumps()` or `str()`, set to `"json"` or `"str"`. Finally,
        `"as_is"` is useful for doing your own formatting and/or passing a
        non-string value (e.g., a list or dict) straight to the model.
        Non-string values are useful for tools that return images or other
        'known' non-text content types.
    error
        An exception that occurred while invoking the tool. If this is set, the
        error message sent to the model and the value is ignored.
    extra
       Additional data associated with the tool result that isn't sent to the
       model.
    request
        Not intended to be used directly. It will be set when the
        :class:`~chatlas.Chat` invokes the tool.

    Note
    ----
    When `model_format` is `"json"` (or `"auto"`), and the value has a
    `.to_json()`/`.to_dict()` method, those methods are called to obtain the
    JSON representation of the value. This is convenient for classes, like
    `pandas.DataFrame`, that have a `.to_json()` method, but don't necessarily
    dump to JSON directly. If this happens to not be the desired behavior, set
    `model_format="as_is"` return the desired value as-is.
    """

    # public
    value: Any
    model_format: Literal["auto", "json", "str", "as_is"] = "auto"
    error: Optional[Exception] = None
    extra: Any = None

    # "private"
    request: Optional[ContentToolRequest] = None
    content_type: ContentTypeEnum = "tool_result"

    @property
    def id(self):
        if not self.request:
            raise ValueError("id is only available after the tool has been called")
        return self.request.id

    @property
    def name(self):
        if not self.request:
            raise ValueError("name is only available after the tool has been called")
        return self.request.name

    @property
    def arguments(self):
        if not self.request:
            raise ValueError(
                "arguments is only available after the tool has been called"
            )
        return self.request.arguments

    # Primarily used for `echo="all"`...
    def __str__(self):
        prefix = "✅ tool result" if not self.error else "❌ tool error"
        comment = f"# {prefix} ({self.id})"
        value = self._get_display_value()
        return f"""```python\n{comment}\n{value}\n```"""

    # ... and for displaying in the notebook
    def _repr_markdown_(self):
        return self.__str__()

    def __repr__(self, indent: int = 0):
        res = " " * indent
        res += f"<ContentToolResult value='{self.value}' id='{self.id}'"
        if self.error:
            res += f" error='{self.error}'"
        return res + ">"

    # Format the value for display purposes
    def _get_display_value(self):
        if self.error:
            return f"Tool call failed with error: '{self.error}'"

        val = self.value

        # If value is already a dict or list, format it directly
        if isinstance(val, (dict, list)):
            return pformat(val, indent=2, sort_dicts=False)

        # For string values, try to parse as JSON
        if isinstance(val, str):
            try:
                json_val = orjson.loads(val)
                return pformat(json_val, indent=2, sort_dicts=False)
            except orjson.JSONDecodeError:
                # Not valid JSON, return as string
                return val

        return str(val)

    def get_model_value(self) -> object:
        "Get the actual value sent to the model."

        if self.error:
            return f"Tool call failed with error: '{self.error}'"

        val, mode = (self.value, self.model_format)

        if isinstance(val, str):
            return val

        if mode == "auto":
            try:
                return self._to_json(val)
            except Exception:
                return str(val)
        elif mode == "json":
            return self._to_json(val)
        elif mode == "str":
            return str(val)
        elif mode == "as_is":
            return val
        else:
            raise ValueError(f"Unknown format mode: {mode}")

    @staticmethod
    def _to_json(value: Any) -> object:
        if hasattr(value, "to_pandas") and callable(value.to_pandas):
            # Many (most?) df libs (polars, pyarrow, ...) have a .to_pandas()
            # method, and pandas has a .to_json() method
            value = value.to_pandas()

        if hasattr(value, "to_json") and callable(value.to_json):
            # pandas defaults to "columns", which is not ideal for LLMs
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
            sig = inspect.signature(value.to_json)
            if "orient" in list(sig.parameters.keys()):
                return value.to_json(orient="records")
            else:
                return value.to_json()

        # Support for df libs (beyond those with a .to_pandas() method)
        if hasattr(value, "__narwhals_dataframe__"):
            try:
                import narwhals

                val = cast(narwhals.DataFrame, narwhals.from_native(value))
                return val.to_pandas().to_json(orient="records")
            except ImportError:
                warnings.warn(
                    f"Tool result object of type {type(value)} appears to be a "
                    "narwhals-compatible DataFrame. If you run into issues with "
                    "the LLM not understanding this value, try installing narwhals: "
                    "`pip install narwhals`.",
                    ImportWarning,
                    stacklevel=2,
                )

        if hasattr(value, "to_dict") and callable(value.to_dict):
            value = value.to_dict()

        return orjson.dumps(value).decode("utf-8")

    def __repr_html__(self):
        return str(self.tagify())

    def tagify(self):
        "A method for rendering this object via htmltools/shiny."
        try:
            from htmltools import HTML, html_escape
        except ImportError:
            raise ImportError(
                ".tagify() is only intended to be called by htmltools/shiny, ",
                "but htmltools is not installed. ",
            )

        # Helper function to format code blocks (optionally with labels for arguments).
        def pre_code(code: str, label: str | None = None) -> str:
            lbl = f"<span class='input-parameter-label'>{label}</span>" if label else ""
            return f"<pre>{lbl}<code>{html_escape(code)}</code></pre>"

        # Helper function to wrap content in a <details> block.
        def details_block(summary: str, content: str, open_: bool = True) -> str:
            open_attr = " open" if open_ else ""
            return (
                f"<details{open_attr}><summary>{summary}</summary>{content}</details>"
            )

        # First, format the input parameters.
        args = self.arguments or {}
        if isinstance(args, dict):
            args = "".join(pre_code(str(v), label=k) for k, v in args.items())
        else:
            args = pre_code(str(args))

        # Wrap the input parameters in an (open) details block.
        if args:
            params = details_block("<strong>Input parameters:</strong>", args)
        else:
            params = ""

        # Also wrap the tool result in an (open) details block.
        result = details_block(
            "<strong>Result:</strong>",
            pre_code(self._get_display_value()),
        )

        # Put both the result and parameters into a container
        result_div = f'<div class="chatlas-tool-result-content">{result}{params}</div>'

        # Header for the top-level result details block.
        if not self.error:
            header = f"Result from tool call: <code>{self.name}</code>"
        else:
            header = f"❌ Failed to call tool <code>{self.name}</code>"

        res = details_block(header, result_div, open_=False)

        return HTML(f'<div class="chatlas-tool-result">{res}</div>')

    def _arguments_str(self) -> str:
        if isinstance(self.arguments, dict):
            return ", ".join(f"{k}={v}" for k, v in self.arguments.items())
        return str(self.arguments)


class ContentToolResultImage(ContentToolResult):
    """
    A tool result that contains an image.

    This is a specialized version of ContentToolResult for returning images.
    It requires the image data to be base64-encoded (as `value`) and
    the MIME type of the image (as `mime_type`).

    Parameters
    ----------
    value
        The image data as a base64-encoded string.
    mime_type
        The MIME type of the image (e.g., "image/png").
    """

    value: str
    model_format: Literal["auto", "json", "str", "as_is"] = "as_is"
    mime_type: ImageContentTypes

    content_type: ContentTypeEnum = "tool_result_image"

    def __str__(self):
        return f"<ContentToolResultImage mime_type='{self.mime_type}'>"

    def _repr_markdown_(self):
        return f"![](data:{self.mime_type};base64,{self.value})"


class ContentToolResultResource(ContentToolResult):
    """
    A tool result that contains a resource.

    This is a specialized version of ContentToolResult for returning resources
    (e.g., images, files) as raw bytes. It requires the resource data to be
    provided as bytes (as `value`) and the MIME type of the resource (as
    `mime_type`).

    Parameters
    ----------
    value
        The resource data, in bytes.
    mime_type
        The MIME type of the image (e.g., "image/png").
    """

    value: bytes
    model_format: Literal["auto", "json", "str", "as_is"] = "as_is"
    mime_type: Optional[str]

    content_type: ContentTypeEnum = "tool_result_resource"

    def __str__(self):
        return f"<ContentToolResultResource mime_type='{self.mime_type}'>"

    def _repr_mimebundle_(self, include=None, exclude=None):
        return {
            self.mime_type: self.value,
            "text/plain": f"<{self.mime_type} object>",
        }


class ContentJson(Content):
    """
    JSON content

    This content type primarily exists to signal structured data extraction
    (i.e., data extracted via [](`~chatlas.Chat`)'s `.chat_structured()` method)

    Parameters
    ----------
    value
        The JSON data extracted
    """

    value: dict[str, Any]

    content_type: ContentTypeEnum = "json"

    def __str__(self):
        return orjson.dumps(self.value, option=orjson.OPT_INDENT_2).decode("utf-8")

    def _repr_markdown_(self):
        return f"""```json\n{self.__str__()}\n```"""

    def __repr__(self, indent: int = 0):
        return " " * indent + f"<ContentJson value={self.value}>"


class ContentPDF(Content):
    """
    PDF content

    This content type primarily exists to signal PDF data extraction
    (i.e., data extracted via [](`~chatlas.Chat`)'s `.chat_structured()` method)

    Parameters
    ----------
    value
        The PDF data extracted
    """

    data: bytes

    content_type: ContentTypeEnum = "pdf"

    def __str__(self):
        return "<PDF document>"

    def _repr_markdown_(self):
        return self.__str__()

    def __repr__(self, indent: int = 0):
        return " " * indent + f"<ContentPDF size={len(self.data)}>"


ContentUnion = Union[
    ContentText,
    ContentImageRemote,
    ContentImageInline,
    ContentToolRequest,
    ContentToolResult,
    ContentToolResultImage,
    ContentToolResultResource,
    ContentJson,
    ContentPDF,
]


def create_content(data: dict[str, Any]) -> ContentUnion:
    """
    Factory function to create the appropriate Content subclass based on the data.

    This is useful when deserializing content from JSON.
    """
    if not isinstance(data, dict):
        raise ValueError("Content data must be a dictionary")

    ct = data.get("content_type")

    if ct == "text":
        return ContentText.model_validate(data)
    elif ct == "image_remote":
        return ContentImageRemote.model_validate(data)
    elif ct == "image_inline":
        return ContentImageInline.model_validate(data)
    elif ct == "tool_request":
        return ContentToolRequest.model_validate(data)
    elif ct == "tool_result":
        return ContentToolResult.model_validate(data)
    elif ct == "tool_result_image":
        return ContentToolResultImage.model_validate(data)
    elif ct == "tool_result_resource":
        return ContentToolResultResource.model_validate(data)
    elif ct == "json":
        return ContentJson.model_validate(data)
    elif ct == "pdf":
        return ContentPDF.model_validate(data)
    else:
        raise ValueError(f"Unknown content type: {ct}")


TOOL_CSS = """
/* Get dot to appear inline, even when in a paragraph following the request */
.chatlas-tool-request + p:has(.markdown-stream-dot) {
  display: inline;
}

/* Hide request when anything other than a dot follows it */
.chatlas-tool-request:not(:has(+ p .markdown-stream-dot)) {
  display: none;
}

.chatlas-tool-request, .chatlas-tool-result {
  font-weight: 300;
  font-size: 0.9rem;
}

.chatlas-tool-result {
  display: inline-block;
  width: 100%;
  margin-bottom: 1rem;
}

.chatlas-tool-result summary {
  list-style: none;
  cursor: pointer;
}

.chatlas-tool-result summary::after {
  content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-caret-right-fill' viewBox='0 0 16 16'%3E%3Cpath d='m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z'/%3E%3C/svg%3E");
  font-size: 1.15rem;
  margin-left: 0.25rem;
  vertical-align: middle;
}

.chatlas-tool-result details[open] summary::after {
  content: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-caret-down-fill' viewBox='0 0 16 16'%3E%3Cpath d='M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z'/%3E%3C/svg%3E");
}

.chatlas-tool-result-content {
  position: relative;
  border: 1px solid var(--bs-border-color, #0066cc);
  width: 100%;
  padding: 1rem;
  border-radius: var(--bs-border-radius, 0.2rem);
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.chatlas-tool-result-content pre, .chatlas-tool-result-content code {
  background-color: var(--bs-body-bg, white) !important;
}

.chatlas-tool-result-content .input-parameter-label {
  position: absolute;
  top: 0;
  width: 100%;
  text-align: center;
  font-weight: 300;
  font-size: 0.8rem;
  color: var(--bs-gray-600);
  background-color: var(--bs-body-bg);
  padding: 0.5rem;
  font-family: var(--bs-font-monospace, monospace);
}

pre:has(> .input-parameter-label) {
  padding-top: 1.5rem;
}

shiny-markdown-stream p:first-of-type:empty {
  display: none;
}
"""
