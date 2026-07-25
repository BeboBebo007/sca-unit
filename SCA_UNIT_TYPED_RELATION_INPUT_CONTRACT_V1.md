# SCA-Unit Typed Relation Conflict Engine Input Contract v1.0

## Purpose
Define the accepted input contract for the Typed Relation Conflict Engine.

## Contract status
Input contract definition.

## Current engine status
The Typed Relation Conflict Engine is implemented, exported, documented, tested, and planned for staged integration.

## Minimal accepted relation object
Each typed relation should be represented as a dictionary-like object.

## Required fields
- source
- target
- type
- required

## Field: source
The source field identifies the origin node of the relation.

Expected value:
- string-compatible value

Example:
api

## Field: target
The target field identifies the destination node of the relation.

Expected value:
- string-compatible value

Example:
database

## Field: type
The type field identifies the meaning of the relation.

Expected value:
- string-compatible value

Examples:
- depends_on
- calls
- writes_to
- requires

## Field: required
The required field identifies whether the relation is required.

Expected value:
- boolean-compatible value

Examples:
- true
- false

## Minimal valid relation example
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

## Minimal valid relation list example
[
  {
    "source": "api",
    "target": "database",
    "type": "depends_on",
    "required": true
  }
]

## Accepted engine inputs
The engine accepts two relation lists:
- first_relations
- second_relations

## Expected Python usage
from sca_unit import detect_typed_relation_conflicts

first_relations = [
    {"source": "api", "target": "database", "type": "depends_on", "required": True}
]

second_relations = [
    {"source": "api", "target": "database", "type": "writes_to", "required": True}
]

conflicts = detect_typed_relation_conflicts(first_relations, second_relations)

## Current normalization behavior
The current engine converts source, target, and type values to strings for deterministic comparison.

## Current required behavior
The current engine converts the required value to a boolean.

## Boundary
This contract defines the accepted minimal input shape. It does not add validation errors, schemas, CLI behavior, or report integration.

## Not included yet
- strict JSON schema validation
- CLI input validation
- structured report integration
- paid report input validation
- automatic project scanning
- SaaS ingestion
- customer data processing

## Risk control
Typed relation analysis should only run when relation-like objects are provided. Existing simple edge workflows should remain unaffected.

## Final contract result
SCA-Unit now has a public minimal input contract for typed relation conflict detection.

## Next milestone
Typed Relation Conflict Engine Validation Policy v1.