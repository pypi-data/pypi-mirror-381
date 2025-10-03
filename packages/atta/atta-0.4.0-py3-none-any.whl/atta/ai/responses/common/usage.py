from attrs import define

from atta.observability.conventions.genai import GenAITelemetryFields
from atta.observability.tracing.attributes import semcov_field


@define(slots=True, kw_only=True)
class InputTokensDetails:
    """Input token usage details."""

    cached_tokens: int | None = semcov_field(
        GenAITelemetryFields.USAGE_INPUT_CACHED_TOKENS.value, default=None
    )


@define(slots=True, kw_only=True)
class OutputTokensDetails:
    """Output token usage details."""

    reasoning_tokens: int | None = semcov_field(
        GenAITelemetryFields.USAGE_OUTPUT_REASONING_TOKENS.value, default=None
    )


@define(slots=True, kw_only=True)
class ResponseUsage:
    """Token usage information."""

    input_tokens: int | None = semcov_field(
        GenAITelemetryFields.USAGE_INPUT_TOKENS.value, default=None
    )
    input_tokens_details: InputTokensDetails | None = None
    output_tokens: int | None = semcov_field(
        GenAITelemetryFields.USAGE_OUTPUT_TOKENS.value, default=None
    )
    output_tokens_details: OutputTokensDetails | None = None
    total_tokens: int | None = semcov_field(
        GenAITelemetryFields.USAGE_TOTAL_TOKENS.value, default=None
    )
