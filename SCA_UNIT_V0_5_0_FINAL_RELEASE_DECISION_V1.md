# SCA-Unit v0.5.0 Final Release Decision v1.0

## Purpose
Record the final release decision for SCA-Unit v0.5.0 before publishing.

## Decision status
Final release decision record.

## Version
v0.5.0

## Release decision
SCA-Unit v0.5.0 is approved for release preparation as an additive Python API release.

## Release theme
Typed Relation Public API.

## Confirmed release contents
SCA-Unit v0.5.0 includes:
- typed relation conflict detection
- typed relation conflict counting
- typed relation validation helper
- public Python API exports
- typed relation documentation
- typed relation validation documentation
- README links
- test coverage for typed relation functionality
- version update from 0.4.0 to 0.5.0

## Confirmed public functions
- StructuralAssessment
- StructuralState
- assess_structures
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Confirmed checks
- full test suite passed
- build completed
- twine metadata check passed
- local wheel install verified
- public typed relation functions verified
- legacy public API preserved

## Confirmed build artifacts
- dist/sca_unit-0.5.0.tar.gz
- dist/sca_unit-0.5.0-py3-none-any.whl

## Release boundary
This release must be described only as an additive Python API release.

## Not claimed in v0.5.0
- CLI typed relation analysis
- structured report integration
- paid report workflow integration
- SCA-Audit Lite
- SaaS
- automatic project auditing
- automated customer data processing

## Release note
SCA-Unit v0.5.0 adds typed relation conflict detection and validation helpers as public Python API features.

## Publish condition
Publishing to PyPI should happen only after the release tag is created and the final package files are verified again.

## Current milestone boundary
This milestone records the final release decision only. It does not publish to PyPI.

## Final decision result
SCA-Unit v0.5.0 is ready for final release tagging and publish preparation.

## Next milestone
v0.5.0 Release Tag Preparation v1.