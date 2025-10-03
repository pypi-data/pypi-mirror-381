from typing import Any

import attrs


def extract_attributes(
    obj: object | type, metadata_key: str, _visited: set[int] | None = None
) -> dict[str, Any]:
    """Extract attributes from an attrs object based on metadata key.

    Args:
        obj: The attrs object to extract attributes from.
        metadata_key: The metadata key to look for in field definitions.
        _visited: Internal set for circular reference protection.

    Returns:
        Dictionary of extracted attributes.

    Raises:
        ValueError: If duplicate attributes are found.
    """
    if obj is None or not attrs.has(obj):  # type: ignore[arg-type]
        return {}

    if _visited is None:
        _visited = set()

    obj_id = id(obj)
    if obj_id in _visited:
        return {}  # Circular reference protection

    _visited.add(obj_id)

    try:
        attributes: dict[str, Any] = {}

        for field_def in attrs.fields(type(obj)):  # type: ignore[arg-type]
            field_value = getattr(obj, field_def.name, None)

            if field_value is None:
                continue

            # Handle nested attrs objects
            if attrs.has(field_value):
                nested_attrs = extract_attributes(field_value, metadata_key, _visited)
                # Check for duplicates
                duplicates = set(attributes.keys()) & set(nested_attrs.keys())
                if duplicates:
                    raise ValueError(
                        f"Duplicate attributes: {', '.join(sorted(duplicates))}"
                    )
                attributes.update(nested_attrs)

            # Handle metadata fields
            attr_name = field_def.metadata.get(metadata_key)
            if attr_name:
                if attr_name in attributes:
                    raise ValueError(f"Duplicate attribute '{attr_name}'")
                attributes[attr_name] = field_value

        return attributes

    finally:
        _visited.discard(obj_id)
