from typing import Literal

type FinishReason = Literal[
    "stop", "length", "tool_calls", "content_filter", "function_call"
]
type ResponseStatus = Literal["in_progress", "completed", "started", "failed"]
