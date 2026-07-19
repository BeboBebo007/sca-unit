# SCA-Unit First Real Customer Operation Gate v1.0

## Purpose
Define the final operation gate before accepting the first controlled real customer request for the manual SCA-Unit Structural Report service.

## Gate status
First real customer operation gate.

## Gate principle
A customer request may be accepted only when it fits the focused SCA-Unit Structural Report workflow.

## Required acceptance conditions
- Customer request is limited to structural comparison: yes/no
- Exactly two JSON structural state files are provided: yes/no
- File order is clear: yes/no
- Files pass input validation: yes/no
- No credentials, tokens, secrets, or private keys are present: yes/no
- No unrelated private documents are included: yes/no
- No sensitive personal data is included: yes/no
- Customer understands the report is structural comparison only: yes/no

## Required customer message
Use the revised positive intake message before accepting the request.

## Allowed operation
The operator may generate a manual SCA-Unit Structural Report only after all acceptance conditions are satisfied.

## Correction path
If the request is close but incomplete, use the revised correction message.

## Rejection path
If the request does not match the focused workflow, use the revised rejection message.

## Delivery path
After successful validation, generation, and manual review, use the revised delivery message.

## Follow-up path
After delivery, use the revised follow-up message and record general feedback safely.

## Operator decision
Choose one:
- Accept for controlled first customer workflow
- Request correction
- Reject request
- Pause for review

## Evidence rule
Record operation evidence without customer secrets, credentials, private submitted data, AMNE internals, or protected structural architecture.

## Service boundary
SCA-Unit provides a structural comparison report. It is not intended to replace legal, financial, medical, cybersecurity, or compliance advice.

## Final gate result
The service may proceed to controlled first real customer operation only when this gate is satisfied.

## Next milestone
SCA-Unit First Real Customer Operation Record v1.
