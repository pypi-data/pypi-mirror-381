import os
from pathlib import Path

from goodgleif.paths import get_writable_dir, default_parquet_path


def test_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("GOODGLEIF_DATA_DIR", str(tmp_path))
    assert get_writable_dir() == tmp_path
    assert default_parquet_path().parent == tmp_path


