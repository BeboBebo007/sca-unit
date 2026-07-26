# SCA-Unit Paid Report Manual Service Operation Checklist

## Purpose
Define the manual operating checklist for delivering a paid SCA-Unit structural report.

## Before accepting a request
- Confirm that the customer understands the service scope
- Confirm that the customer provides two JSON structural state files
- Confirm that the customer does not submit secrets, passwords, tokens, or private keys
- Confirm that the service is manual and not automated payment/order handling yet

## Input handling
- Store customer files in a temporary working folder
- Run customer input validation before report generation
- Stop the workflow if validation fails
- Do not manually edit customer input data except by explicit customer request

## Report generation
- Run paid_report_service.py with validated input files
- Generate the raw SCA-Unit assessment JSON
- Generate the paid Markdown report
- Review the Markdown report before delivery

## Delivery boundary
- Deliver only the paid report output
- Do not expose internal notes or temporary files
- Do not expose AMNE internals or protected structural architecture

## After delivery
- Remove temporary customer files when no longer needed
- Keep only intentional public examples or documented project files
- Record whether the workflow completed successfully

## Next milestone
Paid report customer delivery checklist.
