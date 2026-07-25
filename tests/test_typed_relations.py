from sca_unit.typed_relations import (
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
)


def conflict_types(conflicts):
    return [conflict["conflict_type"] for conflict in conflicts]


def test_relation_type_changed():
    first = [{"source": "api", "target": "database", "type": "depends_on", "required": True}]
    second = [{"source": "api", "target": "database", "type": "writes_to", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert conflict_types(conflicts) == ["relation_type_changed"]


def test_relation_direction_reversed():
    first = [{"source": "api", "target": "database", "type": "depends_on", "required": True}]
    second = [{"source": "database", "target": "api", "type": "depends_on", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert conflict_types(conflicts) == ["relation_direction_reversed"]


def test_required_relation_removed():
    first = [{"source": "auth", "target": "user_store", "type": "requires", "required": True}]
    second = []

    conflicts = detect_typed_relation_conflicts(first, second)

    assert conflict_types(conflicts) == ["required_relation_removed"]


def test_required_status_changed():
    first = [{"source": "payment", "target": "ledger", "type": "writes_to", "required": True}]
    second = [{"source": "payment", "target": "ledger", "type": "writes_to", "required": False}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert conflict_types(conflicts) == ["required_status_changed"]


def test_no_conflict_same_relation():
    first = [{"source": "frontend", "target": "api", "type": "calls", "required": True}]
    second = [{"source": "frontend", "target": "api", "type": "calls", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert conflicts == []
    assert count_typed_relation_conflicts(first, second) == 0
