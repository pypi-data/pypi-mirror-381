import uuid


def get_id() -> str:
    """Get unique id."""
    return str(uuid.uuid4())
