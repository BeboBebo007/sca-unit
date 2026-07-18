# SCA-Unit Customer Input Validation Implementation Plan

## Purpose
Define the implementation steps for validating customer-provided JSON inputs before paid report generation.

## Proposed implementation
Add a small public validation layer for the paid report workflow.

## Validation checks
- Check that the first input path exists
- Check that the second input path exists
- Load both files as JSON
- Reject invalid JSON with a clear message
- Require each input to be a JSON object
- Reject empty JSON objects
- Detect likely secret-like keys when possible
- Return customer-safe validation errors

## Suggested file
paid_report_input_validation.py

## Integration target
paid_report_service.py should call the validation layer before running the raw SCA-Unit assessment.

## Customer-safe behavior
If validation fails, the workflow should stop before report generation and explain what the customer must fix.

## Product boundary
Implementation applies to the public SCA-Unit paid report workflow only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Implement paid report input validation module.
