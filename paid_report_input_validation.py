import json
from pathlib import Path


SECRET_KEY_HINTS = (
    "password",
    "passwd",
    "secret",
    "token",
    "api_key",
    "apikey",
    "private_key",
    "credential",
    "credentials",
)


class PaidReportInputValidationError(ValueError):
    """Customer-safe validation error for paid report inputs."""


def _contains_secret_like_key(value):
    if isinstance(value, dict):
        for key, nested in value.items():
            normalized_key = str(key).lower()
            if any(hint in normalized_key for hint in SECRET_KEY_HINTS):
                return True
            if _contains_secret_like_key(nested):
                return True
    elif isinstance(value, list):
        return any(_contains_secret_like_key(item) for item in value)
    return False


def load_validated_customer_json(path, label):
    input_path = Path(path)

    if not input_path.exists():
        raise PaidReportInputValidationError(f"{label} file does not exist: {path}")

    try:
        with input_path.open("r", encoding="utf-8-sig") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise PaidReportInputValidationError(f"{label} file is not valid JSON: {exc.msg}") from exc

    if not isinstance(data, dict):
        raise PaidReportInputValidationError(f"{label} file must contain a JSON object.")

    if not data:
        raise PaidReportInputValidationError(f"{label} file must not be an empty JSON object.")

    if _contains_secret_like_key(data):
        raise PaidReportInputValidationError(
            f"{label} file appears to contain secret-like keys. Remove secrets, credentials, tokens, or private keys before submitting."
        )

    return data


def validate_paid_report_inputs(first_path, second_path):
    first = load_validated_customer_json(first_path, "First input")
    second = load_validated_customer_json(second_path, "Second input")
    return first, second