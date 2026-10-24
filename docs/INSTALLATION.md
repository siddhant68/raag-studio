# Installation

## Supported setup

The real render path targets **Apple Silicon macOS** with **Python 3.12**, MPS, the pinned ACE-Step 1.5 turbo
engine and FFmpeg/FFprobe. The recorded validation machine is an M5 Pro MacBook Pro with 48 GB unified memory.
Smaller memory configurations and real generation on Linux, Windows or CPU are not validated by this release.
The CPU-only test suite does not need the model or Apple hardware.

Allow at least 25 GiB of free space for a new engine environment, core weights and operating headroom; output
and swap can require more. The runtime's 5 GiB free-disk gate is an emergency floor, not a complete install estimate.
Plug in the Mac and run one heavy generation job at a time.

## 1. Install the app

```sh
git clone https://github.com/siddhant68/raag-studio.git
cd raag-studio
brew install python@3.12 ffmpeg
./scripts/setup.sh
```

This creates `app/.venv` and installs the pinned lightweight app environment from `app/requirements.lock`. There is no frontend build and
no model download at this stage. The setup script changes only this checkout's app environment.

## 2. Install the engine, or reuse one

### New engine

```sh
python3.12 scripts/setup_engine.py --plan
python3.12 scripts/setup_engine.py --yes
export RAAG_TOOLS_DIR="$PWD/runtime"
```

The plan command prints the exact source, model revisions and destination without writing them. `--yes`
explicitly downloads the pinned source, installs the separately pinned engine dependencies in a new environment,
and downloads only the turbo DiT, VAE and Qwen embedding weights. No 5Hz LM or XL weights are included.

The installer refuses existing engine/source directories instead of upgrading or replacing them. An interrupted
installation remains on disk for inspection. It never deletes or resets a runtime. Fresh-machine engine
installation is separate from the working-engine validation: see [release validation](RELEASE_VALIDATION.md).

Expected layout:

```text
runtime/
├── acestep-venv/bin/python
└── ace-step-1.5/
    ├── acestep/
    └── checkpoints/
        ├── acestep-v15-turbo/
        ├── vae/
        └── Qwen3-Embedding-0.6B/
```

The source revision is `ca1e85fe9430179831e6bc6be790c332190a3866`; the core-weight revision is
`19671f406d603126926c1b7e2adc169acbcade22`. The source is from the official
[ACE-Step repository](https://github.com/ace-step/ACE-Step-1.5/tree/ca1e85fe9430179831e6bc6be790c332190a3866).
Upstream's [installation guide](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md)
provides broader platform context; Raag Studio's tested path remains the one described here.

### Existing compatible engine

```sh
export RAAG_TOOLS_DIR="/absolute/path/to/your/tools"
python3.12 scripts/preflight.py --json
```

The folder must contain `acestep-venv/bin/python` and `ace-step-1.5/checkpoints/` in the layout above.
Do not run the installer over an existing shared runtime. Rendering reads that installation; it does not
download weights or upgrade packages. Use the pinned source and dependency versions for the closest match to
the included samples. Different runtimes can produce different numerical results with the same seed.

## 3. Check and start

```sh
python3.12 scripts/preflight.py --json
./scripts/start.sh
open http://127.0.0.1:8477
```

Require `mps: true`, all required checkpoints, FFmpeg and adequate free disk. A busy ComfyUI queue on port
8388 must finish before a music job starts. An unknown queue state should be investigated rather than treated
as evidence of an idle machine. The engine refuses CPU fallback.

Stop the server using `./scripts/stop.sh`. Its PID and log are stored under `data/`. Keep the server bound to
localhost; this release is a local single-user application, with no account/authentication layer for hosting.

## 4. Your first session

1. Enter a brief, such as “A peaceful bansuri at dawn, gentle tabla, no singing, about two minutes.”
2. Leave the optional controls on Auto, or choose a style, instruments, voice, length and number of takes.
3. Press Create to build the plan and queue rendering; inspect the musical plan on the song page.
4. Compare the takes, favourite the ones you like, then export MP3 or WAV.

The Basic planner runs locally. It cannot write original lyrics; supply your own text or enable an optional
Claude provider in Settings. Smart-provider calls use your account and may incur provider charges. API keys
come from the environment and are never saved in the app settings.

## Optional profiles

The default song profile is turbo, shift 3.0, eight steps, no 5Hz LM. Existing classic recipes retain their
historical profile. To explicitly install additional models after reviewing their size:

```sh
app/.venv/bin/python scripts/fetch_models.py lm
app/.venv/bin/python scripts/fetch_models.py xl
```

These commands ask before downloading; render jobs never fetch models. Change profiles in Settings once
the models exist. These optional models were not evaluated in the included twelve-song trial.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| App venv missing | Run `./scripts/setup.sh` with Python 3.12 |
| ACE Python missing | Inspect `RAAG_TOOLS_DIR` and the required folder layout |
| MPS unavailable | Use a native Apple Silicon Python process; check PyTorch's MPS support; CPU fallback is intentionally refused |
| Missing checkpoint | Inspect preflight's per-file results; install explicitly rather than allowing a render-time fetch |
| Job waiting for resources | Finish competing video/image renders; inspect queue state and disk; do not stop unrelated services |
| Smart lyrics unavailable | Enable/configure a smart planner, or provide exact lyrics |
| Provider cannot answer | Read the labelled fallback/reason; check the selected provider's current setup |
| Port already used | Set `RAAG_PORT=8488` before starting; use the corresponding URL |
| Network proxy errors in tests | Tests use local HTTP clients; avoid inheriting an unsupported SOCKS proxy into the test process |
| Lots of swapping | Stop overlapping heavy jobs; use the base turbo profile and inspect memory/disk; lower-memory Macs remain unvalidated |

Back up `data/raag.db` together with `runs/`. Do not copy or publish API keys, server logs or a personal library
when sharing a bug report. [Security and privacy](../SECURITY.md).
