# SCA-Unit Typed Relation Report Section Specification v1.0

## Purpose
Specify the human-readable report section for typed relation findings.

## Specification status
Report section specification record.

## Planned report section name
Typed Relation Findings

## Section purpose
The section explains typed relation conflicts in a format that non-developer users can understand.

## Input source
The section should be based on outputs from:
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Minimum section content
The report section should include:
- total typed relation conflicts
- list of findings
- conflict type
- source node
- target node
- explanation
- suggested interpretation

## Finding format
Each finding should be formatted as a readable block.

## Example finding format
Finding 1
Conflict type: relation_type_changed
Source: api
Target: database
Explanation: The relation between api and database changed type between the two structures.
Interpretation: This may indicate a meaningful architectural or dependency change.

## Conflict explanation rules

### relation_type_changed
Explain that the relation between the same source and target exists in both structures, but the relation type changed.

### required_status_changed
Explain that the relation between the same source and target exists in both structures, but the required status changed.

### relation_direction_reversed
Explain that a relation appears in reversed direction between the two structures.

### required_relation_removed
Explain that a required relation exists in the first structure but is missing from the second structure.

## Empty result behavior
If no typed relation conflicts are found, the section should say:
No typed relation conflicts were detected.

## Validation warning behavior
If validation errors exist, the report should include a validation warning before listing findings.

## Severity policy
This first report section should not introduce advanced severity scoring.

## Suggested wording boundary
The report should explain structural meaning without claiming automated enterprise auditing.

## Not included in this specification
- SaaS
- web dashboard
- automatic repository scanning
- company-wide analysis
- customer data storage
- advanced scoring engine

## Implementation recommendation
Implement a small formatting helper that converts typed relation conflict dictionaries into readable text.

## Final specification result
Typed relation report output should be a simple, readable, bounded report section suitable for manual structural reports.

## Next milestone
Typed Relation Report Formatter Helper v1.