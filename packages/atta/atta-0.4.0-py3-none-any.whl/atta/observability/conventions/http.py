from enum import StrEnum


class HTTPTelemetryFields(StrEnum):
    """HTTP request/response telemetry fields."""

    # Request info
    HTTP_REQUEST_METHOD = "http.request.method"
    HTTP_REQUEST_URL = "http.request.url"
    HTTP_REQUEST_PATH = "http.request.path"
    HTTP_REQUEST_QUERY = "http.request.query"
    HTTP_REQUEST_SCHEME = "http.request.scheme"  # http, https
    HTTP_REQUEST_SIZE_BYTES = "http.request.size_bytes"
    HTTP_REQUEST_BODY_SIZE_BYTES = "http.request.body_size_bytes"

    # Request headers
    HTTP_REQUEST_HEADER_CONTENT_TYPE = "http.request.header.content_type"
    HTTP_REQUEST_HEADER_CONTENT_LENGTH = "http.request.header.content_length"
    HTTP_REQUEST_HEADER_AUTHORIZATION = "http.request.header.authorization"
    HTTP_REQUEST_HEADER_USER_AGENT = "http.request.header.user_agent"
    HTTP_REQUEST_HEADER_ACCEPT = "http.request.header.accept"
    HTTP_REQUEST_HEADER_ACCEPT_ENCODING = "http.request.header.accept_encoding"
    HTTP_REQUEST_HEADER_CACHE_CONTROL = "http.request.header.cache_control"

    # Response info
    HTTP_RESPONSE_STATUS_CODE = "http.response.status_code"
    HTTP_RESPONSE_STATUS_TEXT = "http.response.status_text"
    HTTP_RESPONSE_SIZE_BYTES = "http.response.size_bytes"
    HTTP_RESPONSE_BODY_SIZE_BYTES = "http.response.body_size_bytes"

    # Response headers
    HTTP_RESPONSE_HEADER_CONTENT_TYPE = "http.response.header.content_type"
    HTTP_RESPONSE_HEADER_CONTENT_LENGTH = "http.response.header.content_length"
    HTTP_RESPONSE_HEADER_CACHE_CONTROL = "http.response.header.cache_control"
    HTTP_RESPONSE_HEADER_SET_COOKIE = "http.response.header.set_cookie"

    # Timing metrics
    HTTP_REQUEST_DURATION_MS = "http.request.duration_ms"
    HTTP_REQUEST_TIME_TO_FIRST_BYTE_MS = "http.request.time_to_first_byte_ms"
    HTTP_REQUEST_DNS_TIME_MS = "http.request.dns_time_ms"
    HTTP_REQUEST_CONNECT_TIME_MS = "http.request.connect_time_ms"
    HTTP_REQUEST_SSL_TIME_MS = "http.request.ssl_time_ms"
    HTTP_REQUEST_SEND_TIME_MS = "http.request.send_time_ms"
    HTTP_REQUEST_WAIT_TIME_MS = "http.request.wait_time_ms"
    HTTP_REQUEST_RECEIVE_TIME_MS = "http.request.receive_time_ms"

    # Client info
    HTTP_CLIENT_IP = "http.client.ip"
    HTTP_CLIENT_PORT = "http.client.port"
    HTTP_CLIENT_NAME = "http.client.name"
    HTTP_CLIENT_VERSION = "http.client.version"

    # Server info
    HTTP_SERVER_NAME = "http.server.name"
    HTTP_SERVER_PORT = "http.server.port"
    HTTP_SERVER_ADDRESS = "http.server.address"

    # Route info
    HTTP_ROUTE = "http.route"  # /users/{id}
    HTTP_ROUTE_TEMPLATE = "http.route.template"
    HTTP_ROUTE_PARAMETERS = "http.route.parameters"

    # Error info
    HTTP_ERROR_TYPE = "http.error.type"
    HTTP_ERROR_MESSAGE = "http.error.message"
    HTTP_RETRY_COUNT = "http.retry_count"

    # Cache info
    HTTP_CACHE_HIT = "http.cache.hit"  # true, false
    HTTP_CACHE_KEY = "http.cache.key"
    HTTP_CACHE_TTL_SECONDS = "http.cache.ttl_seconds"


class HTTPMethods(StrEnum):
    """HTTP method values."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    CONNECT = "CONNECT"


class HTTPSchemes(StrEnum):
    """HTTP scheme values."""

    HTTP = "http"
    HTTPS = "https"


class HTTPStatusClasses(StrEnum):
    """HTTP status code classes."""

    INFORMATIONAL = "1xx"  # 100-199
    SUCCESSFUL = "2xx"  # 200-299
    REDIRECTION = "3xx"  # 300-399
    CLIENT_ERROR = "4xx"  # 400-499
    SERVER_ERROR = "5xx"  # 500-599


class HTTPContentTypes(StrEnum):
    """Common HTTP content type values."""

    JSON = "application/json"
    XML = "application/xml"
    HTML = "text/html"
    PLAIN_TEXT = "text/plain"
    FORM_URLENCODED = "application/x-www-form-urlencoded"
    MULTIPART_FORM = "multipart/form-data"
    BINARY = "application/octet-stream"
    PDF = "application/pdf"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
