from attrs import define
from pydantic import BaseModel


@define(slots=True, kw_only=True)
class Annotation:
    """Content annotation placeholder."""


@define(slots=True, kw_only=True)
class ContentText:
    """Text content in a message."""

    text: str
    logprobs: dict[str, float] | None = None
    type: str = "text"
    annotations: list[Annotation] | None = None


@define(slots=True, kw_only=True)
class ParsedContent:
    """Parsed content in a message."""

    text: str
    parsed: BaseModel
    logprobs: dict[str, float] | None = None
    type: str = "output_text"
    annotations: list[Annotation] | None = None


@define(slots=True, kw_only=True)
class ContentRefusal:
    """Refusal content in a message."""

    refusal: str
    type: str = "refusal"


type MessageContent = ContentText | ContentRefusal | ParsedContent
