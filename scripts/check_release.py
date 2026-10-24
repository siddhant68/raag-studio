"""Check tracked/staged release scope, private-data patterns, links and sample hashes.

Read-only. Does not upload data, rewrite Git history, call providers or generate audio.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_ROOTS = {"context_pack", "elevenlabs-rea", "research", "reports", "runtime"}
SECRET_PATTERNS = [
    re.compile(r"sk-ant-(?:api\d+-)?[A-Za-z0-9_-]{35,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"/(?:Users|home)/[^/\s]+/"),
]
REQUIRED = ["README.md", "LICENSE", "NOTICE.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md",
            "docs/INSTALLATION.md", "docs/CONFIGURATION.md", "docs/ARCHITECTURE.md", "docs/CATALOGUE.md",
            "docs/RELEASE_VALIDATION.md", ".github/workflows/tests.yml", "docs/assets/hero.svg", "docs/assets/app.png"]


def main() -> int:
    files = subprocess.check_output(["git", "-C", str(ROOT), "ls-files", "-z"]).decode().split("\0")
    files = [f for f in files if f]
    failures = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"missing release file: {rel}")
    for rel in files:
        p = ROOT / rel
        parts = Path(rel).parts
        if parts[0] in FORBIDDEN_ROOTS or any(x in parts for x in (".venv", "__pycache__")):
            failures.append(f"private/runtime scope tracked: {rel}")
        if p.suffix in (".db", ".sqlite", ".safetensors", ".pt", ".flac", ".wav", ".log"):
            failures.append(f"local/native artifact tracked: {rel}")
        if parts[0] in ("data", "runs") and p.name != "README.md":
            failures.append(f"user state tracked: {rel}")
        if p.suffix in (".py", ".json", ".md", ".sh", ".yml", ".toml", ".txt"):
            content = p.read_text(encoding="utf-8")
            if any(pattern.search(content) for pattern in SECRET_PATTERNS):
                failures.append(f"credential/private-path pattern: {rel}")
            if p.suffix == ".md":
                for link in re.findall(r"\]\(([^)]+)\)", content):
                    target = link.split("#", 1)[0]
                    if not target or "://" in target or target.startswith("mailto:"):
                        continue
                    target = unquote(target.strip("<>"))
                    if not (p.parent / target).exists():
                        failures.append(f"broken local link: {rel} → {target}")
    show = ROOT / "showcase/diverse12_2026-10-25"
    manifest = json.loads((show / "manifest.json").read_text())
    for take in manifest["takes"]:
        for file_key, hash_key in (("request", "request_sha256"), ("audio", "audio_sha256")):
            p = show / take[file_key]
            if hashlib.sha256(p.read_bytes()).hexdigest() != take[hash_key]:
                failures.append(f"sample content changed: {take[file_key]}")
    if len(manifest["takes"]) != 12:
        failures.append("the complete twelve-take showcase is required")
    if failures:
        print("Release audit failed:\n- " + "\n- ".join(failures))
        return 1
    print(f"Release audit passed: {len(files)} tracked files; 12 exact request/audio hashes; local links and scope clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
