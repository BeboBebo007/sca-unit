# SCA-Unit README Structural Example Correction v1.0

## Purpose
Record correction of the README Python structural assessment example after README example verification.

## Correction status
README structural assessment example corrected.

## Issue found
The previous README Python example passed dictionaries directly into assess_structures.

The public API expects StructuralState objects for structural assessment.

## Correction made
The README example now imports StructuralState and constructs structural states explicitly before calling assess_structures.

## Verified examples
- StructuralState assessment example
- typed relation conflict example
- human-readable typed relation report example
- examples/typed_relation_report_formatter_example.py

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
README examples are aligned with the actual public Python API.

## Next milestone
Final Public First-Impression Review v1.