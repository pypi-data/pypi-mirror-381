from collections.abc import Generator, Mapping
from contextlib import contextmanager
from typing import Any

from attrs import define

from atta.observability.tracing.common import TraceIds
from atta.observability.tracing.typing import SpanProtocol, TracingProtocol


@define(slots=True, kw_only=True)
class NoOpSpan(SpanProtocol):
    """No-op span."""

    def set_attribute(self, key: str, value: Any) -> None:
        """No-op attribute setting."""

    def set_attributes(self, attributes: Mapping[str, Any]) -> None:
        """No-op attributes setting."""

    @property
    def raw(self) -> Any:
        """No raw span for no-op - returns NoOpSpan for consistency."""
        return self

    @property
    def context(self) -> Any:
        """No context for no-op - returns NoOpSpan for consistency."""
        return self

    @property
    def correlation_info(self) -> TraceIds:
        """No correlation info for no-op - returns zero IDs."""
        return TraceIds(trace_id=0, span_id=0)


@define(slots=True, kw_only=True)
class NoOpTracer(TracingProtocol[NoOpSpan]):
    """No-op tracer."""

    @contextmanager
    def trace_operation(  # type: ignore[override]
            self,
            _name: str | None = None,
            _attributes: Mapping[str, Any] | None = None,
            _context: Any = None,
            **_params: Any,
    ) -> Generator[NoOpSpan]:
        """No-op tracing - yields empty span.

        Args:
            _name: Name of the operation (ignored).
            _attributes: Dictionary of attributes (ignored).
            _context: OpenTelemetry context (ignored).
            **_params: Additional parameters (ignored).

        Yields:
            NoOpSpan instance.
        """
        yield NoOpSpan()

    @property
    def current_span(self) -> NoOpSpan | None:
        """No current span for no-op tracer - returns noop span for consistency."""
        return NoOpSpan()
