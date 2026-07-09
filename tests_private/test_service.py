import json

import pytest

from private_server.service import (
    InputValidationError,
    assess_structure_files,
    validate_structure_file,
)


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


def test_assess_structure_files_returns_expected_report(tmp_path):
    first_file = tmp_path / "first.json"
    second_file = tmp_path / "second.json"

    first_file.write_text(
        json.dumps(
            {
                "identity": "first",
                "nodes": ["a", "b"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    second_file.write_text(
        json.dumps(
            {
                "identity": "second",
                "nodes": ["a", "b", "c"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    report = assess_structure_files(first_file, second_file)

    assert report["schema_version"] == "1.0"
    assert report["engine"]["scope"] == "non-proprietary prototype"
    assert report["assessment"]["first_identity"] == "first"
    assert report["assessment"]["second_identity"] == "second"
    assert report["assessment"]["verdict"] == "compatible"

def test_assessment_writes_audit_record(tmp_path):
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

    assess_structure_files(
        first_file,
        second_file,
        audit_log_path=audit_log,
    )

    saved = json.loads(
        audit_log.read_text(encoding="utf-8").strip()
    )

    assert saved["first_identity"] == "baseline"
    assert saved["second_identity"] == "observation"
    assert saved["status"] == "completed"
    assert "nodes" not in saved
    assert "edges" not in saved

def test_report_and_audit_share_request_id(tmp_path):
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
                "nodes": ["a", "b"],
                "edges": [["a", "b"]],
            }
        ),
        encoding="utf-8",
    )

    report = assess_structure_files(
        first_file,
        second_file,
        audit_log_path=audit_log,
    )

    saved = json.loads(
        audit_log.read_text(encoding="utf-8").strip()
    )

    assert report["request_id"]
    assert report["request_id"] == saved["request_id"]

def test_assess_structure_payloads_returns_report(tmp_path):
    from private_server.service import (
        assess_structure_payloads,
    )

    audit_log = tmp_path / "payload_audit.jsonl"

    report = assess_structure_payloads(
        {
            "identity": "payload-baseline",
            "nodes": ["a", "b"],
            "edges": [["a", "b"]],
        },
        {
            "identity": "payload-observation",
            "nodes": ["a", "b", "c"],
            "edges": [["a", "b"]],
        },
        audit_log_path=audit_log,
    )

    assert report["request_id"]
    assert report["assessment"]["first_identity"] == (
        "payload-baseline"
    )
    assert report["assessment"]["second_identity"] == (
        "payload-observation"
    )
    assert report["assessment"]["verdict"] == "compatible"
    assert audit_log.exists()

def test_assessment_report_includes_drift_details(tmp_path):
    from private_server.service import assess_structure_payloads

    report = assess_structure_payloads(
        {
            "identity": "baseline",
            "nodes": ["a", "b", "c"],
            "edges": [["a", "b"], ["b", "c"]],
        },
        {
            "identity": "current",
            "nodes": ["b", "c", "d"],
            "edges": [["b", "c"], ["c", "d"]],
        },
        audit_log_path=tmp_path / "audit.jsonl",
    )

    assert report["drift"] == {
        "added_nodes": ["d"],
        "removed_nodes": ["a"],
        "added_edges": [["c", "d"]],
        "removed_edges": [["a", "b"]],
        "severity": "medium",
        "verdict": "review_required",
        "human_summary": "Multiple structural changes detected; review required.",
        "total_changes": 4,
        "summary": {
            "added_node_count": 1,
            "removed_node_count": 1,
            "added_edge_count": 1,
            "removed_edge_count": 1,
        },
    }


def test_identical_structures_report_no_drift(tmp_path):
    from private_server.service import assess_structure_payloads

    structure = {
        "identity": "stable",
        "nodes": ["a", "b"],
        "edges": [["a", "b"]],
    }

    report = assess_structure_payloads(
        structure,
        structure,
        audit_log_path=tmp_path / "audit.jsonl",
    )

    assert report["drift"]["severity"] == "low"
    assert report["drift"]["verdict"] == "no_drift"
    assert report["drift"]["human_summary"] == "No structural drift detected."
    assert report["drift"]["total_changes"] == 0
