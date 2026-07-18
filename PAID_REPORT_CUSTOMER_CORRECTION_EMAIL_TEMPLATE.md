# SCA-Unit Paid Report Customer Correction Email Template

## Purpose
Provide a standard customer-facing message requesting corrected input files for a paid SCA-Unit report.

## Email subject
Correction needed for your SCA-Unit Structural Report request

## Email body
Hello,

Thank you for your SCA-Unit Structural Report request.

We need corrected input files before we can generate your report.

Please resend two valid JSON structural state files:
- First structural state file
- Second structural state file

Please make sure that:
- Both files are valid JSON
- Both files contain JSON objects
- Neither file is empty
- The files do not contain passwords, tokens, API keys, private keys, credentials, or other secrets
- The files do not include unrelated documents or private implementation details

No report has been generated from the rejected files.

Once corrected files are received, the SCA-Unit paid report workflow can be run again.

Best regards,
SCA-Unit Service

## Manual service boundary
This template supports manual customer communication only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Paid report customer communication pack summary.
