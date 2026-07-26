# SCA-Unit Public Repository Surface Cleanup Plan v1.0

## Purpose
Plan a cleanup of the public repository surface after the v0.5.1 release.

## Cleanup status
Planning record.

## Current public release
v0.5.1

## Why this cleanup is needed
The repository currently contains many operational, readiness, launch, pricing, and milestone Markdown records at the root level.

These files are useful as internal project history, but they can make the public repository look larger administratively than technically.

## Cleanup goal
Make the public repository easier to understand for developers, reviewers, and first-time visitors.

## Public surface target
The root of the repository should emphasize:
- README.md
- pyproject.toml
- CHANGELOG_V0_5_1.md
- src/
- tests/
- docs/
- examples/

## Files that should remain prominent
- README.md
- CHANGELOG_V0_5_1.md
- pyproject.toml

## Files that may be moved later
Operational and milestone records may be moved into organized documentation folders, such as:
- docs/project_records/
- docs/service_records/
- docs/release_records/
- docs/archive_records/

## Important boundary
This milestone does not move files.

It only records the cleanup plan.

## Not included
- code change
- package rebuild
- PyPI upload
- deletion of project history
- hidden proprietary mechanisms
- customer data processing

## Safety rule
No public file should be deleted during cleanup unless it is clearly redundant and separately reviewed.

## Link safety
Any future file movement must be followed by README link review.

## Technical positioning after cleanup
SCA-Unit should be presented as a small, clear, public Python package for structural compatibility assessment and typed relation conflict reporting.

## Final planning result
The repository is ready for a controlled public surface audit.

## Next milestone
Root Markdown Inventory v1.