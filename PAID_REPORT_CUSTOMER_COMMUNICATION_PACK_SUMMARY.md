# SCA-Unit Paid Report Customer Communication Pack Summary

## Purpose
Summarize the customer communication documents used in the manual paid SCA-Unit report service.

## Included communication documents
- PAID_REPORT_CUSTOMER_EMAIL_DELIVERY_TEMPLATE.md
- PAID_REPORT_CUSTOMER_REJECTION_EMAIL_TEMPLATE.md
- PAID_REPORT_CUSTOMER_CORRECTION_REQUEST_CHECKLIST.md
- PAID_REPORT_CUSTOMER_CORRECTION_EMAIL_TEMPLATE.md

## Communication flow
1. If customer files are valid, generate the paid report and use the delivery email template.
2. If customer files fail validation, use the rejection email template.
3. If correction is possible, use the correction request checklist.
4. When asking for corrected files, use the correction email template.

## Customer safety principles
- Do not ask customers to send passwords, tokens, API keys, private keys, or credentials
- Do not include temporary files in customer communication
- Do not include internal notes or private implementation details
- Do not expose AMNE internals or protected structural architecture

## Manual service boundary
This communication pack supports manual service delivery only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Paid report manual service readiness summary.
