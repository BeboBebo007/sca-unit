import argparse
import subprocess
import sys

from paid_report_input_validation import (
    PaidReportInputValidationError,
    validate_paid_report_inputs,
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a paid structural compatibility report from two JSON inputs."
    )
    parser.add_argument("first_json", help="Path to the first customer JSON file.")
    parser.add_argument("second_json", help="Path to the second customer JSON file.")
    parser.add_argument(
        "-r",
        "--raw-output",
        default="paid_raw_sca_report.json",
        help="Path for the raw SCA-Unit JSON assessment.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="paid_structural_report.md",
        help="Path for the generated paid report Markdown file.",
    )

    args = parser.parse_args()

    try:
        validate_paid_report_inputs(args.first_json, args.second_json)
    except PaidReportInputValidationError as exc:
        print(f"Input validation failed: {exc}", file=sys.stderr)
        return 2

    subprocess.run(
        [
            sys.executable,
            "-m",
            "sca_unit.cli",
            args.first_json,
            args.second_json,
            "--output",
            args.raw_output,
        ],
        check=True,
    )

    subprocess.run(
        [
            sys.executable,
            "generate_paid_report.py",
            args.raw_output,
            "--output",
            args.output,
        ],
        check=True,
    )

    print("Paid report workflow completed.")
    print(f"Raw assessment written to: {args.raw_output}")
    print(f"Paid report written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())