import argparse
import json
from pathlib import Path

from reusable_service.service import assess_structure_files


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the reusable Python service."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--audit-log",
        default="evidence/reusable_service_audit.jsonl",
    )

    args = parser.parse_args()

    report = assess_structure_files(
        args.first_file,
        args.second_file,
        audit_log_path=args.audit_log,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Report written to: {output_path}")
    print(f"Request ID: {report['request_id']}")


if __name__ == "__main__":
    main()

