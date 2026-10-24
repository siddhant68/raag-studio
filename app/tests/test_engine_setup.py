"""The engine install plan is pinned, explicit and non-destructive."""
import importlib.util
import json
from pathlib import Path

import pytest

PATH = Path(__file__).resolve().parents[2] / "scripts/setup_engine.py"
spec = importlib.util.spec_from_file_location("engine_setup", PATH)
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)


def test_plan_writes_nothing_and_spawns_nothing(tmp_path, monkeypatch, capsys):
    def refuse(*args, **kwargs):
        raise AssertionError("A plan must never execute a subprocess")
    monkeypatch.setattr(setup.subprocess, "run", refuse)
    target = tmp_path / "new-runtime"
    assert setup.main(["--plan", "--tools-dir", str(target)]) == 0
    data = json.loads(capsys.readouterr().out)
    assert not target.exists()
    assert data["source_revision"] == "ca1e85fe9430179831e6bc6be790c332190a3866"
    assert data["model_revision"] == "19671f406d603126926c1b7e2adc169acbcade22"
    assert data["model_patterns"] == ["acestep-v15-turbo/*", "vae/*", "Qwen3-Embedding-0.6B/*"]


def test_existing_engine_is_never_overwritten(tmp_path, monkeypatch):
    monkeypatch.setattr(setup.platform, "system", lambda: "Darwin")
    monkeypatch.setattr(setup.platform, "machine", lambda: "arm64")
    engine = tmp_path / "ace-step-1.5"
    engine.mkdir()
    marker = engine / "existing.txt"
    marker.write_text("keep")
    def refuse(*args, **kwargs):
        raise AssertionError("Existing runtimes must not be changed")
    monkeypatch.setattr(setup.subprocess, "run", refuse)
    with pytest.raises(SystemExit):
        setup.main(["--yes", "--tools-dir", str(tmp_path)])
    assert marker.read_text() == "keep"
