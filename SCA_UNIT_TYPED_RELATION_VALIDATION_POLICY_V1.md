# SCA-Unit Typed Relation Conflict Engine Validation Policy v1.0

## Purpose
Define the validation policy for Typed Relation Conflict Engine inputs.

## Policy status
Validation policy definition.

## Current engine status
The engine currently accepts relation-like dictionary objects and performs deterministic comparison.

## Current input contract
The minimal accepted relation fields are:
- source
- target
- type
- required

## Validation principle
Validation should be explicit, deterministic, and backward-compatible.

## Policy goal
Avoid silent confusion when typed relation inputs are missing required fields or contain unclear values.

## Field validation: source
The source field should be present.

If missing:
- future validation should report an invalid relation input

If present:
- value may be converted to string for deterministic comparison

## Field validation: target
The target field should be present.

If missing:
- future validation should report an invalid relation input

If present:
- value may be converted to string for deterministic comparison

## Field validation: type
The type field should be present.

If missing:
- future validation should report an invalid relation input

If present:
- value may be converted to string for deterministic comparison

## Field validation: required
The required field should be present.

If missing:
- future validation should report an invalid relation input

If present:
- value may be converted to boolean only when the conversion is explicit and documented

## Recommended future validation behavior
A future validation layer may return:
- valid_relations
- invalid_relations
- validation_errors

## Validation error fields
A validation error should include:
- relation_index
- missing_field
- message

## Example validation error
{
  "relation_index": 0,
  "missing_field": "source",
  "message": "Typed relation is missing required field: source"
}

## Non-breaking rule
Validation should not break existing simple edge workflows.

## Additive rule
Validation should be added as a helper layer before deeper report or CLI integration.

## Current milestone boundary
This milestone defines policy only. It does not implement validation behavior.

## Not included yet
- runtime validation code
- strict schema enforcement
- CLI validation
- report integration
- paid report validation
- customer file ingestion
- SaaS validation

## Risk control
Do not silently treat incomplete relation objects as meaningful structural evidence.

## Final policy result
SCA-Unit now has a validation policy for typed relation inputs before implementing validation code.

## Next milestone
Typed Relation Conflict Engine Validation Helper v1.