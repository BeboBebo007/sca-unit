# SCA-Unit

SCA-Unit is a small Python package for structural compatibility assessment.

It compares structured JSON states and reports structural similarity, compatibility, and typed relation conflicts. It is designed for deterministic, lightweight checks where a normal text diff is not enough.

## What it does

SCA-Unit helps compare two structural states by looking at:

- node similarity
- edge similarity
- structural compatibility
- shared-domain conflicts
- typed relation conflicts
- human-readable relation findings

It can be used from Python or from the command line.

## Installation

    pip install sca-unit

PyPI package:

    https://pypi.org/project/sca-unit/

## Command line usage

Check the installed version:

    sca-unit --version

Compare two JSON files:

    sca-unit first.json second.json

Run a quick compatibility check:

    sca-unit first.json second.json --check

## Basic JSON shape

SCA-Unit expects structured input that represents nodes and edges.

Example:

    {
      "nodes": ["api", "database"],
      "edges": [["api", "database"]]
    }

## Python usage

    from sca_unit import assess_structures

    first = {
        "nodes": ["api", "database"],
        "edges": [["api", "database"]],
    }

    second = {
        "nodes": ["api", "cache"],
        "edges": [["api", "cache"]],
    }

    result = assess_structures(first, second)
    print(result)

## Typed relation checks

SCA-Unit also supports typed relation comparison.

It can detect:

- relation type changes
- required-status changes
- reversed relation direction
- removed required relations

Example:

    from sca_unit import detect_typed_relation_conflicts
    from sca_unit import format_typed_relation_report_section

    first = [
        {
            "source": "api",
            "target": "database",
            "type": "depends_on",
            "required": True,
        }
    ]

    second = [
        {
            "source": "api",
            "target": "database",
            "type": "writes_to",
            "required": True,
        }
    ]

    conflicts = detect_typed_relation_conflicts(first, second)
    report = format_typed_relation_report_section(conflicts)
    print(report)

## Human-readable report section

The typed relation formatter produces plain text findings that can be read by humans.

Example output:

    Typed Relation Findings

    Total typed relation conflicts: 1

    Finding 1
    Conflict type: relation_type_changed
    Source: api
    Target: database
    Explanation: The relation between the same source and target exists in both structures, but the relation type changed.
    Interpretation: This may indicate a meaningful architectural or dependency change.

## Documentation

Public documentation is available in the docs/ folder.

Useful entry points:

- docs/typed_relation_conflict_engine.md
- docs/typed_relation_validation.md
- docs/typed_relation_report_formatter.md
- docs/repository_surface/public_repository_surface_final_review_v1.md

Historical project records are organized under:

- docs/release_records/
- docs/service_records/
- docs/project_records/
- docs/archive_records/
- docs/repository_surface/

## Examples

Runnable examples are available in the examples/ folder.

Example:

    python examples/typed_relation_report_formatter_example.py

## Tests

Run the test suite with:

    python -m pytest -q

Current public release verification has passed with:

    76 passed

## Scope and limitations

SCA-Unit is intentionally small.

It is not:

- a full enterprise architecture platform
- a complete software composition analysis system
- a security scanner
- a replacement for human architecture review
- an automatic repository analysis service

It is a lightweight structural comparison package that can be used as a building block for higher-level review workflows.

## Project status

Current public version:

    0.5.1

The package is usable from PyPI and includes a command line interface, Python API, typed relation checks, examples, and tests.

## Design principle

The project aims to stay practical, deterministic, and clear.

It should not overstate what it does. The public package should be easy to install, easy to inspect, and easy to test.
