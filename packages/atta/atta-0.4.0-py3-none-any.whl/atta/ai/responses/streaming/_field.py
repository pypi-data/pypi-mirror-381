from atta.ai.responses.types import ResponseStatus
from atta.observability.conventions.genai import GenAITelemetryFields
from atta.observability.tracing.attributes import semcov_field


def _semcov_status_field(default_status: ResponseStatus) -> ResponseStatus:
    """Factory function for creating semcov status fields."""
    return semcov_field(
        GenAITelemetryFields.RESPONSE_STATUS.value, default=default_status
    )
