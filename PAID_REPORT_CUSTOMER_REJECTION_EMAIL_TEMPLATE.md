# SCA-Unit Paid Report Customer Rejection Email Template

## Purpose
Provide a standard customer-facing message when a paid SCA-Unit report request cannot be processed.

## Email subject
SCA-Unit Structural Report request cannot be processed yet

## Email body
Hello,

Thank you for your SCA-Unit Structural Report request.

At this stage, we cannot process the submitted files because the input validation step did not pass.

Possible reasons include:
- A required JSON file is missing
- A file is not valid JSON
- A submitted JSON file is empty
- A submitted JSON file is not a JSON object
- The submitted data may contain secret-like keys such as passwords, tokens, API keys, or private keys

Please review the files and submit corrected JSON structural state files.

For your safety, do not submit passwords, access tokens, API keys, private keys, credentials, or other secrets.

No report has been generated from the rejected files.

Best regards,
SCA-Unit Service

## Rejection boundary
This message is for manual customer communication only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Paid report customer correction request checklist.
