# Architecture

Raag Studio separates the musical idea, its compiled request and the performance that comes back.

```text
Browser (app/web)
    │ local HTTP / server-sent events
FastAPI (app/backend/main.py)
    ├── Basic rules or opt-in planner → schema-validated plan + provenance
    ├── presets + song blueprint → prioritized caption + tagged lyrics
    ├── SQLite library → songs, revisions, rounds, jobs, takes, feedback
    └── one queue worker → resource gates → engine subprocess
                                           │
                              ACE Python / MPS / MLX
                                           │
                              native FLAC + result receipt
                                           │
                              checks → previews → exports
```

## Boundaries that matter

- **Planner:** decides structured intent; it does not directly construct an unrestricted engine prompt.
- **Compiler:** applies allow-lists, lyric policy, caption limits, conflict handling and explicit engine profiles.
- **Worker:** owns one generation process at a time, handles job state/cancellation and records resource waits.
- **Engine harness:** validates requests before importing the heavy runtime, requires MPS, records requested and
  effective parameters, and blocks outbound non-loopback TCP connections during rendering.
- **Library:** keeps plan revisions and generated takes distinct. Another take/refinement is a new performance.
- **Audio helpers:** decode, inspect length/format/clipping/silence/loudness, make previews and export whole mixes.

The app environment stays lightweight. ACE has a separate environment and checkpoint installation selected by
`RAAG_TOOLS_DIR`; its dependencies are not imported into the web server.

## Files and provenance

User state belongs in `data/`; generated artifacts belong in `runs/<song>/<round>/`. A successful native take
retains the exact request, seed, engine/checkpoint identity, effective parameters, timing, native audio hash,
engine log and result. Temporary output directories end in `.partial` until the caller finalizes them.

The model's stereo output is the authoritative performance. Prompt presence is not a per-instrument mix fader,
and a requested form is not a measured segmentation. A technical “passed” state means a file was not found
broken by the implemented checks; it is not a listener preference score.

## Public release boundary

The release contains the app, tests, necessary golden request fixtures and selected real sample outputs.
Development handoffs, personal provider scripts, third-party research snapshots, local databases, installed
models and private runtime logs are kept outside the clean repository.
