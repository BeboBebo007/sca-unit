# SCA-Unit README Structural Example Real Fix v1.0

## Purpose
Record the actual correction of the README structural assessment example.

## Issue found
The previous correction did not modify README.md because the replacement block did not match the current README text.

A second issue was found during verification: StructuralState requires an identity argument.

## Correction made
The README Python usage example now uses:

StructuralState(identity="baseline", nodes=..., edges=...)
StructuralState(identity="changed", nodes=..., edges=...)

## Verified result
The README structural example was executed with the real public API.

## Boundary
This milestone changes README.md and adds this correction record.

## Not included
- source code change
- package build
- PyPI upload
- new feature
- customer data processing
- protected internal mechanisms

## Final correction result
README Python usage is now aligned with the actual StructuralState constructor and assess_structures API.

## Next milestone
Final Public First-Impression Review v1.