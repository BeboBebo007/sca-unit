# SCA-Unit Paid Report Order Workflow Draft

## Purpose
Define a simple order workflow for paid structural compatibility reports.

## Order steps
1. Customer selects report type: Basic, Standard, or Expert.
2. Customer prepares two structured JSON files.
3. Customer optionally writes a short comparison goal.
4. SCA-Unit assessment is generated from the two JSON states.
5. A human-readable report is prepared from the public SCA-Unit output.
6. Customer receives the report as a Markdown or PDF-ready document.

## Required customer input
- First JSON structural state
- Second JSON structural state
- Selected report type
- Optional comparison goal

## Delivery output
- Human-readable structural compatibility report
- Compatibility verdict
- Compatibility score
- Structural findings
- Risk interpretation
- Practical recommendation

## Current limitation
This is an early manual workflow draft, not an automated payment or web ordering system.

## Service boundary
Reports are based on public SCA-Unit outputs only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Create paid report customer instruction template.
