import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from private_server.service import (
    InputValidationError,
    assess_structure_files,
)


class RequestValidationError(ValueError):
    """Raised when an API request is invalid."""


def process_assessment_request(
    payload: Any,
) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise RequestValidationError(
            "The request body must be a JSON object"
        )

    required_fields = {"first_file", "second_file"}
    missing_fields = sorted(required_fields - payload.keys())

    if missing_fields:
        raise RequestValidationError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    first_file = payload["first_file"]
    second_file = payload["second_file"]

    if not isinstance(first_file, str) or not first_file.strip():
        raise RequestValidationError(
            "first_file must be a non-empty string"
        )

    if not isinstance(second_file, str) or not second_file.strip():
        raise RequestValidationError(
            "second_file must be a non-empty string"
        )

    audit_log = payload.get(
        "audit_log",
        "evidence/private_server_audit.jsonl",
    )

    if not isinstance(audit_log, str) or not audit_log.strip():
        raise RequestValidationError(
            "audit_log must be a non-empty string"
        )

    return assess_structure_files(
        first_file=first_file,
        second_file=second_file,
        audit_log_path=audit_log,
    )


class SCARequestHandler(BaseHTTPRequestHandler):
    server_version = "SCAUnitLocalService/0.1"

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
                    "version": "0.1",
                },
            )
            return

        self._send_json(
            404,
            {"error": "Endpoint not found"},
        )

    def do_POST(self) -> None:
        if self.path != "/assess":
            self._send_json(
                404,
                {"error": "Endpoint not found"},
            )
            return

        expected_api_key = os.environ.get("SCA_UNIT_API_KEY", "")
        provided_api_key = self.headers.get("X-API-Key", "")

        if not expected_api_key:
            self._send_json(
                503,
                {"error": "Service API key is not configured"},
            )
            return

        if provided_api_key != expected_api_key:
            self._send_json(
                401,
                {"error": "Unauthorized"},
            )
            return

        content_type = self.headers.get(
            "Content-Type",
            "",
        )

        if "application/json" not in content_type:
            self._send_json(
                415,
                {"error": "Content-Type must be application/json"},
            )
            return

        try:
            content_length = int(
                self.headers.get("Content-Length", "0")
            )
        except ValueError:
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
            report = process_assessment_request(payload)
        except UnicodeDecodeError:
            self._send_json(
                400,
                {"error": "Request body must use UTF-8"},
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


def run_local_service(
    host: str = "127.0.0.1",
    port: int = 8765,
) -> None:
    server = ThreadingHTTPServer(
        (host, port),
        SCARequestHandler,
    )

    print(
        f"SCA-Unit local service running at "
        f"http://{host}:{port}"
    )
    print("Health endpoint: /health")
    print("Assessment endpoint: /assess")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping local service...")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_local_service()