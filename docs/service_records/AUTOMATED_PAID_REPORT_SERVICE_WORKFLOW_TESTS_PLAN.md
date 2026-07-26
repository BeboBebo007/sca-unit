# SCA-Unit Automated Paid Report Service Workflow Tests Plan

## Purpose
Define automated tests for the complete paid report service workflow.

## Planned workflow tests
- Valid inputs should generate a raw assessment file
- Valid inputs should generate a paid Markdown report file
- Missing input should stop the workflow before output generation
- Invalid input should return a customer-safe validation error
- Service command should return a success exit code for valid inputs
- Service command should return a failure exit code for invalid inputs

## Suggested test target
paid_report_service.py

## Suggested test file
tests/test_paid_report_service_workflow.py

## Expected valid workflow behavior
The service should validate customer inputs, generate the raw SCA-Unit assessment, generate the paid Markdown report, and complete successfully.

## Expected invalid workflow behavior
The service should stop before report generation and return a customer-safe error.

## Product boundary
Tests apply to the public SCA-Unit paid report service workflow only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Implement automated paid report service workflow tests.
