from enum import StrEnum


class SystemTelemetryFields(StrEnum):
    """System resource telemetry fields."""

    # CPU metrics
    CPU_USAGE_PERCENT = "system.cpu.usage_percent"
    CPU_USAGE_USER = "system.cpu.usage_user"
    CPU_USAGE_SYSTEM = "system.cpu.usage_system"
    CPU_USAGE_IDLE = "system.cpu.usage_idle"
    CPU_CORES_LOGICAL = "system.cpu.cores_logical"
    CPU_CORES_PHYSICAL = "system.cpu.cores_physical"
    CPU_FREQUENCY_MHZ = "system.cpu.frequency_mhz"

    # Memory metrics
    MEMORY_USAGE_BYTES = "system.memory.usage_bytes"
    MEMORY_AVAILABLE_BYTES = "system.memory.available_bytes"
    MEMORY_TOTAL_BYTES = "system.memory.total_bytes"
    MEMORY_USAGE_PERCENT = "system.memory.usage_percent"
    MEMORY_SWAP_USED_BYTES = "system.memory.swap_used_bytes"
    MEMORY_SWAP_TOTAL_BYTES = "system.memory.swap_total_bytes"

    # Disk metrics
    DISK_USAGE_BYTES = "system.disk.usage_bytes"
    DISK_AVAILABLE_BYTES = "system.disk.available_bytes"
    DISK_TOTAL_BYTES = "system.disk.total_bytes"
    DISK_USAGE_PERCENT = "system.disk.usage_percent"
    DISK_READ_BYTES = "system.disk.read_bytes"
    DISK_WRITE_BYTES = "system.disk.write_bytes"
    DISK_READ_OPS = "system.disk.read_ops"
    DISK_WRITE_OPS = "system.disk.write_ops"

    # Process metrics
    PROCESS_PID = "system.process.pid"
    PROCESS_CPU_USAGE_PERCENT = "system.process.cpu_usage_percent"
    PROCESS_MEMORY_RSS_BYTES = "system.process.memory_rss_bytes"
    PROCESS_MEMORY_VMS_BYTES = "system.process.memory_vms_bytes"
    PROCESS_THREADS_COUNT = "system.process.threads_count"
    PROCESS_FILE_DESCRIPTORS_COUNT = "system.process.file_descriptors_count"

    # System info
    SYSTEM_OS_NAME = "system.os.name"
    SYSTEM_OS_VERSION = "system.os.version"
    SYSTEM_HOSTNAME = "system.hostname"
    SYSTEM_UPTIME_SECONDS = "system.uptime_seconds"
    SYSTEM_BOOT_TIME = "system.boot_time"


class SystemEventTypes(StrEnum):
    """System event type values."""

    CPU_HIGH_USAGE = "cpu_high_usage"
    MEMORY_HIGH_USAGE = "memory_high_usage"
    DISK_HIGH_USAGE = "disk_high_usage"
    DISK_LOW_SPACE = "disk_low_space"
    PROCESS_START = "process_start"
    PROCESS_EXIT = "process_exit"
    SYSTEM_BOOT = "system_boot"
    SYSTEM_SHUTDOWN = "system_shutdown"
