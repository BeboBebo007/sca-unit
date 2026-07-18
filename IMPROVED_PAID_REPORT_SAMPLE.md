# SCA-Unit Improved Paid Report Sample

## Report title
Structural Compatibility Report

## Customer question
The customer wants to compare two structured JSON states before migration, integration, or technical review.

## Executive verdict
The two structures are partially compatible. They share enough structural similarity to support controlled integration, but several differences should be reviewed before production use.

## Compatibility score
0.708333

## Structural findings
- Node similarity indicates that many structural elements are aligned.
- Edge similarity indicates that relationships are similar but not identical.
- Shared-domain conflict is low in the sample assessment.
- The result supports cautious continuation rather than immediate rejection.

## Risk interpretation
The main risk is not total incompatibility, but silent structural drift between the two states. This means integration may work at first but later produce unexpected behavior if differences are ignored.

## Recommendation
Proceed with controlled integration only after reviewing the changed fields, relationship differences, and expected behavior of downstream systems.

## Service boundary
This report is based on SCA-Unit public structural outputs. It does not expose AMNE internals or protected structural architecture.
