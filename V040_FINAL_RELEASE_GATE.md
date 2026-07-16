# SCA-Unit v0.4.0 Final Release Gate

## Required checks
- Version aligned to 0.4.0 in pyproject.toml
- Package __version__ aligned to 0.4.0
- README updated for v0.4.0
- RELEASE_NOTES updated for v0.4.0
- Wheel built: sca_unit-0.4.0-py3-none-any.whl
- Source distribution built: sca_unit-0.4.0.tar.gz
- Clean install verified from wheel
- CLI --version verified
- CLI --check verified
- Full test suite passed: 50 passed

## Release decision
v0.4.0 is ready for final publication only after this gate is committed and main remains clean.

## Warning
Do not upload to PyPI from a dirty working tree or before confirming the dist files are the intended v0.4.0 artifacts.
