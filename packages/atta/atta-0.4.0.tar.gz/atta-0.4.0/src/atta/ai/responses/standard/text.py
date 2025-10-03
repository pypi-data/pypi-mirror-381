from typing import Literal

from attrs import define, field
from pendulum import DateTime

from atta.ai.responses.common import (
    OutputItem,
    ResponseFunctionToolCall,
    ResponseMessage,
)
from atta.ai.responses.common.reasoning import ResponseReasoningItem
from atta.ai.responses.common.usage import ResponseUsage
from atta.ai.responses.types import ResponseStatus
from atta.observability.conventions.genai import GenAITelemetryFields
from atta.observability.tracing.attributes import semcov_field
from atta.utils.time import current_time


@define(slots=True, kw_only=True)
class TextResponse:
    """Unified response matching OpenAI response format as golden reference.

    AeroAI's internal unified response formats to allow for easy provider migrations.
    """

    # Base
    id: str = semcov_field(GenAITelemetryFields.RESPONSE_ID.value)
    model: str = semcov_field(GenAITelemetryFields.RESPONSE_MODEL.value)
    provider: str = semcov_field(GenAITelemetryFields.PROVIDER_NAME.value)

    # Core
    output: list[OutputItem]
    usage: ResponseUsage | None = None

    # Metadata
    received_at: DateTime = field(factory=current_time)
    object: Literal["text_response"] = "text_response"
    status: ResponseStatus | None = semcov_field(
        GenAITelemetryFields.RESPONSE_STATUS.value, default=None
    )

    # Semantic Convention Attributes
    _output_type: str = semcov_field(
        GenAITelemetryFields.OUTPUT_TYPE.value, default="text", init=False, repr=False
    )
    _tool_calls_count: int = semcov_field(
        GenAITelemetryFields.TOOL_CALLS_COUNT.value, default=0, init=False, repr=False
    )
    _tool_calls_names: list[str] = semcov_field(
        GenAITelemetryFields.TOOL_NAMES.value, default=[], init=False, repr=False
    )

    def __attrs_post_init__(self):
        """Post-initialization hook to set tool call attributes."""
        _tool_calls = self.function_calls

        self._tool_calls_count = len(_tool_calls)
        self._tool_calls_names = [tool_call.name for tool_call in _tool_calls]

    @property
    def function_calls(self) -> tuple[ResponseFunctionToolCall, ...]:
        """Returns a tuple of function call items from the output."""
        return tuple(
            item for item in self.output if isinstance(item, ResponseFunctionToolCall)
        )

    @property
    def reasoning_items(self) -> tuple[ResponseReasoningItem, ...]:
        """Returns a tuple of reasoning items from the output."""
        return tuple(
            item for item in self.output if isinstance(item, ResponseReasoningItem)
        )

    @property
    def messages(self) -> tuple[ResponseMessage, ...]:
        """Returns a tuple of message items from the output."""
        return tuple(item for item in self.output if isinstance(item, ResponseMessage))

    @property
    def content_items(self) -> list[OutputItem]:
        """Returns the list of all output items."""
        return self.output
