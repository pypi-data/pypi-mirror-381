from attrs import define


@define(slots=True, frozen=True)
class TraceIds:
    """Holds trace and span identifiers.

    Args:
        trace_id: Trace identifier (128-bit)
        span_id: Span identifier (64-bit)
    """

    trace_id: int
    span_id: int

    def to_hex_dict(self) -> dict[str, str]:
        """Convert to hexadecimal strings.

        Returns:
            Dictionary with hex-encoded IDs
        """
        return {
            "trace_id": f"{self.trace_id:032x}",
            "span_id": f"{self.span_id:016x}",
        }
