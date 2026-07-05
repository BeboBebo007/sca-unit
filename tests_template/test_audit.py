import json

from reusable_service.audit import append_audit_record, create_audit_record


def test_audit_record_is_written_without_structural_content(tmp_path):
    log_path = tmp_path / "audit.jsonl"

    record = create_audit_record(
        first_identity="baseline",
        second_identity="observation",
        status="completed",
    )

    append_audit_record(record, log_path)

    saved = json.loads(log_path.read_text(encoding="utf-8").strip())

    assert saved["request_id"]
    assert saved["timestamp_utc"]
    assert saved["first_identity"] == "baseline"
    assert saved["second_identity"] == "observation"
    assert saved["status"] == "completed"
    assert "nodes" not in saved
    assert "edges" not in saved
    assert "assessment" not in saved

