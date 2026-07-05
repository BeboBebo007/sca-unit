import json

import pytest

from private_server.api import (
    RequestValidationError,
    process_assessment_request,
)


def test_process_assessment_request_returns_report(tmp_path):
    first_file = tmp_path / "first.json"
    second_file = tmp_path / "second.json"
    audit_log = tmp_path / "audit.jsonl"

    first_file.write_text(
        json.dumps(
            {
                "identity": "baseline",
                "nodes": ["a", "b"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    second_file.write_text(
        json.dumps(
            {
                "identity": "observation",
                "nodes": ["a", "b", "c"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    report = process_assessment_request(
        {
            "first_file": str(first_file),
            "second_file": str(second_file),
            "audit_log": str(audit_log),
        }
    )

    assert report["request_id"]
    assert report["assessment"]["first_identity"] == "baseline"
    assert report["assessment"]["second_identity"] == "observation"
    assert report["assessment"]["verdict"] == "compatible"
    assert audit_log.exists()


def test_missing_file_field_is_rejected():
    with pytest.raises(
        RequestValidationError,
        match="Missing required fields",
    ):
        process_assessment_request(
            {
                "first_file": "first.json",
            }
        )


def test_non_object_request_is_rejected():
    with pytest.raises(
        RequestValidationError,
        match="JSON object",
    ):
        process_assessment_request(
            ["first.json", "second.json"]
        )