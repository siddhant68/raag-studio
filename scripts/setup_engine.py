"""Explicitly install a pinned ACE engine into a fresh, separate local runtime.

--plan is read-only. --yes opts into downloading source, dependencies and core weights.
Existing source/environment folders are never upgraded, replaced or deleted.
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://github.com/ace-step/ACE-Step-1.5.git"
SOURCE_REVISION = "ca1e85fe9430179831e6bc6be790c332190a3866"
MODEL_REPO = "ACE-Step/Ace-Step1.5"
MODEL_REVISION = "19671f406d603126926c1b7e2adc169acbcade22"
PATTERNS = ["acestep-v15-turbo/*", "vae/*", "Qwen3-Embedding-0.6B/*"]


def plan(tools: Path) -> dict:
    return {
        "tools_dir": str(tools), "source_url": SOURCE_URL, "source_revision": SOURCE_REVISION,
        "model_repo": MODEL_REPO, "model_revision": MODEL_REVISION, "model_patterns": PATTERNS,
        "engine_python": str(tools / "acestep-venv/bin/python"),
        "requirements": str(ROOT / "requirements-engine-macos.txt"),
        "needs": "Apple Silicon macOS, Python 3.12, Git, FFmpeg, at least 25 GiB free",
        "downloads": "source, Python dependencies, turbo DiT, VAE and Qwen embedding; no 5Hz LM or XL",
        "modifies_existing_runtime": False,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tools-dir", type=Path, default=ROOT / "runtime")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--plan", action="store_true", help="print the download plan, write nothing (default)")
    mode.add_argument("--yes", action="store_true", help="install into fresh folders; downloads several GB")
    args = ap.parse_args(argv)
    tools = args.tools_dir.expanduser().resolve()
    details = plan(tools)
    print(json.dumps(details, indent=2))
    if not args.yes:
        return 0
    if sys.version_info[:2] != (3, 12):
        ap.error("use Python 3.12")
    if platform.system() != "Darwin" or platform.machine() != "arm64":
        ap.error("this pinned installer supports Apple Silicon macOS only")
    source, env = tools / "ace-step-1.5", tools / "acestep-venv"
    if source.exists() or env.exists():
        ap.error("engine/source folders already exist; refusing to upgrade or overwrite them. "
                 "Reuse the installation with RAAG_TOOLS_DIR, or select a new --tools-dir.")
    for command in ("git", "ffmpeg", "ffprobe"):
        if shutil.which(command) is None:
            ap.error(f"{command} is required; install it first")
    ancestor = tools
    while not ancestor.exists():
        ancestor = ancestor.parent
    if shutil.disk_usage(ancestor).free < 25 * 2**30:
        ap.error("at least 25 GiB free is required for installation")
    tools.mkdir(parents=True, exist_ok=True)
    # Each command has fixed arguments and a fresh destination; no shell or destructive checkout.
    subprocess.run(["git", "init", str(source)], check=True)
    subprocess.run(["git", "-C", str(source), "remote", "add", "origin", SOURCE_URL], check=True)
    subprocess.run(["git", "-C", str(source), "fetch", "--depth", "1", "origin", SOURCE_REVISION], check=True)
    subprocess.run(["git", "-C", str(source), "checkout", "--detach", "FETCH_HEAD"], check=True)
    subprocess.run([sys.executable, "-m", "venv", str(env)], check=True)
    python = env / "bin/python"
    subprocess.run([str(python), "-m", "pip", "install", "-r", str(ROOT / "requirements-engine-macos.txt")],
                   check=True)
    download = (
        "import json,sys; from huggingface_hub import snapshot_download; "
        "snapshot_download(repo_id=sys.argv[1],revision=sys.argv[2],local_dir=sys.argv[3],"
        "allow_patterns=json.loads(sys.argv[4]))"
    )
    download_env = {k: v for k, v in os.environ.items() if k not in ("HF_HUB_OFFLINE", "TRANSFORMERS_OFFLINE")}
    subprocess.run([str(python), "-c", download, MODEL_REPO, MODEL_REVISION,
                    str(source / "checkpoints"), json.dumps(PATTERNS)], check=True, env=download_env)
    (tools / "installation.json").write_text(json.dumps(details, indent=2) + "\n")
    checked = subprocess.run([sys.executable, str(ROOT / "scripts/preflight.py"), "--json"],
                             env={**os.environ, "RAAG_TOOLS_DIR": str(tools)})
    print("Engine installation retained at:", tools)
    print("Set RAAG_TOOLS_DIR to this folder before starting the app.")
    return checked.returncode


if __name__ == "__main__":
    raise SystemExit(main())
