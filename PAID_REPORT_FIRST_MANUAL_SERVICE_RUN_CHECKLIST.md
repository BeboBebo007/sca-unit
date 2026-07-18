# SCA-Unit Paid Report First Manual Service Run Checklist

## Purpose
Define the checklist for running the first controlled manual paid SCA-Unit structural report service.

## Before accepting the first request
- Confirm that the customer understands the service scope
- Confirm that the service is a manual structural assessment only
- Confirm that the customer will provide two JSON structural state files
- Confirm that the customer should not submit secrets, credentials, tokens, API keys, or private keys

## Input handling
- Store the two customer JSON files in a temporary working folder
- Confirm which file is the first structural state
- Confirm which file is the second structural state
- Run input validation before generating any report
- Stop the workflow if validation fails

## Report generation
- Run paid_report_service.py with the validated input files
- Generate the raw SCA-Unit assessment JSON
- Generate the paid Markdown structural report
- Review the report before customer delivery

## Customer delivery
- Use the customer delivery email template
- Attach only the paid Markdown report
- Attach raw assessment JSON only if included in the service scope
- Do not include temporary files, internal notes, or private implementation details

## After completion
- Record that the manual workflow completed
- Remove temporary customer files when no longer needed
- Keep only intentional public examples or documented service records

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Paid report first manual service run record template.
