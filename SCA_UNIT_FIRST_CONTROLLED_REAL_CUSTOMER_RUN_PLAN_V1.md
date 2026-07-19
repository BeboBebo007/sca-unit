# SCA-Unit First Controlled Real Customer Run Plan v1.0

## Purpose
Define the first controlled real customer run plan for the manual paid SCA-Unit Structural Report service.

## Core objective
Validate the manual paid report workflow under realistic customer-service conditions without expanding product scope.

## Run type
Controlled manual service run.

## Input required
- First customer-provided JSON structural state file
- Second customer-provided JSON structural state file
- Clear confirmation of which file is the first state and which file is the second state

## Input safety rule
Customer files must not contain passwords, tokens, API keys, private keys, credentials, secrets, unrelated private implementation details, or unrelated documents.

## Pre-run checklist
- Confirm customer request scope
- Confirm two JSON structural state files are available
- Confirm files are intended for structural comparison
- Confirm no secrets or credentials are included
- Confirm service limitation notice is understood
- Confirm this is not legal, financial, medical, cybersecurity, or compliance certification

## Execution workflow
1. Save customer files in a controlled local working folder
2. Validate input files using the paid report validation workflow
3. Generate raw SCA-Unit assessment JSON
4. Generate readable Markdown structural report
5. Review the report manually before delivery
6. Remove temporary files that should not be retained
7. Deliver only the approved customer-facing report

## Output to customer
- Markdown Structural Report
- Optional raw SCA-Unit assessment JSON only if included in agreed scope

## Evidence to record
- Date of run
- Type of customer request
- Whether input validation passed
- Whether report generation succeeded
- Any customer confusion
- Any documentation gap
- Any service workflow issue
- Any pricing or delivery lesson
- Final decision recommendation

## Do not record
- Customer secrets
- Credentials
- Private submitted data
- AMNE internals
- Protected structural architecture

## Success criteria
- Workflow completes without manual confusion
- Inputs are safely validated
- Report is generated repeatably
- Customer-facing output is clear
- Evidence is recorded without exposing protected knowledge

## Failure handling
If validation fails, do not generate a report. Use the customer rejection or correction communication templates.

## Current boundary
This milestone creates the plan only. It does not perform the real customer run.

## Next milestone
SCA-Unit First Controlled Real Customer Run Record Template v1.
