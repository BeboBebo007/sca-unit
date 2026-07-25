# SCA-Unit Version Planning for v0.5.0 v1.0

## Purpose
Define the version planning rationale for SCA-Unit v0.5.0.

## Planning status
Version planning record.

## Current public version
The current package version is v0.4.0.

## Proposed next version
v0.5.0

## Why v0.5.0
The typed relation layer adds a meaningful new public Python API capability while preserving the existing structural assessment interface.

## Proposed v0.5.0 scope
SCA-Unit v0.5.0 may include:
- typed relation conflict detection
- typed relation conflict counting
- typed relation validation helper
- public Python API exports
- typed relation documentation
- README links
- full public API test confirmation

## Proposed public functions
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Legacy functions preserved
- StructuralAssessment
- StructuralState
- assess_structures

## Release boundary
v0.5.0 should not claim CLI integration, report integration, paid workflow integration, SaaS capability, or automatic project auditing.

## Recommended release note
Added typed relation conflict detection and validation helpers as public Python API features.

## Compatibility expectation
The release should remain backward-compatible with v0.4.0 public imports.

## Required checks before release
- full pytest suite passes
- version number updated
- changelog updated
- README remains accurate
- build succeeds
- package metadata check succeeds

## Not included in v0.5.0
- command-line typed relation analysis
- structured report integration
- paid report workflow integration
- SCA-Audit Lite
- SaaS
- customer data processing

## Final planning result
v0.5.0 is justified as a focused additive release for typed relation public API functionality.

## Next milestone
v0.5.0 Changelog Draft v1.