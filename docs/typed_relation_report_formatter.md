# Typed Relation Report Formatter

## Purpose
SCA-Unit provides a helper for formatting typed relation conflicts as a human-readable report section.

## Public function
format_typed_relation_report_section(conflicts, validation_errors=None)

## What it does
The formatter converts typed relation conflict dictionaries into readable text.

It is intended for:
- manual structural reports
- readable summaries
- simple report sections
- explaining typed relation changes to non-developer users

## Basic example
from sca_unit import (
    detect_typed_relation_conflicts,
    format_typed_relation_report_section,
)

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

## Example output
Typed Relation Findings

Total typed relation conflicts: 1

Finding 1
Conflict type: relation_type_changed
Source: api
Target: database
Explanation: The relation between the same source and target exists in both structures, but the relation type changed.
Interpretation: This may indicate a meaningful architectural or dependency change.

## Empty result behavior
If there are no conflicts, the formatter returns:

Typed Relation Findings

No typed relation conflicts were detected.

## Validation warning behavior
If validation errors are provided, the formatter includes a validation warning section before the findings.

Example:
format_typed_relation_report_section(
    [],
    validation_errors=["missing field: source"],
)

## Boundary
This helper formats typed relation findings only.

It does not provide:
- SaaS
- automatic repository scanning
- company-wide analysis
- customer data storage
- advanced severity scoring
- full audit automation

## Public positioning
The formatter is a small report helper for SCA-Unit structural assessment workflows.

## Related functions
- detect_typed_relation_conflicts
- count_typed_relation_conflicts
- validate_typed_relations