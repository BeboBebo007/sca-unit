# SCA-Unit Public Service Page Update v1.0

## Purpose
Provide a public-safe service page update for the manual SCA-Unit Structural Report service.

## Service title
SCA-Unit Structural Report

## Short description
A manual structural comparison report for two JSON structural state files.

## What this service does
SCA-Unit compares two structural representations and turns the result into a readable report.

The report helps clarify whether two JSON structural states appear compatible, partially compatible, or meaningfully different in structure.

## Best fit
This service is useful when you want to compare:
- Two versions of a JSON-based structure
- Two structural states before and after a change
- Two simple software or configuration representations
- Two schema-like structures

## What the customer sends
- Exactly two JSON structural state files
- A short note explaining which file is the first state and which file is the second state
- A short explanation of what changed between the two states

## Required JSON structure
Each file should include:
- identity
- nodes
- edges

## Minimal JSON example
{
  "identity": "example-state-1",
  "nodes": ["module_a", "module_b"],
  "edges": [["module_a", "module_b"]]
}

## What the customer receives
- Input summary
- Executive verdict
- Compatibility score
- Structural metrics
- Practical recommendation
- Service boundary

## What not to send
Please do not send passwords, API keys, tokens, private keys, credentials, confidential secrets, sensitive personal data, or unrelated private documents.

## Service mode
Manual controlled service operation.

## Service boundary
SCA-Unit provides a structural comparison report. It is not intended to replace legal, financial, medical, cybersecurity, or compliance advice.

## Public wording rule
The public page should be clear, useful, calm, and focused on value.

## Protected knowledge rule
This page must not mention AMNE internals or protected structural architecture.

## Next milestone
SCA-Unit First Real Customer Public README Link v1.
