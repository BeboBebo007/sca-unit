from sca_unit import (
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
)


def test_typed_relation_functions_are_publicly_exported():
    first = [{"source": "api", "target": "database", "type": "depends_on", "required": True}]
    second = [{"source": "api", "target": "database", "type": "writes_to", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert count_typed_relation_conflicts(first, second) == 1
    assert conflicts[0]["conflict_type"] == "relation_type_changed"
