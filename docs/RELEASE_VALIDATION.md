# Public release validation — 25 October 2026

Version: **0.3.0-alpha.1** (`0.3.0a1` in the API). The clean release is derived from working application
snapshot `611bb52198eb817c1a56b5586ff6acdb65c8c1db`.

## What was preserved

- Thirteen critical musical source/data files are byte-identical, including both compilers, the plan schema,
  rule planner, songwriter, lyric craft, song/section planning, presets, instrument vocabulary and queue worker.
- All function/class ASTs in the engine harness are unchanged. Its path configuration now honors
  `RAAG_TOOLS_DIR` and defaults to the public checkout's `runtime/` folder.
- The twelve saved showcase plans compile into exactly the original engine request objects: caption, lyrics,
  metadata, fixed seed, checkpoint/profile, duration, tempo/meter targets, shift, steps and LM settings.
- Original request file hashes and all twelve MP3 hashes match. No sample was regenerated or replaced for release.
- All 597 installed ACE Python source files match the upstream Git blobs at the pinned source revision
  `ca1e85fe9430179831e6bc6be790c332190a3866`.

The source/hash evidence is in [quality_baseline.json](quality_baseline.json). The permanent musical request
regressions live in `app/tests/test_release_quality.py`; intended future musical changes must update their
evidence deliberately.

## Checks performed locally

| Check | Result |
| --- | --- |
| Fresh Python 3.12 app environment | Installed from pinned requirements; dependency check clean |
| Complete Python/integration suite before final startup guard | **622 passed**, 214.43 s; tests use fake audio, no real render/provider call |
| Final startup + release/installer regression checks | **17 passed**, including refusal of an unrelated HTTP listener on the requested port |
| Independent Node browser-logic run | **33 passed**, zero failures |
| Shell scripts / installer syntax | `sh -n` and Python compilation passed |
| Engine installer plan | Read-only mode tested; existing-runtime refusal tested |
| Real installed-engine preflight | MPS available, required core weights present, FFmpeg/FFprobe available, queue idle |
| Twelve original requests | All pass dry-run validation with the actual installed ACE Python/source/weights |
| Running app | Root interface and system, genre, instrument, settings and OpenAPI routes checked; real engine mode, Basic planner |
| Browser verification | Fresh app rendered correctly with a representative brief; actual screenshot included |
| Release scope / links / samples | Checked by `scripts/check_release.py` before publishing |

The suite reports one upstream Starlette TestClient deprecation warning for HTTPX. It does not affect these
passing checks; replacing the test client is a future dependency-maintenance task.

Hosted Linux CI exposed a test fixture that assumed the optional Claude executable was installed while
simulating an authentication failure. The fixture now stubs executable discovery as well as transport, so it
tests the intended fallback without a CLI installation or provider call. Application/musical code is unchanged.

## Recorded audio evidence

The previous local fixed-seed batch rendered twelve of twelve takes successfully, one attempt per brief with
no retries. It produced 24:30 of requested audio in 7:08 including file checks/copies, with 5:41 combined engine
subprocess time. Hardware: M5 Pro, 48 GB unified memory. All native files decoded at their requested duration,
48 kHz stereo; no full-scale clipping was found. The listening copies measured -16.27 to -16.25 LUFS, with
highest true peak -1.77 dBTP. Track 4 crossed the 5% quiet-duration warning threshold.

See the [showcase](../showcase/diverse12_2026-10-25/README.md) and its
[measurement manifest](../showcase/diverse12_2026-10-25/manifest.json). Private native audio/engine logs remain
with the original development run and are not part of this repository.

## Limits of this validation

No new real take, paid call or weight download was needed to package the public release. Therefore this is
request/source equivalence evidence, **not** a new musical preference test or a promise of byte-identical
waveforms across computers.

The opt-in installer pins the observed source, core weights and known engine dependencies. A complete
multi-GB installation from nothing on a second Mac has **not** been performed. It is documented as a separate
validation task rather than claimed as completed. Lower-memory Macs, other operating systems, LM and XL
profiles need their own real-generation evaluation.

Human musical ratings remain pending. Hindi diction, duet separation, rap flow, genre, meter and melody
adherence cannot be certified by technical checks. This showcase does not establish a general shift3 advantage.
