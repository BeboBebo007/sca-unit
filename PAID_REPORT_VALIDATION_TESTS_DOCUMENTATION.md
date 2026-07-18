# SCA-Unit Paid Report Validation Tests Documentation

## Purpose
Document repeatable validation scenarios for the paid report workflow.

## Test scenario 1: valid customer inputs
Input: sample_a.json and sample_b.json.

Expected behavior:
- Input validation passes
- Raw SCA-Unit assessment is generated
- Paid Markdown report is generated
- Workflow exits successfully

## Test scenario 2: missing first input file
Input: missing first JSON file and valid second JSON file.

Expected behavior:
- Input validation fails
- Workflow stops before raw assessment generation
- Workflow stops before paid report generation
- Customer-safe error message is shown

## Verified behavior
Both scenarios were manually validated in the paid report workflow.

## Temporary outputs
Generated validation output files should not be committed unless intentionally used as public examples.

## Product boundary
These tests document the public SCA-Unit paid report workflow only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Automated paid report validation tests plan.
