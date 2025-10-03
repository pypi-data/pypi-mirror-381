from collections.abc import Generator, Mapping
from contextlib import contextmanager
from typing import Any

from attrs import define, field
from opentelemetry import trace
from opentelemetry.context import Context
from opentelemetry.trace import NonRecordingSpan, Span, SpanContext, Tracer

from atta.observability.tracing.common import TraceIds
from atta.observability.tracing.typing import SpanProtocol, TracingProtocol


@define(slots=True, kw_only=True, frozen=True)
class OpenTelemetrySpan(SpanProtocol):
    """OpenTelemetry span."""

    _span: Span

    def set_attribute(self, key: str, value: Any) -> None:
        """Set an attribute on the span.

        Args:
            key: Name of the attribute.
            value: Value of the attribute.

        Returns:
            Nothing.

        Raises:
            ValueError: If the value is None.
        """
        if value is None:
            raise ValueError("Attribute value cannot be None")

        self._span.set_attribute(key, value)

    def set_attributes(self, attributes: Mapping[str, Any]) -> None:
        """Set attributes on the span.

        Args:
            attributes: Dictionary of attributes to set.

        Returns:
            Nothing.

        Raises:
              ValueError: If any value in the dictionary is None.
        """
        for key, value in attributes.items():
            self.set_attribute(key, value)

    @property
    def raw(self) -> Span:
        """Get the raw span."""
        return self._span

    @property
    def context(self) -> SpanContext:
        """Get the span context."""
        return self._span.get_span_context()

    @property
    def correlation_info(self) -> TraceIds:
        """Get correlation info."""
        context = self.context
        return TraceIds(
            span_id=context.span_id,
            trace_id=context.trace_id,
        )


@define(slots=True, kw_only=True)
class OpenTelemetryTracer(TracingProtocol[OpenTelemetrySpan]):
    """OpenTelemetry tracer."""

    # Base
    name: str

    # Private
    _tracer: Tracer = field(init=False)

    def __attrs_post_init__(self) -> None:
        """Initialize tracer."""
        self._tracer = trace.get_tracer(self.name)

    @contextmanager
    def trace_operation(
        self,
        name: str,
        attributes: Mapping[str, Any] | None = None,
        context: Context | None = None,
        **params: Any,
    ) -> Generator[OpenTelemetrySpan]:
        """Trace an operation using the OpenTelemetry tracer.

        Args:
            name: Name of the operation.
            attributes: Dictionary of attributes to set on the span.
            context: OpenTelemetry context to use for the span.
            **params: Additional OpenTelemetry parameters (kind, links, etc.).

        Yields:
            OpenTelemetry span object.
        """
        with self._tracer.start_as_current_span(
            name=name, attributes=attributes, context=context, **params
        ) as _span:
            yield OpenTelemetrySpan(span=_span)

    @property
    def current_span(self) -> OpenTelemetrySpan | None:
        """Get the current span.

        Returns:
            OpenTelemetrySpan or None if no span is set in the current context.
        """
        current_span = trace.get_current_span()
        if isinstance(current_span, NonRecordingSpan):
            return None
        return OpenTelemetrySpan(span=trace.get_current_span())
