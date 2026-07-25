# SCA-Unit Typed Relation Conflict Engine v1.0

## Purpose
Document the minimal Typed Relation Conflict Engine added to SCA-Unit.

## Status
Minimal runtime engine available through the public Python package interface.

## Public import
from sca_unit import detect_typed_relation_conflicts
from sca_unit import count_typed_relation_conflicts

## What the engine does
The engine compares typed relations represented as dictionaries and detects deterministic relationship-level conflicts.

## Minimal relation format
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

## Supported conflict types
- relation_type_changed
- relation_direction_reversed
- required_relation_removed
- required_status_changed

## Example
from sca_unit import detect_typed_relation_conflicts

first = [
    {"source": "api", "target": "database", "type": "depends_on", "required": True}
]

second = [
    {"source": "api", "target": "database", "type": "writes_to", "required": True}
]

conflicts = detect_typed_relation_conflicts(first, second)
print(conflicts[0]["conflict_type"])

## Expected result
relation_type_changed

## Why this matters
This feature moves SCA-Unit beyond raw node and edge set comparison by detecting meaningful typed relationship changes.

## Current boundary
This is an additive Python API feature only. It is not yet integrated into the command line interface or paid report workflow.

## Compatibility
The existing SCA-Unit public functions remain available:
- StructuralAssessment
- StructuralState
- assess_structures

## Final documentation result
The Typed Relation Conflict Engine is documented as the first deeper structural capability in SCA-Unit.