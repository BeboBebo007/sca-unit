import json
from pathlib import Path
from typing import Any

from sca_unit.assessment import assess_structures
from sca_unit.models import StructuralState


class InputValidationError(ValueError):
    """Raised when an invalid input file is rejected."""


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


def load_structural_state(file_path: str | Path) -> StructuralState:
    content = validate_structure_file(file_path)

    try:
        return StructuralState.create(
            identity=content["identity"],
            nodes=content["nodes"],
            edges=content["edges"],
        )
    except (TypeError, ValueError) as exc:
        raise InputValidationError(f"Invalid structural data: {exc}") from exc


def assess_structure_files(
    first_file: str | Path,
    second_file: str | Path,
) -> dict[str, Any]:
    first = load_structural_state(first_file)
    second = load_structural_state(second_file)

    assessment = assess_structures(first, second)

    return {
        "schema_version": "1.0",
        "engine": {
            "name": "SCA-Unit Public Structural Assessment",
            "scope": "non-proprietary prototype",
            "version": "0.2.0",
        },
        "assessment": assessment.as_dict(),
    }