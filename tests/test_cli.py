import json
from pathlib import Path

import pytest

from sca_unit.cli import (
    build_report,
    load_structural_state,
    write_report,
)


def write_structure(
    path: Path,
    identity: str,
    nodes: list[str],
    edges: list[list[str]],
) -> None:
    path.write_text(
        json.dumps(
            {
                "identity": identity,
                "nodes": nodes,
                "edges": edges,
            }
        ),
        encoding="utf-8",
    )


def test_build_report_for_identical_structures(
    tmp_path: Path,
) -> None:
    first_path = tmp_path / "first.json"
    second_path = tmp_path / "second.json"

    write_structure(
        first_path,
        "first",
        ["A", "B", "C"],
        [["A", "B"], ["B", "C"]],
    )

    write_structure(
        second_path,
        "second",
        ["A", "B", "C"],
        [["A", "B"], ["B", "C"]],
    )

    report = build_report(first_path, second_path)

    assert report["schema_version"] == "1.0"
    assert report["assessment"]["verdict"] == "identical"
    assert report["assessment"]["compatibility"] == pytest.approx(1.0)
    assert report["assessment"]["conflict"] == pytest.approx(0.0)


def test_write_report(tmp_path: Path) -> None:
    output_path = tmp_path / "reports" / "result.json"

    report = {
        "schema_version": "1.0",
        "assessment": {
            "verdict": "compatible",
        },
    }

    write_report(report, output_path)

    saved = json.loads(output_path.read_text(encoding="utf-8"))

    assert output_path.exists()
    assert saved["assessment"]["verdict"] == "compatible"


def test_rejects_invalid_edge_format(tmp_path: Path) -> None:
    invalid_path = tmp_path / "invalid.json"

    write_structure(
        invalid_path,
        "invalid",
        ["A", "B"],
        [["A"]],
    )

    with pytest.raises(ValueError, match="two-item list"):
        load_structural_state(invalid_path)