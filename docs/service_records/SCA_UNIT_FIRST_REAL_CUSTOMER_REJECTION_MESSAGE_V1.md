# SCA-Unit First Real Customer Rejection Message v1.0

## Purpose
Provide a safe rejection message for the first real customer request when the submitted request is unsafe, unclear, or outside the current manual service boundary.

## Message status
Approved public-safe customer rejection message template.

## Customer rejection message

Hello,

Thank you for your interest in the SCA-Unit Structural Report service.

After reviewing the request, I cannot process it in its current form because it is outside the safe scope of this service or does not meet the current intake requirements.

This service currently accepts only a limited structural comparison request based on exactly two JSON structural state files.

I cannot process files or requests that include passwords, API keys, tokens, private keys, credentials, confidential secrets, unrelated private documents, sensitive personal data, or requests for legal, financial, medical, cybersecurity, or compliance certification.

For safety, no report will be generated from the submitted material.

You may submit a corrected request later if it contains only two JSON structural state files and is limited to structural comparison.

Kind regards,
SCA-Unit

## Internal use note
Use this message when the request is unsafe, out of scope, or cannot be corrected safely in its submitted form.

## Safety rule
Do not process rejected files. Do not generate a report from unsafe or out-of-scope material.

## Protected knowledge rule
This message must not mention AMNE internals or protected structural architecture.

## Next milestone
SCA-Unit First Real Customer Delivery Message v1.
