import os
import pytest

from runrl.config import ClientConfig


def test_config_from_env(monkeypatch):
    monkeypatch.setenv("RUNRL_API_KEY", "rl_test")
    cfg = ClientConfig.from_env()
    assert cfg.api_key == "rl_test"


def test_missing_api_key_raises(monkeypatch):
    monkeypatch.delenv("RUNRL_API_KEY", raising=False)
    from runrl.client import RunRLClient
    from runrl.exceptions import AuthenticationError

    with pytest.raises(AuthenticationError):
        RunRLClient()
