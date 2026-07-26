# SCA-Unit Typed Relation Conflict Engine Specification v1.0

## Purpose
Define the first technical specification for a typed relation conflict engine in SCA-Unit.

## Specification status
Typed relation conflict engine specification.

## Background
The current public implementation compares nodes and edges mainly as sets. This is useful but not enough to distinguish deeper relationship-level conflicts.

## Engine goal
Detect meaningful conflicts between typed relations inside two JSON-first structural states.

## Core relation model
A typed relation should be represented as a structured object with explicit fields.

## Minimal relation fields
- source
- target
- type
- required

## Optional relation fields for later versions
- weight
- constraint
- version
- evidence
- domain
- label
- metadata

## Minimal JSON relation example
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

## First supported conflict types
- relation_type_changed
- relation_direction_reversed
- required_relation_removed
- required_status_changed

## Conflict 1: relation_type_changed
A conflict occurs when the same source and target exist in both structures but the relation type changes.

## Conflict 2: relation_direction_reversed
A conflict occurs when relation A -> B in one structure appears as B -> A in the other structure inside the same shared node domain.

## Conflict 3: required_relation_removed
A conflict occurs when a required relation in the first structure is missing from the second structure.

## Conflict 4: required_status_changed
A conflict occurs when a relation changes from required to optional or from optional to required.

## First engine inputs
- first structure
- second structure
- typed relation list from first structure
- typed relation list from second structure

## First engine outputs
- conflict count
- conflict list
- conflict type
- affected source
- affected target
- first relation snapshot
- second relation snapshot
- human-readable explanation

## Compatibility with existing edge model
The first implementation should preserve compatibility with the current simple edge model. Typed relations should be an additive capability, not a breaking replacement.

## Non-goals for first implementation
- No semantic matching
- No machine learning
- No graph database
- No SaaS
- No automatic project audit
- No enterprise integration
- No unsupported file format execution

## Expected value
This engine should allow SCA-Unit to distinguish between shallow edge difference and meaningful typed relationship conflict.

## SCA-Audit Lite relevance
Typed relation conflicts can later become evidence in a paid SCA-Audit Lite report for one software or AI project.

## Acceptance criteria
- Typed relations can be compared deterministically
- Changed relation type can be detected
- Reversed direction can be detected
- Required relation removal can be detected
- Required status change can be detected
- Existing simple examples should remain usable
- No protected internal mechanisms are disclosed

## Final specification result
SCA-Unit has a clear first technical specification for moving beyond raw set similarity into typed structural relation assessment.

## Next milestone
Typed Relation Conflict Engine Test Cases v1.