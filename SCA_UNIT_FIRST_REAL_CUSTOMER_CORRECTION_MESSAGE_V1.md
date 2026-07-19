# SCA-Unit First Real Customer Correction Message v1.0

## Purpose
Provide a safe correction message for the first real customer request when submitted files or request details need correction before processing.

## Message status
Approved public-safe customer correction message template.

## Customer correction message

Hello,

Thank you for sending the files for the SCA-Unit Structural Report service.

Before I can process the request, one or more items need correction so that the service remains safe and within scope.

Please check the following:

1. Send exactly two JSON structural state files
2. Confirm which file is the first state and which file is the second state
3. Remove any passwords, API keys, tokens, private keys, credentials, confidential secrets, unrelated private documents, or sensitive personal data
4. Make sure the request is limited to structural comparison only

Important limitation: this service is not a legal, financial, medical, cybersecurity, or compliance certification service. It provides a structural comparison report only.

After receiving corrected files, I will review the request again before generating any report.

Kind regards,
SCA-Unit

## Internal use note
Use this message when the customer request is potentially acceptable but requires correction before processing.

## Safety rule
Do not process files until the correction is complete and the intake checklist is satisfied.

## Protected knowledge rule
This message must not mention AMNE internals or protected structural architecture.

## Next milestone
SCA-Unit First Real Customer Rejection Message v1.
