import subprocess
import sys


def run_paid_report_service(project_root, first, second, raw_output, report_output):
    return subprocess.run(
        [
            sys.executable,
            str(project_root / "paid_report_service.py"),
            str(first),
            str(second),
            "--raw-output",
            str(raw_output),
            "--output",
            str(report_output),
        ],
        cwd=project_root,
        text=True,
        capture_output=True,
    )


def test_paid_report_service_generates_outputs_for_valid_inputs(tmp_path):
    project_root = tmp_path.cwd()

    first = project_root / "sample_a.json"
    second = project_root / "sample_b.json"
    raw_output = tmp_path / "raw_report.json"
    report_output = tmp_path / "paid_report.md"

    result = run_paid_report_service(project_root, first, second, raw_output, report_output)

    assert result.returncode == 0
    assert raw_output.exists()
    assert report_output.exists()
    assert "Paid report workflow completed." in result.stdout


def test_paid_report_service_stops_for_missing_input(tmp_path):
    project_root = tmp_path.cwd()

    missing = tmp_path / "missing.json"
    second = project_root / "sample_b.json"
    raw_output = tmp_path / "raw_report.json"
    report_output = tmp_path / "paid_report.md"

    result = run_paid_report_service(project_root, missing, second, raw_output, report_output)

    assert result.returncode == 2
    assert not raw_output.exists()
    assert not report_output.exists()
    assert "Input validation failed" in result.stderr
    assert "First input file does not exist" in result.stderr