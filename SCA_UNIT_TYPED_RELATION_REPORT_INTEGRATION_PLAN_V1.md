# SCA-Unit Typed Relation Report Integration Plan v1.0

## Purpose
Plan how typed relation findings should be integrated into human-readable structural reports.

## Plan status
Report integration planning record.

## Current public release
v0.5.0

## Current typed relation capabilities
SCA-Unit currently provides:
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Integration goal
Convert typed relation findings from raw Python results into readable report sections.

## Why this matters
Typed relation conflicts are useful technically, but customers need clear explanations, severity, meaning, and recommended interpretation.

## Proposed report section
A future structural report may include a section named:

Typed Relation Findings

## Proposed report fields
Each typed relation finding should include:
- conflict type
- source node
- target node
- first relation type
- second relation type
- required status before
- required status after
- human-readable explanation
- suggested interpretation

## Proposed conflict explanations

### relation_type_changed
The relation between the same source and target exists in both structures, but the relation type changed.

### required_status_changed
The relation between the same source and target exists in both structures, but its required status changed.

### relation_direction_reversed
The same relation appears with reversed direction between the two structures.

### required_relation_removed
A required relation exists in the first structure but is missing from the second structure.

## Proposed report value
This report section helps users understand structural changes that are not visible from simple node similarity alone.

## Initial report boundary
The first implementation should only add readable report text. It should not create a full audit platform.

## Not included in first implementation
- SaaS
- automatic repository scanning
- company-wide data processing
- web dashboard
- advanced severity scoring
- customer data storage

## Recommended implementation order
1. Define report text format.
2. Add a small formatting helper.
3. Add tests for readable report output.
4. Add one documentation example.

## Commercial meaning
Report integration moves SCA-Unit closer to paid manual structural reports.

## Final plan result
Typed relation findings should be integrated into reports as a clear human-readable section before moving toward SCA-Audit Lite.

## Next milestone
Typed Relation Report Section Specification v1.