# SCA-Unit Release Notes

## v0.4.0 - Public usability improvement release

### Added
- Added sca-unit --version command.
- Added sca-unit first.json second.json --check for short validation summaries.
- Added clearer CLI input error guidance with an expected JSON format hint.
- Added v0.4.0 release checklist.

### Verified
- Full test suite passes: 50 passed.
- CLI report version is aligned with package __version__.
- UTF-8-BOM JSON input is supported.

### Release rule
Do not upload to PyPI until version numbers, README, release notes, clean install, and CLI checks all pass.

## v0.3.0 - First public PyPI release

Initial public SCA-Unit release on PyPI with structural JSON comparison, deterministic assessment reports, and public demo materials.
