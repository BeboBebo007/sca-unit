# SCA-Unit v0.5.0 Pre-Publish Checklist v1.0

## Purpose
Record the pre-publish checklist for SCA-Unit v0.5.0.

## Checklist status
Pre-publish checklist record.

## Version
v0.5.0

## Completed checks
- Version number updated to 0.5.0
- Full test suite passed
- Source distribution built
- Wheel distribution built
- Package metadata check passed
- Local wheel install verified
- Public typed relation API verified
- Legacy public API preserved
- README updated
- Typed relation documentation added
- Typed relation validation documentation added

## Confirmed local install result
The built wheel installs locally as sca-unit 0.5.0.

## Confirmed typed relation outputs
- relation_type_changed
- conflict count: 1
- validation errors for valid relation: empty list

## Public functions included
- StructuralAssessment
- StructuralState
- assess_structures
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations

## Build artifacts expected
- dist/sca_unit-0.5.0.tar.gz
- dist/sca_unit-0.5.0-py3-none-any.whl

## Release boundary
The release should be presented as an additive Python API release.

## Not claimed
- CLI typed relation analysis
- structured report integration
- paid report integration
- SCA-Audit Lite
- SaaS
- automated customer data processing

## Remaining before publish
- final release decision
- final release tag
- PyPI upload only if approved
- post-publish verification only after upload

## Final checklist result
SCA-Unit v0.5.0 has passed the local pre-publish checklist and is ready for a final release decision.

## Next milestone
v0.5.0 Final Release Decision v1.