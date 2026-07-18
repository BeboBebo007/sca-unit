# SCA-Unit Product Hardening Plan

## Purpose
Define the next hardening phase after the post-release product phase closure.

## Phase focus
Improve reliability, clarity, automation, and customer-facing report quality without exposing protected architecture.

## Hardening areas
- Validate customer JSON inputs more clearly
- Improve error messages for invalid structures
- Strengthen paid report generation workflow
- Add clearer report sections for risks and recommendations
- Reduce manual steps where safe
- Preserve public-only SCA-Unit boundary

## Report automation direction
Paid reports may start manually, but the workflow should gradually become more automated: input check, raw assessment, Markdown report generation, and optional PDF-ready output.

## Product boundary
Hardening applies to the public SCA-Unit reporting layer only.

## Safety boundary
No AMNE internals or protected structural architecture exposed.

## Next milestone
Customer input validation plan.
