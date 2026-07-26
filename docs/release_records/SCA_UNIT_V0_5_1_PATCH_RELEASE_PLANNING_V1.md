# SCA-Unit v0.5.1 Patch Release Planning v1.0

## Purpose
Plan the v0.5.1 patch release for SCA-Unit.

## Planning status
Patch release planning record.

## Current public release
v0.5.0

## Planned next release
v0.5.1

## Release type
Patch release.

## Planned release theme
Typed Relation Report Formatter.

## Planned public addition
The v0.5.1 patch release should include:
- format_typed_relation_report_section
- public export from sca_unit
- formatter tests
- formatter documentation
- runnable formatter example
- README example link

## Why this is a patch release
The release adds a small public helper and documentation around existing typed relation capabilities.

## Public value
The formatter makes typed relation findings easier to use in human-readable structural reports.

## Commercial value
The formatter supports the manual paid Structural Report workflow by turning raw typed relation findings into readable report text.

## Required checks before release
- version bump from 0.5.0 to 0.5.1
- full test suite passes
- README references are correct
- formatter example runs
- build artifacts are regenerated
- twine check passes
- release readiness is recorded
- release tag is created before PyPI upload

## Expected verification commands
python -m pytest -q
python examples/typed_relation_report_formatter_example.py
python -m build
python -m twine check dist/*

## Release boundary
v0.5.1 should remain a small public Python package patch release.

## Not included in v0.5.1
- SaaS
- web dashboard
- automatic repository scanning
- company-wide analysis
- customer data processing
- advanced severity scoring
- protected internal mechanisms

## Recommended release note
SCA-Unit v0.5.1 adds a human-readable formatter for typed relation findings, with documentation and a runnable example.

## Final planning result
SCA-Unit v0.5.1 should be prepared as a small patch release focused on the typed relation report formatter.

## Next milestone
v0.5.1 Version Bump v1.