# SCA-Unit Move Release Records from Root v1.0

## Purpose
Record the first controlled movement of root Markdown files into an organized documentation folder.

## Movement status
Release records moved from repository root.

## Destination
docs/release_records/

## Movement method
git mv

## Scope
Only release, publishing, version, build, PyPI, TestPyPI, and release-readiness records were moved.

## Boundary
This milestone does not delete files.

## README link handling
README links were reviewed and updated where matching moved file names were found.

## Public surface value
This reduces the number of administrative Markdown files visible at the repository root and makes the project look more technical and easier to inspect.

## Safety rule
No project history was deleted.

## Not included
- service record movement
- project record movement
- repository-surface record movement
- archive record movement
- code change
- package build
- PyPI upload

## Final movement result
Release records are organized under docs/release_records/.

## Next milestone
Move Repository Surface Records from Root v1.