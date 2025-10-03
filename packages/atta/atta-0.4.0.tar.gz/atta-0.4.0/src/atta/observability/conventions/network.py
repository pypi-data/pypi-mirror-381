from enum import StrEnum


class NetworkTelemetryFields(StrEnum):
    """Network telemetry fields."""

    # Connection info
    NET_PEER_HOST = "net.peer.host"
    NET_PEER_PORT = "net.peer.port"
    NET_PEER_IP = "net.peer.ip"
    NET_HOST_HOST = "net.host.host"
    NET_HOST_PORT = "net.host.port"
    NET_HOST_IP = "net.host.ip"

    # Protocol info
    NET_TRANSPORT = "net.transport"  # tcp, udp, pipe, unix
    NET_PROTOCOL_NAME = "net.protocol.name"  # http, https, grpc, amqp
    NET_PROTOCOL_VERSION = "net.protocol.version"  # 1.1, 2.0, 3.0

    # Connection metrics
    NET_CONNECTION_STATE = "net.connection.state"  # established, listening, closed
    NET_CONNECTION_TYPE = "net.connection.type"  # client, server
    NET_CONNECTION_POOL_SIZE = "net.connection.pool_size"
    NET_CONNECTION_POOL_ACTIVE = "net.connection.pool_active"
    NET_CONNECTION_POOL_IDLE = "net.connection.pool_idle"

    # Traffic metrics
    NET_BYTES_SENT = "net.bytes_sent"
    NET_BYTES_RECEIVED = "net.bytes_received"
    NET_PACKETS_SENT = "net.packets_sent"
    NET_PACKETS_RECEIVED = "net.packets_received"
    NET_PACKETS_DROPPED = "net.packets_dropped"
    NET_ERRORS_COUNT = "net.errors_count"

    # Timing metrics
    NET_CONNECT_TIME_MS = "net.connect_time_ms"
    NET_DNS_LOOKUP_TIME_MS = "net.dns_lookup_time_ms"
    NET_SSL_HANDSHAKE_TIME_MS = "net.ssl_handshake_time_ms"
    NET_ROUND_TRIP_TIME_MS = "net.round_trip_time_ms"

    # Interface metrics
    NET_INTERFACE_NAME = "net.interface.name"
    NET_INTERFACE_STATE = "net.interface.state"  # up, down
    NET_INTERFACE_SPEED_MBPS = "net.interface.speed_mbps"


class NetworkTransportTypes(StrEnum):
    """Network transport protocol values."""

    TCP = "tcp"
    UDP = "udp"
    PIPE = "pipe"
    UNIX = "unix"
    QUIC = "quic"


class NetworkConnectionStates(StrEnum):
    """Network connection state values."""

    ESTABLISHED = "established"
    LISTENING = "listening"
    CLOSED = "closed"
    CONNECTING = "connecting"
    CLOSING = "closing"
    TIME_WAIT = "time_wait"


class NetworkConnectionTypes(StrEnum):
    """Network connection type values."""

    CLIENT = "client"
    SERVER = "server"


class NetworkInterfaceStates(StrEnum):
    """Network interface state values."""

    UP = "up"
    DOWN = "down"
    UNKNOWN = "unknown"
