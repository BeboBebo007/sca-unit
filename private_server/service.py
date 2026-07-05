import json
from pathlib import Path
from typing import Any


class InputValidationError(ValueError):
    """يُرفع عند رفض ملف إدخال غير صالح."""


def validate_structure_file(file_path: str | Path) -> dict[str, Any]:
    path = Path(file_path)

    if not path.exists():
        raise InputValidationError(f"File does not exist: {path}")

    if not path.is_file():
        raise InputValidationError(f"Path is not a file: {path}")

    if path.suffix.lower() != ".json":
        raise InputValidationError("Only JSON files are accepted")

    try:
        content = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise InputValidationError("Invalid JSON content") from exc

    if not isinstance(content, dict):
        raise InputValidationError("The JSON root must be an object")

    required_fields = {"identity", "nodes", "edges"}
    missing_fields = sorted(required_fields - content.keys())

    if missing_fields:
        raise InputValidationError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    if not isinstance(content["identity"], str) or not content["identity"].strip():
        raise InputValidationError("The identity field must be a non-empty string")

    if not isinstance(content["nodes"], list):
        raise InputValidationError("The nodes field must be a list")

    if not isinstance(content["edges"], list):
        raise InputValidationError("The edges field must be a list")

    return content