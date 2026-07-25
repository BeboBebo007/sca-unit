from sca_unit import (
    StructuralAssessment,
    StructuralState,
    assess_structures,
    count_typed_relation_conflicts,
    detect_typed_relation_conflicts,
    validate_typed_relations,
)


def test_all_public_exports_are_available_after_validation_export():
    assert StructuralAssessment is not None
    assert StructuralState is not None
    assert assess_structures is not None
    assert count_typed_relation_conflicts is not None
    assert detect_typed_relation_conflicts is not None
    assert validate_typed_relations is not None


def test_validate_typed_relations_is_publicly_exported():
    relations = [
        {"source": "api", "target": "database", "type": "depends_on", "required": True}
    ]

    result = validate_typed_relations(relations)

    assert result["valid_relations"] == relations
    assert result["invalid_relations"] == []
    assert result["validation_errors"] == []
