import os

import pendulum
from pendulum import DateTime, Timezone

# ----------
# Set defaults
# ----------


def _get_default_timezone() -> Timezone:
    """Get default timezone from environment variable.

    Falls back to UTC if the TIMEZONE environment variable is not set or invalid.

    Returns:
        Default timezone instance, UTC if environment variable is invalid.
    """
    timezone_str = os.getenv("TIMEZONE", "UTC")
    try:
        return Timezone(timezone_str)
    except ValueError:
        # Fallback to UTC if the provided timezone is invalid
        return Timezone("UTC")


# Default timezone for the application
DEFAULT_TIMEZONE: Timezone = _get_default_timezone()

# A constant representing a far-future datetime, useful for placeholders.
MAX_TIME: DateTime = pendulum.datetime(9999, 12, 31).naive()


# ----------
# Functions
# ----------


def current_time() -> DateTime:
    """Get the current time, localized to the default timezone."""
    return pendulum.now(tz=DEFAULT_TIMEZONE)


def current_time_isoformat() -> str:
    """Return the current time as an ISO 8601 formatted string.

    Returns:
        Current time in ISO 8601 format.
    """
    return current_time().isoformat()


def current_time_naive() -> DateTime:
    """Get the current time as a DateTime object (without timezone information).

    Returns:
        Current time as DateTime object without timezone information.
    """
    return current_time().naive()


def timestamp_to_isoformat(
    timestamp: float, timezone: Timezone = DEFAULT_TIMEZONE
) -> str:
    """Convert a Unix timestamp to ISO 8601 formatted string.

    Args:
        timestamp: Unix timestamp (seconds since epoch)
        timezone: Timezone to use for the timestamp

    Returns:
        ISO 8601 formatted timestamp string with given timezone.
    """
    return pendulum.from_timestamp(timestamp, tz=timezone).isoformat()


def timestamp_to_datetime(
    timestamp: float, timezone: Timezone = DEFAULT_TIMEZONE
) -> DateTime:
    """Convert a Unix timestamp to DateTime object."""
    return pendulum.from_timestamp(timestamp, tz=timezone)
