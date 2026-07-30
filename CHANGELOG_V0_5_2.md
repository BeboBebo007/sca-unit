# SCA-Unit v0.5.2 Changelog v1.0

## Version
v0.5.2

## Release type
Small public quality release.

## Summary
SCA-Unit v0.5.2 improves public usability and example reliability without changing the structural assessment engine.

## Added
- Official runnable structural assessment example:
  - examples/structural_assessment_example.py
- Automated behavior tests for public examples:
  - tests/test_examples_behavior.py

## Updated
- README examples section now lists both runnable examples:
  - python examples/structural_assessment_example.py
  - python examples/typed_relation_report_formatter_example.py
- README Python usage example now uses StructuralState with identity values.
- Public version references updated from 0.5.1 to 0.5.2.

## Verified
- Structural assessment example runs successfully.
- Typed relation report formatter example runs successfully.
- Public example behavior is covered by pytest.
- Test suite increased from 76 tests to 78 tests.

## Not changed
- No structural assessment engine change.
- No algorithmic claim expansion.
- No paid-service expansion.
- No protected internal mechanisms disclosed.

## Final release note
v0.5.2 is a small reliability and public usability release.