# SCA-Unit Remove Obsolete Private Service Tests v1.0

## Purpose
Remove obsolete private service tests that referenced private_server modules removed during commercial surface cleanup.

## Issue corrected
Milestone 311 removed private_server modules, but obsolete tests_private files still imported those modules and caused pytest collection errors.

## Correction made
- removed obsolete tests_private files tied to private_server
- removed tests_private from pytest discovery
- kept the public package tests focused on src/sca_unit and public examples

## Verification
The remaining public test suite passes after cleanup.

## Boundary
This milestone is cleanup correction only.

## Not included
- source engine change
- algorithm change
- PyPI upload
- package build
- new feature
- commercial service restoration

## Final public position
SCA-Unit remains a small, installable, deterministic Python package with a clean public test surface.

## Next milestone
Final Public Surface Consistency Check v1.