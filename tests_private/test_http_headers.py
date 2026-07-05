import threading
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

from private_server.api import HardenedThreadingHTTPServer, SCARequestHandler


def test_health_response_includes_security_headers():
    server = ThreadingHTTPServer(("127.0.0.1", 0), SCARequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    connection = HTTPConnection("127.0.0.1", server.server_port, timeout=2)

    try:
        connection.request("GET", "/health")
        response = connection.getresponse()
        response.read()

        assert response.status == 200
        assert response.getheader("X-Content-Type-Options") == "nosniff"
        assert response.getheader("Cache-Control") == "no-store"
        assert response.getheader("Connection") == "close"
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def test_server_applies_connection_timeout(monkeypatch):
    class DummySocket:
        timeout = None

        def settimeout(self, value):
            self.timeout = value

    dummy_socket = DummySocket()

    monkeypatch.setattr(
        ThreadingHTTPServer,
        "get_request",
        lambda self: (
            dummy_socket,
            ("127.0.0.1", 12345),
        ),
    )

    server = object.__new__(
        HardenedThreadingHTTPServer
    )
    request, address = server.get_request()

    assert request is dummy_socket
    assert address == ("127.0.0.1", 12345)
    assert dummy_socket.timeout == 5
