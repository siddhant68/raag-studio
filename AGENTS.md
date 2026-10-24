# Raag Studio

Raag Studio is a local music application. Start with README.md and docs/ARCHITECTURE.md.

- Application: app/. Operational scripts: scripts/. User data: data/. Generated audio: runs/.
- Preserve the musical pipeline unless a task explicitly calls for a musical change. Caption compilation, lyric preservation, presets, seeds and engine profiles have regression coverage.
- A prompt target is not a verified property of the performance. Keep musical judgments separate from decoding/loudness checks.
- Never overwrite a favourite or an existing native render. Preserve request/result provenance.
- Reuse configured ACE runtimes read-only. App dependencies belong in app/.venv; optional new engine installations belong in runtime/.
- Check MPS, disk and generation queues before real renders. Run one heavy job at a time. CPU fallback is deliberately disabled.
- Tests use a clearly labelled fake engine and temporary storage; do not present their audio as generated music.
- Smart planners are optional and disabled by default. Never enable a provider or make paid calls during tests.
- Do not commit keys, databases, model weights, native renders, personal logs or research archives.
- Run the relevant tests after edits. Changes affecting the song pipeline must pass tests/test_release_quality.py and the complete suite.
