# SCA-Unit v0.5.2 Install-from-Wheel Smoke Test v1.0

## Purpose
Verify that the locally built v0.5.2 wheel can be installed and used in a fresh isolated environment.

## Smoke test scope
Install from local wheel only.

## Checked items
- fresh virtual environment created
- local wheel installed successfully
- package import works
- installed version is 0.5.2
- public StructuralState API works
- assess_structures works
- CLI version command works
- project pytest suite still passes

## Boundary
This milestone performs install-from-wheel verification only.

## Not included
- PyPI upload
- publishing
- source engine change
- new algorithm
- customer data processing
- protected internal mechanisms

## Final result
v0.5.2 wheel is install-smoke-test ready.

## Next milestone
v0.5.2 Publish Decision Gate v1.