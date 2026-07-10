import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from private_server.service import (
    InputValidationError,
    assess_json_payloads,
    assess_structure_payloads,
)


class RequestValidationError(ValueError):
    """Raised when an API request is invalid."""


def api_keys_match(
    expected_api_key: str,
    provided_api_key: str,
) -> bool:
    if not expected_api_key or not provided_api_key:
        return False

    return hmac.compare_digest(
        expected_api_key,
        provided_api_key,
    )


def is_json_content_type(content_type: str) -> bool:
    media_type = content_type.split(";", 1)[0].strip().lower()
    return media_type == "application/json"


def parse_content_length(value: str) -> int:
    if not value or not value.isascii() or not value.isdigit():
        raise RequestValidationError("Invalid Content-Length")

    return int(value)


def process_assessment_request(
    payload: Any,
) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise RequestValidationError(
            "The request body must be a JSON object"
        )

    required_fields = {
        "first_structure",
        "second_structure",
    }
    missing_fields = sorted(
        required_fields - payload.keys()
    )

    if missing_fields:
        raise RequestValidationError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    first_structure = payload["first_structure"]
    second_structure = payload["second_structure"]

    if not isinstance(first_structure, dict):
        raise RequestValidationError(
            "first_structure must be a JSON object"
        )

    if not isinstance(second_structure, dict):
        raise RequestValidationError(
            "second_structure must be a JSON object"
        )

    audit_log = payload.get(
        "audit_log",
        "evidence/private_server_audit.jsonl",
    )

    if not isinstance(audit_log, str) or not audit_log.strip():
        raise RequestValidationError(
            "audit_log must be a non-empty string"
        )

    return assess_structure_payloads(
        first_structure=first_structure,
        second_structure=second_structure,
        audit_log_path=audit_log,
    )



def process_json_assessment_request(
    payload: Any,
) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise RequestValidationError(
            "The request body must be a JSON object"
        )

    required_fields = {
        "first_document",
        "second_document",
    }
    missing_fields = sorted(
        required_fields - payload.keys()
    )

    if missing_fields:
        raise RequestValidationError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    audit_log = payload.get(
        "audit_log",
        "evidence/private_server_audit.jsonl",
    )

    if not isinstance(audit_log, str) or not audit_log.strip():
        raise RequestValidationError(
            "audit_log must be a non-empty string"
        )

    return assess_json_payloads(
        first_document=payload["first_document"],
        second_document=payload["second_document"],
        first_identity=payload.get(
            "first_identity",
            "baseline-json",
        ),
        second_identity=payload.get(
            "second_identity",
            "current-json",
        ),
        audit_log_path=audit_log,
    )


class SCARequestHandler(BaseHTTPRequestHandler):
    server_version = "SCAUnitLocalService/0.2"

    def _send_json(
        self,
        status_code: int,
        payload: dict[str, Any],
    ) -> None:
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
        ).encode("utf-8")

        self.send_response(status_code)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8",
        )
        self.send_header(
            "Content-Length",
            str(len(encoded)),
        )
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.close_connection = True
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json(
                200,
                {
                    "status": "ok",
                    "service": "SCA-Unit Local Private Service",
                    "scope": "non-proprietary prototype",
                    "version": "0.2",
                    "input_mode": "direct-structural-payload",
                },
            )
            return

        self._send_json(
            404,
            {"error": "Endpoint not found"},
        )

    def do_POST(self) -> None:
        if self.path not in {"/assess", "/assess-json"}:
            self._send_json(
                404,
                {"error": "Endpoint not found"},
            )
            return

        expected_api_key = os.environ.get(
            "SCA_UNIT_API_KEY",
            "",
        )
        provided_api_key = self.headers.get(
            "X-API-Key",
            "",
        )

        if not expected_api_key:
            self._send_json(
                503,
                {
                    "error": (
                        "Service API key is not configured"
                    )
                },
            )
            return

        if not api_keys_match(expected_api_key, provided_api_key):
            self._send_json(
                401,
                {"error": "Unauthorized"},
            )
            return

        content_type = self.headers.get(
            "Content-Type",
            "",
        )

        if not is_json_content_type(content_type):
            self._send_json(
                415,
                {
                    "error": (
                        "Content-Type must be application/json"
                    )
                },
            )
            return

        try:
            content_length = parse_content_length(
                self.headers.get(
                    "Content-Length",
                    "",
                )
            )
        except RequestValidationError:
            self._send_json(
                400,
                {"error": "Invalid Content-Length"},
            )
            return

        if content_length <= 0:
            self._send_json(
                400,
                {"error": "Request body is required"},
            )
            return

        if content_length > 1_000_000:
            self._send_json(
                413,
                {"error": "Request body is too large"},
            )
            return

        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(
                raw_body.decode("utf-8")
            )
            if self.path == "/assess-json":
                report = process_json_assessment_request(
                    payload
                )
            else:
                report = process_assessment_request(
                    payload
                )
        except UnicodeDecodeError:
            self._send_json(
                400,
                {
                    "error": (
                        "Request body must use UTF-8"
                    )
                },
            )
            return
        except json.JSONDecodeError:
            self._send_json(
                400,
                {"error": "Invalid JSON request body"},
            )
            return
        except (
            RequestValidationError,
            InputValidationError,
        ) as exc:
            self._send_json(
                400,
                {"error": str(exc)},
            )
            return
        except Exception:
            self._send_json(
                500,
                {"error": "Internal service error"},
            )
            return

        self._send_json(200, report)

    def log_message(
        self,
        format: str,
        *args: Any,
    ) -> None:
        return


class HardenedThreadingHTTPServer(ThreadingHTTPServer):
    request_timeout_seconds = 5

    def get_request(self):
        request, client_address = super().get_request()
        request.settimeout(self.request_timeout_seconds)
        return request, client_address


def run_local_service(
    host: str = "127.0.0.1",
    port: int = 8765,
) -> None:
    server = HardenedThreadingHTTPServer(
        (host, port),
        SCARequestHandler,
    )

    print(
        f"SCA-Unit local service running at "
        f"http://{host}:{port}"
    )
    print("Health endpoint: /health")
    print("Assessment endpoint: /assess")
    print("Input mode: direct structural payload")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping local service...")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_local_service()