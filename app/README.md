# Application source

Read the [project README](../README.md) and [installation guide](../docs/INSTALLATION.md).

- `backend/`: FastAPI, planning, compilation, SQLite library, queue, audio/export helpers.
- `web/`: the browser interface; plain HTML, CSS and JavaScript, with no build step.
- `engine/`: the guarded ACE subprocess harness and an explicitly labelled test engine.
- `genres/`, `recipes/`: musical presets and starting recipes.
- `experiments/`: reproducible showcase and blind listening tools.
- `tests/`: API, queue, planning, lyrics, exports and interface regression tests.

Run tests from the repository root: `app/.venv/bin/python -m pytest -q`.
