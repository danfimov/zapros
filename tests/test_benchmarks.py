import pytest
from pywhatwgurl import URL

from zapros import Response
from zapros._constants import CHUNK_SIZE
from zapros._decoders import ByteChunker
from zapros._handlers._std._sync_http1 import Http1Connection
from zapros._models import Request as ZaprosRequest
from zapros._sync_pool import Http1ConnectionPool

BROWSER_HEADERS = [
    ("Host", "example.com"),
    ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Accept-Language", "en-US,en;q=0.5"),
    ("Cookie", "ID=" + "A" * 200),
    ("Connection", "keep-alive"),
    ("Referer", "https://example.com/previous/page"),
    ("Origin", "https://example.com"),
    ("X-Request-Id", "0123456789abcdef0123456789abcdef"),
]

RESPONSE_HEADERS = [
    (b"Cache-Control", b"private, max-age=0"),
    (b"Content-Type", b"text/html; charset=UTF-8"),
    (b"Date", b"Fri, 20 May 2016 09:23:41 GMT"),
    (b"Server", b"gws"),
    (b"X-Frame-Options", b"SAMEORIGIN"),
]

HEADER_COUNTS = [
    pytest.param(2, id="2headers"),
    pytest.param(5, id="5headers"),
    pytest.param(8, id="8headers"),
]

RESPONSE_BODY_SIZES = [
    pytest.param(0, id="nobody"),
    pytest.param(1024, id="1KiB"),
    pytest.param(256 * 1024, id="256KiB"),
]


class FakeStream:
    """A BaseNetworkStream that replays canned bytes and discards writes.

    read() hands back DEFAULT_READ_SIZE-ish slices so the caller goes round the
    NEED_DATA loop the way it would against a socket, without the syscalls.
    """

    def __init__(self, to_read: bytes, chunk_size: int = 64 * 1024) -> None:
        self._to_read = to_read
        self._offset = 0
        self._chunk_size = chunk_size
        self.written = 0

    def read(self, max_bytes: int, timeout: float | None = None) -> bytes:
        end = min(self._offset + min(max_bytes, self._chunk_size), len(self._to_read))
        chunk = self._to_read[self._offset : end]
        self._offset = end
        return chunk

    def write_all(self, data: bytes, timeout: float | None = None) -> int:
        self.written += len(data)
        return len(data)

    def close(self) -> None:
        pass

    def selected_alpn_protocol(self) -> None:
        return None


@pytest.fixture(scope="session", params=HEADER_COUNTS)
def request_headers(request: pytest.FixtureRequest) -> list[tuple[str, str]]:
    return BROWSER_HEADERS[: request.param]


@pytest.fixture(scope="session", params=RESPONSE_BODY_SIZES)
def response_body(request: pytest.FixtureRequest) -> bytes:
    return b"x" * request.param


@pytest.fixture(scope="session")
def raw_response_headers() -> bytes:
    lines = [b"%s: %s" % pair for pair in RESPONSE_HEADERS]
    lines.append(b"Content-Length: 0")
    return b"HTTP/1.1 200 OK\r\n" + b"\r\n".join(lines) + b"\r\n\r\n"


@pytest.fixture(scope="session")
def typical_response() -> bytes:
    """A fixed 1 KiB response, for benchmarks whose axis is not body size."""
    body = b"x" * 1024
    lines = [b"%s: %s" % pair for pair in RESPONSE_HEADERS]
    lines.append(b"Content-Length: %d" % len(body))
    return b"HTTP/1.1 200 OK\r\n" + b"\r\n".join(lines) + b"\r\n\r\n" + body


@pytest.fixture(scope="session")
def raw_response(response_body: bytes) -> bytes:
    lines = [b"%s: %s" % pair for pair in RESPONSE_HEADERS]
    lines.append(b"Content-Length: %d" % len(response_body))
    return b"HTTP/1.1 200 OK\r\n" + b"\r\n".join(lines) + b"\r\n\r\n" + response_body


@pytest.fixture(scope="session")
def body() -> bytes:
    return b"x" * (4 * 1024 * 1024)


@pytest.fixture(scope="session")
def body_chunks(body: bytes) -> list[bytes]:
    socket_sized_inbound_pease_size = 64 * 1024
    return [body[i : i + socket_sized_inbound_pease_size] for i in range(0, len(body), socket_sized_inbound_pease_size)]


@pytest.fixture(
    scope="session",
    params=[
        pytest.param(1024, id="1KiB"),
        pytest.param(CHUNK_SIZE // 2, id="8KiB"),
        pytest.param(CHUNK_SIZE, id="16KiB"),
        pytest.param(64 * 1024, id="64KiB"),
        pytest.param(1024 * 1024, id="1MiB"),
        pytest.param(4 * 1024 * 1024, id="4MiB"),
        pytest.param(8 * 1024 * 1024, id="8MiB"),
    ],
)
def single_feed_body(request: pytest.FixtureRequest, body: bytes) -> bytes:
    return body[: request.param]


@pytest.mark.benchmark
def test_bench_bytechunker_stream(body_chunks: list[bytes], body: bytes) -> None:
    chunker = ByteChunker(CHUNK_SIZE)
    total = sum(len(chunk) for piece in body_chunks for chunk in chunker.feed(piece))
    total += len(chunker.flush())
    assert total == len(body)


@pytest.mark.benchmark
def test_bench_bytechunker_single_feed(single_feed_body: bytes) -> None:
    chunker = ByteChunker(CHUNK_SIZE)
    total = sum(len(c) for c in chunker.feed(single_feed_body)) + len(chunker.flush())
    assert total == len(single_feed_body)


@pytest.mark.benchmark
def test_bench_iter_bytes_identity_e2e(body_chunks: list[bytes], body: bytes) -> None:
    response = Response(200, content=iter(body_chunks))
    assert sum(len(c) for c in response.iter_bytes()) == len(body)


class TestHttp1:
    """The HTTP/1.1 path, which is where h11 does its work.

    Driven over a fake transport rather than MockServer: real socket I/O would
    dominate the measurement and drown out the protocol handling these are meant
    to track. Nothing here references h11 directly, so the same benchmarks
    measure whichever h11 implementation zapros is wired to.
    """

    @staticmethod
    def _request(headers: list[tuple[str, str]]) -> ZaprosRequest:
        return ZaprosRequest(URL("http://example.com/path/to/thing"), "GET", dict(headers))

    @pytest.mark.benchmark
    def test_send_request_headers(self, request_headers: list[tuple[str, str]]) -> None:
        """Building and serializing the request line and headers."""
        stream = FakeStream(b"")
        conn = Http1Connection(stream, pool=Http1ConnectionPool())
        conn._send_request_headers(method="GET", target=b"/path/to/thing", headers=request_headers)
        assert stream.written

    @pytest.mark.benchmark
    def test_receive_response_headers(self, raw_response_headers: bytes) -> None:
        """Feeding bytes in and pulling the parsed status and headers out."""
        conn = Http1Connection(FakeStream(raw_response_headers), pool=Http1ConnectionPool())
        conn._send_request_headers(method="GET", target=b"/", headers=[("Host", "example.com")])
        conn._send_request_body(body=None, write_timeout=None, deadline=None)
        status, headers = conn._receive_response_headers()
        assert status == 200 and headers

    @pytest.mark.benchmark
    def test_roundtrip(self, raw_response: bytes, response_body: bytes) -> None:
        """A whole request/response cycle, body included.

        Body size is the axis here, so this tracks framing and buffer copies.
        """
        conn = Http1Connection(FakeStream(raw_response), pool=Http1ConnectionPool())
        response = conn.send_request(self._request([("Accept", "*/*")]))
        assert len(response.read()) == len(response_body)

    @pytest.mark.benchmark
    def test_roundtrip_headers(self, request_headers: list[tuple[str, str]], typical_response: bytes) -> None:
        """The same cycle with header count as the axis instead."""
        conn = Http1Connection(FakeStream(typical_response), pool=Http1ConnectionPool())
        response = conn.send_request(self._request(request_headers))
        response.read()
        assert response.status == 200

    @pytest.mark.benchmark
    def test_roundtrip_keepalive(self, typical_response: bytes) -> None:
        """Ten cycles on one connection, which is what a pooled client does.

        Amortizes connection setup away and exercises the h11 cycle reset.
        """
        stream = FakeStream(typical_response * 10)
        conn = Http1Connection(stream, pool=Http1ConnectionPool())
        for _ in range(10):
            response = conn.send_request(self._request([("Accept", "*/*")]))
            response.read()
        assert stream.written
