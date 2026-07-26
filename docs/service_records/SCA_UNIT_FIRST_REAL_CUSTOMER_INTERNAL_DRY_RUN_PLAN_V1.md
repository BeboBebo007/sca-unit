# SCA-Unit First Real Customer Internal Dry Run Plan v1.0

## Purpose
Define the internal dry run plan for testing the first real customer workflow before using it with an actual customer.

## Dry run status
Internal controlled test only. No real customer data is used.

## Dry run objective
Verify that the full SCA-Unit customer workflow can run from intake to delivery using safe test JSON files and revised positive customer messages.

## Test data rule
Use only artificial JSON structural state files created for testing.

Do not use real customer files, private documents, credentials, secrets, tokens, or sensitive personal data.

## Required workflow steps
1. Use the revised intake message
2. Prepare two safe test JSON structural state files
3. Run input validation
4. Generate the structural comparison report
5. Manually review the generated report
6. Use the revised delivery message
7. Use the revised follow-up message
8. Record dry run observations

## Success criteria
- Intake message is clear
- Test files are accepted by validation
- Report generation completes successfully
- Report is readable
- Delivery message matches the completed report
- Follow-up message feels positive and useful
- No AMNE internals are exposed
- No protected structural architecture is exposed

## Failure criteria
- Validation behavior is unclear
- Report output is confusing
- Customer message language feels weak or fearful
- Workflow requires missing documentation
- Any protected knowledge appears in public-facing material

## Dry run record requirements
Record the dry run date, test file names, validation result, report generation result, manual review result, message review result, and final decision.

## Final decision options
- Ready for first real customer
- Ready with minor wording changes
- Needs documentation improvement
- Needs engineering improvement
- Not ready

## Protected knowledge rule
The dry run must not include AMNE internals, protected structural architecture, real customer data, credentials, secrets, or private submitted material.

## Next milestone
SCA-Unit First Real Customer Internal Dry Run Record Template v1.
