#!/bin/sh
# Install only the lightweight app dependencies. Never downloads music models.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHON=${PYTHON:-python3.12}
command -v "$PYTHON" >/dev/null 2>&1 || {
  echo "Python 3.12 is required. On macOS: brew install python@3.12" >&2
  exit 1
}
"$PYTHON" -c 'import sys; assert sys.version_info[:2] == (3, 12), "Use Python 3.12"'
if [ ! -x "$ROOT/app/.venv/bin/python" ]; then
  "$PYTHON" -m venv "$ROOT/app/.venv"
fi
"$ROOT/app/.venv/bin/python" -m pip install -r "$ROOT/app/requirements.lock"
mkdir -p "$ROOT/data" "$ROOT/runs"
echo "App dependencies ready. See docs/INSTALLATION.md for the separate ACE engine setup."
echo "No models were downloaded. Start with: ./scripts/start.sh"
