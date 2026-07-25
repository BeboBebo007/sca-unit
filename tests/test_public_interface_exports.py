from sca_unit import (
    StructuralAssessment,
    StructuralState,
    assess_structures,
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
)


def test_legacy_public_exports_are_preserved():
    assert StructuralAssessment is not None
    assert StructuralState is not None
    assert assess_structures is not None


def test_typed_relation_public_exports_are_available():
    first = [{"source": "api", "target": "database", "type": "depends_on", "required": True}]
    second = [{"source": "api", "target": "database", "type": "writes_to", "required": True}]

    conflicts = detect_typed_relation_conflicts(first, second)

    assert count_typed_relation_conflicts(first, second) == 1
    assert conflicts[0]["conflict_type"] == "relation_type_changed"
