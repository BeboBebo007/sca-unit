# SCA-Unit Paid Report Workflow Improvement

## Status
SCA-Unit now has a public post-release product direction.

## Workflow goal
Improve the paid structural report workflow so it is clear, repeatable, and understandable for a non-technical customer.

## Customer input
- First JSON structural state
- Second JSON structural state
- Optional short description of what the customer wants to compare

## Processing path
1. Validate that both inputs are structured JSON files.
2. Run SCA-Unit structural compatibility assessment.
3. Generate a raw JSON report.
4. Convert the raw report into a human-readable structural report.
5. Provide a concise verdict, score, risks, and recommendation.

## Report output
- Compatibility verdict
- Compatibility score
- Node similarity
- Edge similarity
- Shared-domain conflict signal
- Structural interpretation
- Practical recommendation

## Product boundary
This is a public paid reporting layer built on SCA-Unit outputs.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Create improved paid report sample text.
