from attrs import define

from atta.ai.responses.common.content import MessageContent
from atta.ai.responses.types import ResponseStatus


@define(slots=True, kw_only=True)
class ResponseMessage:
    """Message output item from response."""

    id: str
    role: str = "assistant"
    content: list[MessageContent] | None = None
    type: str = "message"
    status: ResponseStatus | None = None
