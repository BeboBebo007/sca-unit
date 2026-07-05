import os
from pathlib import Path

from private_server.api import run_local_service


class EnvironmentConfigurationError(RuntimeError):
    """Raised when the local environment file is invalid."""


def load_local_environment(
    file_path: str | Path = ".env.local",
) -> None:
    path = Path(file_path)

    if not path.exists():
        raise EnvironmentConfigurationError(
            f"Environment file does not exist: {path}"
        )

    if not path.is_file():
        raise EnvironmentConfigurationError(
            f"Environment path is not a file: {path}"
        )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" not in line:
            raise EnvironmentConfigurationError(
                f"Invalid environment entry: {line}"
            )

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            raise EnvironmentConfigurationError(
                "Environment variable name must not be empty"
            )

        os.environ[key] = value

    if not os.environ.get("SCA_UNIT_API_KEY", "").strip():
        raise EnvironmentConfigurationError(
            "SCA_UNIT_API_KEY is not configured"
        )


def main() -> None:
    load_local_environment()
    run_local_service()


if __name__ == "__main__":
    main()