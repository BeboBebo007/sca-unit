# SCA-Unit

SCA-Unit is a structural assessment prototype designed to compare two system representations as structures rather than as isolated values.

It accepts two structural descriptions in JSON format and produces a deterministic assessment report containing:

- Node similarity
- Edge similarity
- Structural compatibility
- Shared-domain conflict
- A structural verdict

The current public prototype intentionally excludes proprietary structural consolidation, optimization, self-evolution, and protected decision mechanisms.

---

## Current Version

0.4.0

## Local Demo Package

Run the local browser demo with:

.\run_demo.ps1

The demo opens http://127.0.0.1:8765 and uses SCA_UNIT_API_KEY from .env.local.

## First-time setup after extraction

Before running the demo, create a local environment file named .env.local in the project root with this content:

SCA_UNIT_API_KEY=sca-unit-demo-key-2026-secure-local-001

This file is intentionally excluded from the public ZIP package.

## Demo Examples

Use these files for a quick browser demo:

- demo_examples/baseline_user.json
- demo_examples/changed_user.json

Paste baseline_user.json into the first JSON box and changed_user.json into the second JSON box, then click Compare structures.


---

## Command Line Usage

Show the installed version:

sca-unit --version

Run a full structural assessment report:

sca-unit first.json second.json

Run a short validation check without printing the full JSON report:

sca-unit first.json second.json --check

When input JSON is invalid, SCA-Unit prints an input error plus a short expected-format hint.

## Public Product Positioning

SCA-Unit is a public Python package for structural compatibility assessment between two structured software or logical states.

It can be used from the command line, from Python, or as a foundation for generated structural reports.

### Public use
- Compare two JSON structural states
- Produce a compatibility assessment
- Use the result in review, migration, integration, or system-evolution workflows

### Paid report layer
SCA-Unit can also support a paid structural report workflow:

1. Customer provides two JSON structural states.
2. SCA-Unit generates a raw JSON assessment.
3. A human-readable structural report is generated from the assessment.

This public layer does not expose AMNE internals or protected structural architecture.

## Public examples

The repository includes a small examples directory for quick testing:

- examples/example_system_v1.json
- examples/example_system_v2.json
- examples/example_paid_structural_report.md

Run the example assessment:

sca-unit examples/example_system_v1.json examples/example_system_v2.json --output examples/example_raw_report.json

Then inspect the generated raw report or use it as input for the paid report workflow.
