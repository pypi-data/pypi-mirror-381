from typing import Any

import orjson


def parse_json(data: str | dict[Any, Any] | None) -> dict[Any, Any]:
    """Parse JSON data to dictionary.

    Args:
        data: JSON data.

    Returns:
        Dictionary representation of JSON data.

    Info:
        - If data is None, returns empty dictionary.
        - If data is already a dictionary, returns it as is.
        - If data is not a string, tries to parse it as JSON.
        - If parsing fails, returns empty dictionary.
    """
    if data is None:
        return {}

    if isinstance(data, dict):
        return data

    try:
        return orjson.loads(data)  # type: ignore[no-any-return]
    except orjson.JSONDecodeError:
        return {}
