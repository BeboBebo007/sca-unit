# SCA-Unit

SCA-Unit is a JSON-first Structural Assessment Engine for comparing two structured states and producing a deterministic structural compatibility assessment.

The current public implementation accepts two JSON structural state files and reports node similarity, edge similarity, structural compatibility, shared-domain conflict, and a structural verdict.

Unlike a generic text diff tool, SCA-Unit focuses on structural relationships, compatibility signals, and explainable change between structured representations.

Public overview:

- [docs/structural_assessment_engine_public_overview.md](docs/structural_assessment_engine_public_overview.md)

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

This public layer is limited to the documented SCA-Unit workflow and does not include proprietary internal mechanisms.

## Public examples

The repository includes a small examples directory for quick testing:

- examples/example_system_v1.json
- examples/example_system_v2.json
- examples/example_paid_structural_report.md

Run the example assessment:

sca-unit examples/example_system_v1.json examples/example_system_v2.json --output examples/example_raw_report.json

Then inspect the generated raw report or use it as input for the paid report workflow.

## Public landing message

SCA-Unit compares two structured JSON states and produces a deterministic structural compatibility assessment.

It is intended for developers, reviewers, and technical teams who need to understand structural differences before migration, integration, review, or system evolution.

Install:

    pip install sca-unit==0.4.0

Quick command:

    sca-unit first.json second.json

This public layer is limited to the documented SCA-Unit workflow and does not include proprietary internal mechanisms.

## Paid structural report package

SCA-Unit includes a public paid-report package index for the Structural Compatibility Report service.

Start here:

PAID_REPORT_PUBLIC_PACKAGE_INDEX.md

This public service layer uses SCA-Unit outputs only and remains limited to the documented public workflow.

## Paid Structural Report Service

SCA-Unit also supports a manual paid structural report service based on two customer-provided JSON structural state files.

Read the service page: [PAID_REPORT_PUBLIC_PAGE_FINAL_VERSION.md](PAID_REPORT_PUBLIC_PAGE_FINAL_VERSION.md)

This public service page uses only the documented public SCA-Unit workflow.

## Public Launch Announcement

Read the public launch announcement for the manual paid SCA-Unit Structural Report service.

Launch announcement: [PAID_REPORT_PUBLIC_LAUNCH_ANNOUNCEMENT_FINAL_VERSION.md](PAID_REPORT_PUBLIC_LAUNCH_ANNOUNCEMENT_FINAL_VERSION.md)

This public announcement uses only the documented public SCA-Unit workflow.
## First Real Customer Structural Report Service

SCA-Unit is ready for a controlled first real customer request for the manual Structural Report service.

Public service page:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_PAGE_UPDATE_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_PAGE_UPDATE_V1.md)

Request instructions:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_REQUEST_INSTRUCTIONS_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_REQUEST_INSTRUCTIONS_V1.md)

This controlled service compares exactly two JSON structural state files and turns the result into a readable structural report.

Please do not submit passwords, API keys, tokens, private keys, credentials, confidential secrets, sensitive personal data, or unrelated private documents.

SCA-Unit provides a structural comparison report. It is not intended to replace legal, financial, medical, cybersecurity, or compliance advice.
## First Real Customer Service Index

For the controlled first real customer Structural Report service, start here:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_INDEX_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_SERVICE_INDEX_V1.md)

This index links the public service page, request instructions, and readiness notice for the manual SCA-Unit Structural Report service.
## First Real Customer Pricing

The controlled first customer Structural Report service uses simple initial pricing:

- Basic Report: 9 EUR
- Standard Report: 29 EUR
- Expert Report: 79 EUR

Recommended first customer tier:

- Standard Report: 29 EUR

Pricing alignment file:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_SERVICE_PRICING_ALIGNMENT_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_SERVICE_PRICING_ALIGNMENT_V1.md)

The service compares exactly two JSON structural state files and produces a readable structural report.
## First Real Customer Public Operation Notice

SCA-Unit is publicly ready to receive a first suitable customer request under controlled manual operation.

Operation start notice:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_OPERATION_START_NOTICE_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_OPERATION_START_NOTICE_V1.md)

The first suitable customer request must remain limited to exactly two JSON structural state files and must pass the acceptance checklist before work begins.
## First Real Customer Public Operation Final Index

SCA-Unit now includes a final public operation index for the first suitable customer Structural Report request.

Final operation index:

- [SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_OPERATION_FINAL_INDEX_V1.md](SCA_UNIT_FIRST_REAL_CUSTOMER_PUBLIC_OPERATION_FINAL_INDEX_V1.md)

This index collects the public service materials, operation control files, simulation confirmations, pricing, and acceptance boundaries for controlled manual operation.
## First Revenue Path

SCA-Unit now includes a controlled first revenue path for the manual Structural Report service.

First revenue path:

- [SCA_UNIT_FIRST_REVENUE_PATH_CONSOLIDATION_V1.md](SCA_UNIT_FIRST_REVENUE_PATH_CONSOLIDATION_V1.md)

Revenue readiness checklist:

- [SCA_UNIT_FIRST_REVENUE_READINESS_CHECKLIST_V1.md](SCA_UNIT_FIRST_REVENUE_READINESS_CHECKLIST_V1.md)

Manual operation record:

- [SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_RECORD_V1.md](SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_RECORD_V1.md)

Manual operation Go gate:

- [SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_GO_GATE_V1.md](SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_GO_GATE_V1.md)

Manual operation start notice:

- [SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_START_NOTICE_V1.md](SCA_UNIT_FIRST_REVENUE_MANUAL_OPERATION_START_NOTICE_V1.md)

Preferred first revenue offer:

- Standard Report: 29 EUR

This revenue path is manual and controlled. It does not include automated checkout, subscriptions, enterprise billing, or tax handling.
## External Documentation

SCA-Unit includes an external documentation index for public readers, code assistants, and future documentation alignment.

External documentation index:

- [docs/external_documentation_index.md](docs/external_documentation_index.md)

This index links the public structural assessment overview, README alignment records, public operation records, and first revenue path records.
## Documentation Surface Closure

SCA-Unit includes a final closure record for the current external documentation surface.

Documentation surface closure:

- [SCA_UNIT_DOCUMENTATION_SURFACE_FINAL_CLOSURE_V1.md](SCA_UNIT_DOCUMENTATION_SURFACE_FINAL_CLOSURE_V1.md)

This closure confirms that the current public documentation surface is stable for the JSON-first Structural Assessment Engine positioning.
