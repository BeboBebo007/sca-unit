import json
from pathlib import Path

import sca_unit

import pytest

from sca_unit.cli import (
    build_report,
    create_parser,
    load_structural_state,
    main,
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
    assert report["engine"]["version"] == sca_unit.__version__
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

def test_load_structural_state_accepts_utf8_bom(tmp_path: Path) -> None:
    bom_path = tmp_path / 'bom.json'
    content = json.dumps({
        'identity': 'bom-case',
        'nodes': ['A', 'B'],
        'edges': [['A', 'B']],
    })
    bom_path.write_text(content, encoding='utf-8-sig')

    state = load_structural_state(bom_path)

    assert state.identity == 'bom-case'
    assert state.nodes == frozenset({'A', 'B'})
    assert state.edges == frozenset({('A', 'B')})



def test_cli_version_option_outputs_package_version(capsys) -> None:
    parser = create_parser()

    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["--version"])

    assert exc_info.value.code == 0
    assert f"sca-unit {sca_unit.__version__}" in capsys.readouterr().out


def test_cli_check_mode_prints_short_summary(tmp_path: Path, capsys, monkeypatch) -> None:
    first_path = tmp_path / "first.json"
    second_path = tmp_path / "second.json"

    write_structure(first_path, "first", ["A", "B"], [["A", "B"]])
    write_structure(second_path, "second", ["A", "B"], [["A", "B"]])

    monkeypatch.setattr("sys.argv", ["sca-unit", str(first_path), str(second_path), "--check"])

    assert main() == 0

    output = capsys.readouterr().out
    assert "SCA-Unit check passed." in output
    assert "Verdict: identical" in output
    assert "Compatibility: 1.0" in output
