import json

import pytest

from private_server.api import (
    parse_content_length,
    is_json_content_type,
    api_keys_match,
    RequestValidationError,
    process_assessment_request,
    process_json_assessment_request,
)


def test_process_payload_request_returns_report(tmp_path):
    audit_log = tmp_path / "audit.jsonl"

    report = process_assessment_request(
        {
            "first_structure": {
                "identity": "baseline",
                "nodes": ["a", "b"],
                "edges": [["a", "b"]],
            },
            "second_structure": {
                "identity": "observation",
                "nodes": ["a", "b", "c"],
                "edges": [["a", "b"]],
            },
            "audit_log": str(audit_log),
        }
    )

    assert report["request_id"]
    assert report["assessment"]["first_identity"] == "baseline"
    assert report["assessment"]["second_identity"] == "observation"
    assert report["assessment"]["verdict"] == "compatible"
    assert audit_log.exists()

    saved = json.loads(
        audit_log.read_text(encoding="utf-8").strip()
    )

    assert saved["request_id"] == report["request_id"]


def test_missing_structure_field_is_rejected():
    with pytest.raises(
        RequestValidationError,
        match="Missing required fields",
    ):
        process_assessment_request(
            {
                "first_structure": {
                    "identity": "first",
                    "nodes": [],
                    "edges": [],
                }
            }
        )


def test_non_object_request_is_rejected():
    with pytest.raises(
        RequestValidationError,
        match="JSON object",
    ):
        process_assessment_request(
            ["first", "second"]
        )


def test_file_path_request_is_rejected():
    with pytest.raises(
        RequestValidationError,
        match="Missing required fields",
    ):
        process_assessment_request(
            {
                "first_file": "first.json",
                "second_file": "second.json",
            }
        )

def test_api_keys_match_accepts_identical_keys():
    assert api_keys_match(
        "test-secret-key",
        "test-secret-key",
    )


def test_api_keys_match_rejects_invalid_or_empty_keys():
    assert not api_keys_match(
        "test-secret-key",
        "wrong-secret-key",
    )
    assert not api_keys_match(
        "test-secret-key",
        "",
    )


def test_json_content_type_accepts_valid_values():
    assert is_json_content_type("application/json")
    assert is_json_content_type(
        "Application/JSON; charset=utf-8"
    )


def test_json_content_type_rejects_impostors():
    assert not is_json_content_type("text/application/json")
    assert not is_json_content_type("application/jsonevil")
    assert not is_json_content_type("")


def test_parse_content_length_accepts_digits():
    assert parse_content_length("1234") == 1234


def test_parse_content_length_rejects_ambiguous_values():
    for value in ("", "+10", " 10", "10 ", "1.0", "abc"):
        with pytest.raises(
            RequestValidationError,
            match="Invalid Content-Length",
        ):
            parse_content_length(value)


def test_process_json_assessment_request(tmp_path):
    report = process_json_assessment_request(
        {
            "first_document": {
                "user": {
                    "name": "Ada",
                }
            },
            "second_document": {
                "user": {
                    "name": "Ada",
                    "roles": ["admin"],
                }
            },
            "first_identity": "profile-v1",
            "second_identity": "profile-v2",
            "audit_log": str(tmp_path / "audit.jsonl"),
        }
    )

    assert report["assessment"]["first_identity"] == "profile-v1"
    assert report["assessment"]["second_identity"] == "profile-v2"
    assert report["drift"]["added_nodes"] == [
        "$.user.roles",
        "$.user.roles[0]",
    ]
    assert report["drift"]["total_changes"] == 4
    assert report["drift"]["verdict"] == "review_required"
