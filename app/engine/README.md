# Engine harness

`run_takes.py` validates a text-to-music request, then renders its explicit seeds sequentially through
ACE-Step 1.5. It requires MPS and uses the installed Apple Silicon engine, including its native MLX DiT path.
The web server does not import the heavy engine dependencies.

Read the [request contract](REQUEST_CONTRACT.md), [configuration guide](../../docs/CONFIGURATION.md) and
[installation guide](../../docs/INSTALLATION.md).

```sh
export RAAG_TOOLS_DIR="$PWD/runtime"
python3.12 scripts/preflight.py --json
"$RAAG_TOOLS_DIR/acestep-venv/bin/python" app/engine/run_takes.py request.json runs/example.partial --dry-run
```

Omit `--dry-run` only for an intended real generation after checking resources. `OUT_DIR` must be fresh,
its parent must exist and its name must end in `.partial`. The caller renames it after exit 0 and a `done` event.
Never overwrite an existing take or delete a partial directory merely to force a retry.

The harness records the request hash, seed, requested/effective parameters, checkpoint, device, timing,
checkpoint-listing comparison and outbound network-attempt record. Library output goes to `engine.log`;
JSON events stay on stdout. Missing weights are an error, and CPU fallback is refused.

Core weights are installed separately. An in-process guard prevents ACE from treating an absent optional
5Hz LM as an invitation to download; non-loopback outbound TCP is blocked during rendering. Source files and
checkpoints are reused read-only. `fake_engine.py` is an explicitly labelled integration-test signal generator.
