# SCA-Unit Customer Input Validation Plan

## Purpose
Define how customer-provided JSON inputs should be checked before generating a structural compatibility report.

## Validation goals
- Confirm that both input files exist
- Confirm that both files are valid JSON
- Confirm that both files contain structured objects
- Reject empty or unusable structures clearly
- Avoid processing secrets, credentials, or private keys when detectable
- Provide simple customer-facing error messages

## Customer-safe error messages
Errors should explain what the customer must fix without exposing internal implementation details.

## Manual service relevance
For early manual paid reports, validation helps avoid wasting time on unusable inputs before assessment and report writing.

## Future automation direction
Validation can later become a pre-report step inside the paid report workflow.

## Product boundary
Validation applies to public SCA-Unit report inputs only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Customer input validation implementation plan.
