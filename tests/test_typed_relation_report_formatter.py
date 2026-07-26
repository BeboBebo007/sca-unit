from sca_unit import (
    detect_typed_relation_conflicts,
    format_typed_relation_report_section,
)


def test_format_typed_relation_report_section_with_conflict():
    first = [{"source": "api", "target": "database", "type": "depends_on", "required": True}]
    second = [{"source": "api", "target": "database", "type": "writes_to", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)
    report = format_typed_relation_report_section(conflicts)

    assert "Typed Relation Findings" in report
    assert "Total typed relation conflicts: 1" in report
    assert "Finding 1" in report
    assert "Conflict type: relation_type_changed" in report
    assert "Source: api" in report
    assert "Target: database" in report
    assert "Explanation:" in report
    assert "Interpretation:" in report


def test_format_typed_relation_report_section_empty_result():
    report = format_typed_relation_report_section([])

    assert "Typed Relation Findings" in report
    assert "No typed relation conflicts were detected." in report


def test_format_typed_relation_report_section_with_validation_warning():
    report = format_typed_relation_report_section([], validation_errors=["missing field: source"])

    assert "Validation warning:" in report
    assert "- missing field: source" in report
