# SCA-Unit Typed Relation Validation v1.0

## Purpose
Document the public typed relation validation helper.

## Public import
from sca_unit import validate_typed_relations

## What it does
The validation helper checks typed relation inputs and separates valid relations from invalid relations.

## Required fields
Each typed relation should include:
- source
- target
- type
- required

## Example valid relation
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

## Example usage
from sca_unit import validate_typed_relations

relations = [
    {"source": "api", "target": "database", "type": "depends_on", "required": True}
]

result = validate_typed_relations(relations)

print(result["valid_relations"])
print(result["invalid_relations"])
print(result["validation_errors"])

## Returned fields
The helper returns:
- valid_relations
- invalid_relations
- validation_errors

## Example invalid relation
{
  "source": "api"
}

## Example validation error
{
  "relation_index": 0,
  "missing_field": "target",
  "message": "Typed relation is missing required field: target"
}

## Current boundary
This helper validates relation shape only. It does not run CLI validation, report integration, paid report validation, or SaaS ingestion.

## Why this matters
Typed relation validation prevents incomplete relation objects from being treated as meaningful structural evidence.

## Compatibility
The helper is additive and does not change existing SCA-Unit structural comparison behavior.

## Final documentation result
Typed relation validation is now documented as a public helper for safer typed relation usage.