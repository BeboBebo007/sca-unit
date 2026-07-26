# SCA-Unit Move Repository Surface Records from Root v1.0

## Purpose
Record the controlled movement of repository-surface Markdown files into docs/repository_surface/.

## Movement status
Repository surface records moved from repository root.

## Destination
docs/repository_surface/

## Movement method
git mv

## Scope
Only GitHub, README, public repository, and documentation-surface records were moved.

## Boundary
This milestone does not delete files.

## README link handling
README links were reviewed and updated where matching moved file names were found.

## Public surface value
This reduces the number of repository-operation Markdown files visible at the root and makes the project easier to inspect.

## Safety rule
No project history was deleted.

## Not included
- service record movement
- project record movement
- archive record movement
- code change
- package build
- PyPI upload

## Final movement result
Repository surface records are organized under docs/repository_surface/.

## Next milestone
Move Project Records from Root v1.