# Sample SCA-Unit Structural Report

## Report type
Paid Structural Compatibility Report - Sample

## Input summary
- Source A: customer-system-v1
- Source B: customer-system-v2

## Executive verdict
Compatible

## Compatibility score
0.708333

## Structural metrics
- Node similarity: 0.75
- Edge similarity: 0.666667
- Conflict: 0.0
- Engine version: 0.4.0

## Structural findings
- Both systems share login, profile, and payment nodes.
- Source B adds an audit node.
- Source B adds a payment-to-audit edge.
- The systems remain compatible, but Source B introduces an additional monitoring or compliance layer.

## Risk interpretation
The added audit structure does not create a direct conflict, but it changes the system boundary and should be reviewed before migration, integration, or production deployment.

## Practical recommendation
Proceed only if the audit layer is intentional, required, and supported by the target environment.

## Service boundary
This report is generated from public SCA-Unit functionality and does not expose protected internal architecture.
