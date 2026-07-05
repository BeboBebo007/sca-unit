import json

import pytest

from private_server.service import InputValidationError, validate_structure_file


def test_valid_structure_file(tmp_path):
    file_path = tmp_path / "structure.json"
    file_path.write_text(
        json.dumps(
            {
                "identity": "test-structure",
                "nodes": ["a", "b"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    result = validate_structure_file(file_path)

    assert result["identity"] == "test-structure"
    assert result["nodes"] == ["a", "b"]


def test_missing_required_field_is_rejected(tmp_path):
    file_path = tmp_path / "structure.json"
    file_path.write_text(
        json.dumps(
            {
                "identity": "incomplete-structure",
                "nodes": [],
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(InputValidationError, match="Missing required fields"):
        validate_structure_file(file_path)


def test_invalid_json_is_rejected(tmp_path):
    file_path = tmp_path / "structure.json"
    file_path.write_text("{invalid", encoding="utf-8")

    with pytest.raises(InputValidationError, match="Invalid JSON"):
        validate_structure_file(file_path)


def test_non_json_file_is_rejected(tmp_path):
    file_path = tmp_path / "structure.txt"
    file_path.write_text("text", encoding="utf-8")

    with pytest.raises(InputValidationError, match="Only JSON"):
        validate_structure_file(file_path)