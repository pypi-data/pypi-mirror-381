from typing import Literal

from attrs import define

from atta.ai.responses.common import OutputItem
from atta.ai.responses.standard.text import TextResponse
from atta.ai.responses.streaming._field import _semcov_status_field
from atta.ai.responses.types import ResponseStatus

# Event type constants
TEXT_DELTA_EVENT = "response.output_text.delta"
SUMMARY_TEXT_DELTA_EVENT = "response.reasoning_summary_text.delta"
OUTPUT_ITEM_DONE_EVENT = "response.output_item.done"
RESPONSE_COMPLETED_EVENT = "response.completed"


# ----------
# Items
# ----------


@define(slots=True, kw_only=True)
class TextResponseTextDeltaEvent:
    """Stream event for text delta."""

    delta: str
    logprobs: dict[str, float] | None = None
    type: Literal["response.output_text.delta"] = TEXT_DELTA_EVENT
    status: ResponseStatus = _semcov_status_field("in_progress")


@define(slots=True, kw_only=True)
class TextResponseSummaryTextDeltaEvent:
    """Stream event for summary text delta."""

    delta: str
    type: Literal["response.reasoning_summary_text.delta"] = SUMMARY_TEXT_DELTA_EVENT
    status: ResponseStatus = _semcov_status_field("in_progress")


@define(slots=True, kw_only=True)
class TextResponseOutputItemDoneEvent:
    """Stream event for output item done."""

    item: OutputItem
    type: Literal["response.output_item.done"] = OUTPUT_ITEM_DONE_EVENT
    status: ResponseStatus = _semcov_status_field("in_progress")


@define(slots=True, kw_only=True)
class TextResponseCompletedEvent:
    """Stream event for response completed."""

    response: TextResponse
    type: Literal["response.completed"] = RESPONSE_COMPLETED_EVENT
    status: ResponseStatus = _semcov_status_field("completed")


# ----------
# Union type for stream event
# ----------

type TextResponseStreamEvent = (
    TextResponseTextDeltaEvent
    | TextResponseSummaryTextDeltaEvent
    | TextResponseOutputItemDoneEvent
    | TextResponseCompletedEvent
)
