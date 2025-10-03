from typing import Any

from attrs import NOTHING, field

from atta.utils.attributes import extract_attributes

SEMCOV_FIELD_METADATA_KEY = "semcov_attribute"


def semcov_field(  # type: ignore[no-untyped-def]
    semcov_attribute: str,
    default=NOTHING,
    validator=None,
    repr: bool = True,
    eq: bool = True,
    order=None,
    hash=None,
    init: bool = True,
    metadata: dict[str, Any] | None = None,
    converter=None,
) -> Any:
    """Create a field that tracks semantic-convention attributes."""
    if not isinstance(semcov_attribute, str) or not semcov_attribute.strip():
        raise ValueError("`telemetry_attribute` must be a non-empty string")

    metadata = {} if metadata is None else metadata.copy()
    metadata[SEMCOV_FIELD_METADATA_KEY] = semcov_attribute

    return field(
        default=default,
        validator=validator,
        repr=repr,
        eq=eq,
        order=order,
        hash=hash,
        init=init,
        metadata=metadata,
        converter=converter,
    )


def extract_semcov_attributes(obj: object | type) -> dict[str, Any]:
    """Extract semantic convention attributes from an attrs object."""
    return extract_attributes(obj, SEMCOV_FIELD_METADATA_KEY)
