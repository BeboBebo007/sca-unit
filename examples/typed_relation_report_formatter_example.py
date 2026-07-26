from sca_unit import (
    detect_typed_relation_conflicts,
    format_typed_relation_report_section,
    validate_typed_relations,
)


first_relations = [
    {
        "source": "api",
        "target": "database",
        "type": "depends_on",
        "required": True,
    }
]

second_relations = [
    {
        "source": "api",
        "target": "database",
        "type": "writes_to",
        "required": True,
    }
]


first_validation = validate_typed_relations(first_relations)
second_validation = validate_typed_relations(second_relations)

validation_errors = (
    first_validation["validation_errors"]
    + second_validation["validation_errors"]
)

conflicts = detect_typed_relation_conflicts(first_relations, second_relations)

report = format_typed_relation_report_section(
    conflicts,
    validation_errors=validation_errors,
)

print(report)