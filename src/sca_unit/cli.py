from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .assessment import assess_structures
from .models import StructuralState

INPUT_FORMAT_HINT = (
    'Expected input JSON: {"identity": "name", "nodes": ["A", "B"], '
    '"edges": [["A", "B"]]}'
)


def load_json_object(path: Path) -> dict[str, Any]:
    """Read a JSON object from a UTF-8 or UTF-8-BOM file."""
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise ValueError(f"Unable to read '{path}': {exc}") from exc

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in '{path}' at "
            f"line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(data, dict):
        raise ValueError(
            f"The top-level JSON value in '{path}' must be an object."
        )

    return data


def load_structural_state(path: Path) -> StructuralState:
    """Convert a JSON document into a StructuralState."""
    data = load_json_object(path)

    identity = data.get("identity")
    nodes = data.get("nodes")
    edges = data.get("edges")

    if not isinstance(identity, str):
        raise ValueError(f"'identity' in '{path}' must be a string.")

    if not identity.strip():
        raise ValueError(f"'identity' in '{path}' must not be empty.")

    if not isinstance(nodes, list):
        raise ValueError(f"'nodes' in '{path}' must be a list.")

    if not all(isinstance(node, str) for node in nodes):
        raise ValueError(
            f"Every node in '{path}' must be represented by a string."
        )

    if not isinstance(edges, list):
        raise ValueError(f"'edges' in '{path}' must be a list.")

    normalized_edges: list[tuple[str, str]] = []

    for index, edge in enumerate(edges):
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError(
                f"Edge #{index} in '{path}' must be a two-item list."
            )

        source, target = edge

        if not isinstance(source, str) or not isinstance(target, str):
            raise ValueError(
                f"Edge #{index} in '{path}' must contain string node names."
            )

        normalized_edges.append((source, target))

    return StructuralState.create(
        identity=identity,
        nodes=nodes,
        edges=normalized_edges,
    )


def build_report(
    first_path: Path,
    second_path: Path,
) -> dict[str, Any]:
    """Compare two structures and return a public assessment report."""
    first = load_structural_state(first_path)
    second = load_structural_state(second_path)

    assessment = assess_structures(first, second)

    return {
        "schema_version": "1.0",
        "engine": {
            "name": "SCA-Unit Public Structural Assessment",
            "version": __version__,
            "scope": "non-proprietary prototype",
        },
        "inputs": {
            "first_file": str(first_path),
            "second_file": str(second_path),
            "first_identity": first.identity,
            "second_identity": second.identity,
        },
        "assessment": assessment.as_dict(),
    }


def write_report(
    report: dict[str, Any],
    output_path: Path,
) -> None:
    """Save a formatted JSON report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        output_path.write_text(
            json.dumps(
                report,
                indent=2,
                ensure_ascii=False,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        raise ValueError(
            f"Unable to write report to '{output_path}': {exc}"
        ) from exc


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sca-unit",
        description=(
            "Compare two structural JSON files and generate "
            "a structural-assessment report."
        ),
    )

    parser.add_argument(
        "first",
        type=Path,
        help="Path to the first structural JSON file.",
    )

    parser.add_argument(
        "second",
        type=Path,
        help="Path to the second structural JSON file.",
    )

    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Optional path for the generated JSON report.",
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate inputs and print a short assessment summary without writing a report.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"sca-unit {__version__}",
    )

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    try:
        report = build_report(args.first, args.second)

        if args.check:
            print("SCA-Unit check passed.")
            print(f"Verdict: {report['assessment']['verdict']}")
            print(f"Compatibility: {report['assessment']['compatibility']}")
            return 0

        if args.output is not None:
            write_report(report, args.output)
            print(f"Report written to: {args.output}")
        else:
            print(
                json.dumps(
                    report,
                    indent=2,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )

        return 0

    except ValueError as exc:
        print(f"SCA-Unit input error: {exc}", file=sys.stderr)
        print(f"Hint: {INPUT_FORMAT_HINT}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
