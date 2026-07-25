from sca_unit.typed_relations import validate_typed_relations


def test_validate_typed_relations_accepts_valid_relation():
    relations = [
        {"source": "api", "target": "database", "type": "depends_on", "required": True}
    ]

    result = validate_typed_relations(relations)

    assert result["valid_relations"] == relations
    assert result["invalid_relations"] == []
    assert result["validation_errors"] == []


def test_validate_typed_relations_reports_missing_source():
    relations = [
        {"target": "database", "type": "depends_on", "required": True}
    ]

    result = validate_typed_relations(relations)

    assert result["valid_relations"] == []
    assert result["invalid_relations"] == relations
    assert result["validation_errors"][0]["relation_index"] == 0
    assert result["validation_errors"][0]["missing_field"] == "source"


def test_validate_typed_relations_reports_multiple_missing_fields():
    relations = [
        {"source": "api"}
    ]

    result = validate_typed_relations(relations)
    missing_fields = [error["missing_field"] for error in result["validation_errors"]]

    assert result["valid_relations"] == []
    assert result["invalid_relations"] == relations
    assert missing_fields == ["target", "type", "required"]
