# SCA-Unit v0.5.0 PyPI Publish Preparation v1.0

## Purpose
Record PyPI publish preparation for SCA-Unit v0.5.0.

## Preparation status
PyPI publish preparation record.

## Version
v0.5.0

## Release tag
v0.5.0

## Current release theme
Typed Relation Public API.

## Expected distribution files
- dist/sca_unit-0.5.0.tar.gz
- dist/sca_unit-0.5.0-py3-none-any.whl

## Required checks before upload
- repository is clean
- release tag v0.5.0 exists
- full pytest suite passes
- twine metadata check passes
- wheel file exists
- source distribution file exists

## PyPI upload boundary
This milestone does not upload to PyPI.

## Do not include in public release claims
- CLI typed relation analysis
- structured report integration
- paid report integration
- SCA-Audit Lite
- SaaS
- automatic project auditing
- customer data processing

## Public release note
SCA-Unit v0.5.0 adds typed relation conflict detection and validation helpers as public Python API features.

## Safe publish command for the next milestone
python -m twine upload dist/*

## Security reminder
The PyPI token must never be committed, written into files, or pasted into the repository.

## Final preparation result
SCA-Unit v0.5.0 is ready for PyPI upload if the user explicitly approves the publish step.

## Next milestone
v0.5.0 PyPI Upload v1.