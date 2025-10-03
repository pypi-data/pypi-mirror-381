from attrs import define

from atta.ai.responses.types import ResponseStatus


@define(slots=True, kw_only=True)
class ReasoningContent:
    """Reasoning content block."""

    content: str
    type: str = "reasoning_text"


@define(slots=True, kw_only=True)
class ReasoningSummary:
    """Reasoning summary."""

    text: str
    type: str = "summary_text"


@define(slots=True, kw_only=True)
class ResponseReasoningItem:
    """Reasoning output item from response."""

    id: str
    summary: list[ReasoningSummary]
    content: list[ReasoningContent] | None = None
    encrypted_content: str | None = None
    status: ResponseStatus | None = None
    type: str = "reasoning"
