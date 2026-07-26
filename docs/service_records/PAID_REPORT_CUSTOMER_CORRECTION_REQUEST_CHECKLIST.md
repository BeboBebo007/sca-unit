# SCA-Unit Paid Report Customer Correction Request Checklist

## Purpose
Define what to request from a customer when submitted files cannot be processed.

## When to request correction
- A required JSON file is missing
- A submitted file is not valid JSON
- A submitted JSON file is empty
- A submitted JSON file is not a JSON object
- Submitted data contains secret-like keys
- The customer submitted the wrong files

## Correction request checklist
- Ask the customer to resend two valid JSON structural state files
- Ask the customer to remove passwords, tokens, API keys, private keys, and credentials
- Ask the customer to confirm which file is the first state and which file is the second state
- Ask the customer not to send unrelated documents or private implementation details
- Confirm that no report was generated from rejected files

## Customer safety note
Customer files should not contain secrets, credentials, access tokens, passwords, or private keys.

## Manual service boundary
This checklist supports manual customer communication only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Paid report customer correction email template.
