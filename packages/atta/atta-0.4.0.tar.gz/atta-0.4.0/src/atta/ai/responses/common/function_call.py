from typing import Any

from attrs import define, field
import orjson

from atta.ai.responses.types import ResponseStatus


@define(slots=True, kw_only=True)
class ResponseFunctionToolCall:
    """Function tool call output item from response."""

    id: str
    call_id: str
    name: str
    arguments: dict[str, Any] = field(
        converter=lambda x: orjson.loads(x) if isinstance(x, str) else x
    )
    status: ResponseStatus | None = None
    type: str = "function_call"
