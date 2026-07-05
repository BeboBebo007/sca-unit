import os

import pytest

from private_server.start_local import (
    EnvironmentConfigurationError,
    load_local_environment,
)


def test_load_local_environment_sets_api_key(tmp_path, monkeypatch):
    monkeypatch.delenv("SCA_UNIT_API_KEY", raising=False)

    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "SCA_UNIT_API_KEY=test-secret-key-0123456789abcdef\n",
        encoding="utf-8",
    )

    load_local_environment(env_file)

    assert os.environ["SCA_UNIT_API_KEY"] == "test-secret-key-0123456789abcdef"


def test_missing_environment_file_is_rejected(tmp_path):
    missing_file = tmp_path / ".env.local"

    with pytest.raises(
        EnvironmentConfigurationError,
        match="does not exist",
    ):
        load_local_environment(missing_file)


def test_missing_api_key_is_rejected(tmp_path, monkeypatch):
    monkeypatch.delenv("SCA_UNIT_API_KEY", raising=False)

    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "OTHER_SETTING=value\n",
        encoding="utf-8",
    )

    with pytest.raises(
        EnvironmentConfigurationError,
        match="SCA_UNIT_API_KEY",
    ):
        load_local_environment(env_file)

def test_weak_api_key_is_rejected(tmp_path, monkeypatch):
    monkeypatch.delenv("SCA_UNIT_API_KEY", raising=False)

    env_file = tmp_path / ".env.local"
    env_file.write_text(
        "SCA_UNIT_API_KEY=weak-key\n",
        encoding="utf-8",
    )

    with pytest.raises(
        EnvironmentConfigurationError,
        match="at least 32 characters",
    ):
        load_local_environment(env_file)
