from collections.abc import Callable


def get_func_name(func: Callable) -> str:  # type: ignore[type-arg]
    """Get func name with the module location.

    Args:
        func: Callable.

    Returns:
        Function/Method name with module location.
    """
    if not callable(func):
        return str(func)

    name = getattr(func, "__name__", str(func))
    module = getattr(func, "__module__", "<unknown>")
    return f"{name}@{module}"
