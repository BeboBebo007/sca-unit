# SCA-Unit v0.4.0 Release Checklist

## Current baseline
- Current public package version: 0.3.0
- Current branch: milestone/62-v040-release-checklist
- Current test count after Milestone 61: 50 passed

## Must be completed before v0.4.0
- Update pyproject.toml version from 0.3.0 to 0.4.0
- Update src/sca_unit/__init__.py __version__ to 0.4.0
- Confirm CLI command: sca-unit --version
- Confirm CLI command: sca-unit first.json second.json --check
- Confirm invalid input prints SCA-Unit input error and Hint
- Run full pytest suite
- Build wheel and source distribution
- Install package in a clean virtual environment
- Verify import sca_unit works
- Verify sca-unit CLI works after clean install
- Update README with --version, --check, and error guidance
- Update RELEASE_NOTES.md for v0.4.0
- Create final git tag only after all checks pass

## Release rule
Do not upload to PyPI until version numbers, tests, README, release notes, clean install, and CLI checks all pass.
