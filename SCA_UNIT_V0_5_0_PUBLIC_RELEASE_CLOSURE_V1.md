# SCA-Unit v0.5.0 Public Release Closure v1.0

## Purpose
Close the public release cycle for SCA-Unit v0.5.0.

## Closure status
Public release closure record.

## Version
v0.5.0

## PyPI package
sca-unit==0.5.0

## PyPI page
https://pypi.org/project/sca-unit/0.5.0/

## Release tag
v0.5.0

## Release theme
Typed Relation Public API.

## Completed release steps
- version updated to 0.5.0
- changelog draft prepared
- release readiness reviewed
- pre-publish checklist completed
- final release decision recorded
- release tag created
- build artifacts verified
- PyPI upload completed
- public PyPI install verified
- legacy public API verified
- typed relation public API verified

## Verified public functions
- StructuralAssessment
- StructuralState
- assess_structures
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Verified public install command
pip install sca-unit==0.5.0

## Verified expected outputs
- version: 0.5.0
- import result: imports_ok
- typed relation conflict: relation_type_changed
- conflict count: 1
- validation errors for valid relation: empty list

## Public release note
SCA-Unit v0.5.0 adds typed relation conflict detection and validation helpers as public Python API features.

## Release boundary
This release is an additive Python API release.

## Not claimed in this release
- CLI typed relation analysis
- structured report integration
- paid report integration
- SCA-Audit Lite
- SaaS
- automatic project auditing
- automated customer data processing

## Security status
No PyPI token, password, credential, real customer data, or protected internal mechanism is stored in the repository.

## Final closure result
SCA-Unit v0.5.0 is publicly released, publicly installable from PyPI, and verified.

## Next milestone
Post-v0.5.0 Roadmap Reset v1.