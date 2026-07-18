import json

import pytest

from paid_report_input_validation import (
    PaidReportInputValidationError,
    validate_paid_report_inputs,
)


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def test_valid_customer_json_inputs_pass_validation(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    write_json(first, {"nodes": ["a"], "edges": []})
    write_json(second, {"nodes": ["b"], "edges": []})

    first_data, second_data = validate_paid_report_inputs(first, second)

    assert first_data["nodes"] == ["a"]
    assert second_data["nodes"] == ["b"]


def test_missing_first_input_file_fails_validation(tmp_path):
    missing = tmp_path / "missing.json"
    second = tmp_path / "second.json"

    write_json(second, {"nodes": ["b"]})

    with pytest.raises(PaidReportInputValidationError, match="First input file does not exist"):
        validate_paid_report_inputs(missing, second)


def test_missing_second_input_file_fails_validation(tmp_path):
    first = tmp_path / "first.json"
    missing = tmp_path / "missing.json"

    write_json(first, {"nodes": ["a"]})

    with pytest.raises(PaidReportInputValidationError, match="Second input file does not exist"):
        validate_paid_report_inputs(first, missing)


def test_invalid_json_fails_validation(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    first.write_text("{invalid json", encoding="utf-8")
    write_json(second, {"nodes": ["b"]})

    with pytest.raises(PaidReportInputValidationError, match="First input file is not valid JSON"):
        validate_paid_report_inputs(first, second)


def test_empty_json_object_fails_validation(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    write_json(first, {})
    write_json(second, {"nodes": ["b"]})

    with pytest.raises(PaidReportInputValidationError, match="First input file must not be an empty JSON object"):
        validate_paid_report_inputs(first, second)


def test_non_object_json_fails_validation(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    write_json(first, ["not", "an", "object"])
    write_json(second, {"nodes": ["b"]})

    with pytest.raises(PaidReportInputValidationError, match="First input file must contain a JSON object"):
        validate_paid_report_inputs(first, second)


def test_secret_like_keys_fail_validation(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    write_json(first, {"api_key": "do-not-submit"})
    write_json(second, {"nodes": ["b"]})

    with pytest.raises(PaidReportInputValidationError, match="secret-like keys"):
        validate_paid_report_inputs(first, second)