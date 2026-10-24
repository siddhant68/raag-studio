"""Preserve the twelve real showcase requests across public-release packaging.

These compare compiled musical behaviour with saved requests from actual renders;
they do not render audio, judge taste or assume byte-identical rerenders.
"""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend import compiler, song_compiler
from backend.plan_schema import Plan

ROOT = Path(__file__).resolve().parents[2]
SHOW = ROOT / "showcase/diverse12_2026-10-25"
MANIFEST = json.loads((SHOW / "manifest.json").read_text())


@pytest.mark.parametrize("take", MANIFEST["takes"], ids=lambda t: f"{t['n']:02d}")
def test_saved_real_showcase_plan_compiles_to_the_identical_request(take):
    request_file = SHOW / take["request"]
    saved = json.loads(request_file.read_text())
    plan = Plan.model_validate_json((request_file.parent / "plan.json").read_text())
    compiled = song_compiler.compile_song(plan, engine_profile="shift3")
    rebuilt = compiler.to_engine_request(compiled, [take["seed"]], audio_format="flac", meta=saved["meta"])
    block = song_compiler.model_block(compiled)
    if block:
        rebuilt["model"] = block
    assert rebuilt == saved
    assert hashlib.sha256(request_file.read_bytes()).hexdigest() == take["request_sha256"]
    assert (compiled["caption"] + "\n") == (request_file.parent / "caption.txt").read_text()
    assert saved["params"]["shift"] == 3.0
    assert saved["params"]["inference_steps"] == 8
    assert saved["params"]["thinking"] is False
    assert not saved.get("model", {}).get("lm")


def test_runtime_override_reaches_the_harness_without_importing_torch(monkeypatch, tmp_path):
    monkeypatch.setenv("RAAG_TOOLS_DIR", str(tmp_path / "compatible-engine"))
    path = ROOT / "app/engine/run_takes.py"
    spec = importlib.util.spec_from_file_location("release_harness", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.DEFAULT_ENGINE == tmp_path / "compatible-engine/ace-step-1.5"
    assert "torch" not in mod.__dict__


def test_completed_showcase_prepare_never_requests_new_lyrics(monkeypatch, tmp_path):
    import shutil
    from experiments import showcase
    def refuse_new_calls():
        raise AssertionError("Completed public samples must never make new songwriter calls")
    monkeypatch.setattr(showcase, "default_planner", refuse_new_calls)
    scratch = tmp_path / "show"
    shutil.copytree(SHOW / "takes", scratch / "takes")
    before = {p.relative_to(scratch): p.read_bytes() for p in scratch.rglob("*.json")}
    result = showcase.prepare(showcase.load_spec(), show_dir=scratch, runs_dir=tmp_path / "runs")
    assert len(result["prepared"]) == 12
    assert all(state == "kept (already rendered)" for _, state in result["prepared"])
    assert all((scratch / rel).read_bytes() == content for rel, content in before.items())
