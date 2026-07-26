# SCA-Unit Typed Relation Report Formatter Public Export Review v1.0

## Purpose
Review the public export status of the typed relation report formatter helper.

## Review status
Public export review record.

## Current public release
v0.5.0

## Reviewed helper
format_typed_relation_report_section

## Expected public import
from sca_unit import format_typed_relation_report_section

## Export location
src/sca_unit/__init__.py

## Source implementation
src/sca_unit/typed_relations.py

## Documentation
docs/typed_relation_report_formatter.md

## Tests
tests/test_typed_relation_report_formatter.py

## Review checklist
- helper is implemented
- helper is exported from package root
- helper appears in __all__
- helper is documented
- formatter tests pass
- full test suite passes

## Public API meaning
Users can access the formatter directly from the top-level sca_unit package.

## Boundary
This review confirms public export only.

## Not included
- version bump
- PyPI upload
- SaaS
- automatic repository scanning
- customer data processing
- protected internal mechanisms

## Final review result
The typed relation report formatter is publicly exported and documented if all checks pass.

## Next milestone
Typed Relation Report Formatter Usage Example v1.