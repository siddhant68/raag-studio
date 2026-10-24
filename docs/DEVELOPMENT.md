# Development

Python 3.12, FFmpeg/FFprobe and Node.js 22+ cover the app's automated tests. No model weights, API key or GPU
are needed. Node is used for the browser logic tests; the interface has no npm build.

```sh
./scripts/setup.sh
app/.venv/bin/python -m pytest -q
node --test app/tests/js/logic.test.mjs
python3.12 scripts/check_release.py
```

Tests create temporary SQLite databases and fake-engine artifacts. `RAAG_ENGINE=fake` is deliberately labelled
through the API/UI and produces test signals, not real music. Do not enable a smart planner or run a real engine
as part of CI. The suite covers plan validation, exact lyrics, compilation, presets, API state, queue behaviour,
cancellation, export, favourites and pure UI logic.

To develop the interface without an engine installation:

```sh
RAAG_ENGINE=fake RAAG_PORT=8488 ./scripts/start.sh
```

Use a separate data directory if you also have a personal app instance running. Stop with `./scripts/stop.sh`.

## Musical changes

The fixed release plans are regression fixtures. `test_release_quality.py` recompiles all twelve against their
saved engine requests, including the exact words, captions, seeds, profile and metadata. A deliberate change
that updates those fixtures must explain the musical intent and include before/after evidence.

Automated checks cannot establish that one melody, pronunciation or arrangement is better. Use the blind-sheet
tools under `app/experiments/` for a separately authorized listening trial. Keep seeds/briefs constant when
isolating a setting. Preserve previous favourites and native outputs; do not silently cherry-pick samples.
