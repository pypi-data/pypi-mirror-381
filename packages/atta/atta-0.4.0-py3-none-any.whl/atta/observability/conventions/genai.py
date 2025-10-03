from enum import StrEnum


class GenAITelemetryFields(StrEnum):
    """OpenTelemetry GenAI semantic convention fields."""

    # Request attributes
    REQUEST_MODEL = "gen_ai.request.model"
    REQUEST_CHOICE_COUNT = "gen_ai.request.choice_count"
    REQUEST_MAX_TOKENS = "gen_ai.request.max_tokens"
    REQUEST_TEMPERATURE = "gen_ai.request.temperature"
    REQUEST_TOP_P = "gen_ai.request.top_p"
    REQUEST_TOP_K = "gen_ai.request.top_k"
    REQUEST_FREQUENCY_PENALTY = "gen_ai.request.frequency_penalty"
    REQUEST_PRESENCE_PENALTY = "gen_ai.request.presence_penalty"
    REQUEST_STOP_SEQUENCES = "gen_ai.request.stop_sequences"

    # Response attributes
    RESPONSE_ID = "gen_ai.response.id"
    RESPONSE_MODEL = "gen_ai.response.model"
    RESPONSE_FINISH_REASONS = "gen_ai.response.finish_reasons"
    RESPONSE_STATUS = "gen_ai.response.status"

    # Usage/Token attributes
    USAGE_INPUT_TOKENS = "gen_ai.usage.input_tokens"
    USAGE_INPUT_CACHED_TOKENS = "gen_ai.usage.input_cached_tokens"
    USAGE_OUTPUT_TOKENS = "gen_ai.usage.output_tokens"
    USAGE_OUTPUT_REASONING_TOKENS = "gen_ai.usage.output_reasoning_tokens"
    USAGE_TOTAL_TOKENS = "gen_ai.usage.total_tokens"

    # System attributes
    SYSTEM_NAME = "gen_ai.system"  # "openai", "anthropic", "mistral"
    OPERATION_NAME = "gen_ai.operation.name"  # "chat", "completion"

    # Content attributes
    OUTPUT_TYPE = "gen_ai.output.type"  # "text", "json", "image"

    # Conversation attributes
    CONVERSATION_ID = "gen_ai.conversation.id"

    # Tool attributes (extension)
    TOOL_CALLS_COUNT = "gen_ai.tool_calls.count"
    TOOL_NAMES = "gen_ai.tool_calls.names"

    # Provider
    PROVIDER_NAME = "gen_ai.provider.name"


class GenAISystemValues(StrEnum):
    """GenAI system provider values."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    MISTRAL = "mistral"
    GOOGLE = "google"


class GenAIOperationValues(StrEnum):
    """GenAI operation type values."""

    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"


class GenAIOutputTypeValues(StrEnum):
    """GenAI output content type values."""

    TEXT = "text"
    JSON = "json"
    IMAGE = "image"


class GenAIFinishReasonValues(StrEnum):
    """GenAI finish reason values."""

    STOP = "stop"
    LENGTH = "length"
    CONTENT_FILTER = "content_filter"
    TOOL_CALLS = "tool_calls"
    FUNCTION_CALL = "function_call"
    ERROR = "error"
