from collections.abc import Mapping
from contextlib import AbstractContextManager
from typing import Any, Protocol, runtime_checkable

from atta.observability.tracing.common import TraceIds


@runtime_checkable
class TracingProtocol[T](Protocol):
    """Protocol for tracing."""

    def trace_operation(
        self,
        name: str,
        attributes: Mapping[str, Any] | None = None,
        context: Any = None,
        **params: Any,
    ) -> AbstractContextManager[T]:
        """Trace an operation."""
        ...

    @property
    def current_span(self) -> T | None:
        """Get the current span."""
        ...


@runtime_checkable
class SpanProtocol(Protocol):
    """Protocol for spans."""

    def set_attribute(self, key: str, value: Any) -> None:
        """Set an attribute on the span."""
        ...

    def set_attributes(self, attributes: Mapping[str, Any]) -> None:
        """Set attributes on the span."""

    @property
    def raw(self) -> Any:
        """Get the raw span."""
        ...

    @property
    def context(self) -> Any:
        """Get the span context."""
        ...

    @property
    def correlation_info(self) -> TraceIds:
        """Get correlation info."""
        ...
