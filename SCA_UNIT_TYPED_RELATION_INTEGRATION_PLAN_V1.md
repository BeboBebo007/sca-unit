# SCA-Unit Typed Relation Conflict Engine Integration Plan v1.0

## Purpose
Define a safe integration plan for the Typed Relation Conflict Engine.

## Current status
The minimal typed relation engine is implemented, exported, documented, and covered by tests.

## Confirmed test result
The full test suite passed after the typed relation engine was added.

## Current public boundary
The engine is available through the Python API only.

## Current public imports
from sca_unit import detect_typed_relation_conflicts
from sca_unit import count_typed_relation_conflicts

## Integration principle
Typed relation conflict detection must remain additive and must not break existing JSON structural comparison behavior.

## Phase 1: Python API
Status: completed.

The engine can be used directly by Python callers.

## Phase 2: Structured report integration
Future step.

Add typed relation conflict results to internal structured assessment reports only when input structures provide typed relation objects.

## Phase 3: CLI integration
Future step.

Expose typed relation conflict information through command-line output without changing existing CLI behavior for simple edge-based inputs.

## Phase 4: Paid report integration
Future step.

Use typed relation conflicts as evidence inside human-readable Structural Report outputs.

## Phase 5: SCA-Audit Lite connection
Future step.

Typed relation conflicts can support project-level audit reports for one software or AI project at a time.

## Not started in this milestone
- No report integration
- No CLI integration
- No paid report integration
- No SaaS
- No automated checkout
- No enterprise platform
- No customer data processing

## Risk control
Do not force typed relations into existing simple edge workflows. Typed relation analysis should run only when compatible relation objects are present.

## Final integration plan result
The Typed Relation Conflict Engine has a safe staged path from Python API to reports, CLI, paid reports, and later SCA-Audit Lite.

## Next milestone
Typed Relation Conflict Engine Input Contract v1.