from enum import StrEnum


class ChatRole(StrEnum):
    """Chat roles."""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"
    DEVELOPER = "developer"
