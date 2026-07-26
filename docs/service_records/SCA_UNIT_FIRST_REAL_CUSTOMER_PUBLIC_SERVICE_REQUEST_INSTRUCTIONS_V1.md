# SCA-Unit First Real Customer Public Service Request Instructions v1.0

## Purpose
Provide public-safe request instructions for the first controlled real customer request for the manual SCA-Unit Structural Report service.

## Instruction status
Public-safe customer request instructions.

## What to send
To request a SCA-Unit Structural Report, send exactly two JSON structural state files.

Please label them clearly as:
- First state
- Second state

Also include a short note explaining what the two files represent.

## Required file format
Each JSON file should describe a structural state using:
- identity
- nodes
- edges

## Minimal example
{
  "identity": "example-state-1",
  "nodes": ["module_a", "module_b"],
  "edges": [["module_a", "module_b"]]
}

## What the report provides
The report compares the two structures and provides:
- Input summary
- Executive verdict
- Compatibility score
- Structural metrics
- Practical recommendation
- Service boundary

## What not to send
Do not send:
- Passwords
- API keys
- Tokens
- Private keys
- Credentials
- Confidential secrets
- Sensitive personal data
- Unrelated private documents

## Request note template
First state file: [file name]
Second state file: [file name]
Short explanation: [what changed between the two states]

## Service boundary
SCA-Unit provides a structural comparison report. It is not intended to replace legal, financial, medical, cybersecurity, or compliance advice.

## Protected knowledge rule
These instructions must not mention AMNE internals or protected structural architecture.

## Next milestone
SCA-Unit First Real Customer Public Service Page Update v1.
