import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_example(relative_path: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(ROOT / relative_path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def test_structural_assessment_example_runs():
    output = run_example("examples/structural_assessment_example.py")

    assert "SCA-Unit structural assessment example" in output
    assert "first_identity: baseline" in output
    assert "second_identity: changed" in output
    assert "node_similarity:" in output
    assert "edge_similarity:" in output
    assert "compatibility:" in output
    assert "verdict: partial" in output


def test_typed_relation_report_formatter_example_runs():
    output = run_example("examples/typed_relation_report_formatter_example.py")

    assert "Typed Relation Findings" in output
    assert "Total typed relation conflicts: 1" in output
    assert "Conflict type: relation_type_changed" in output
    assert "Source: api" in output
    assert "Target: database" in output