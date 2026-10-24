# The musical configuration

Raag Studio's controls describe a musical intention, and the stored plan makes that intention inspectable.
The implementation lives in `app/backend/plan_schema.py`, `planner_base.py`, `song_blueprint.py` and
`song_compiler.py`. This guide distinguishes the browser controls, the richer plan/API and the engine inputs.

## One brief, three layers

1. **Intent:** the brief and your explicit choices. Fields left on Auto are filled from rules, a genre preset,
   an accepted recipe or an optional smart planner.
2. **Musical plan:** a validated schema containing instruments and roles, vocals, lyrics, timing, mood, form
   and provenance. Every field can carry a source (`you`, `suggested`, `recipe`, `rule`) and a reason.
3. **Engine request:** a prioritized caption of at most 512 characters, separately tagged lyrics and typed
   metadata such as duration, BPM, key, meter, seed and profile. The compile report records conflicts and drops.

The Basic planner is a keyword/rule system, labelled as such. Claude can interpret more free-form intent when
you explicitly enable a smart provider. Both feed the same validator and compiler. A smart-provider failure
is surfaced as a labelled fallback; it is not silently described as a successful LLM plan.

## What is available where?

| Choice | Browser | Structured plan / API | Meaning |
| --- | --- | --- | --- |
| Brief | Required text | `brief`, 1–4000 characters | The feeling, setting or musical direction |
| Style | Auto or preset | `genre`, `pipeline` | A musical vocabulary and default form, not an audio filter |
| Voice | Auto, instrumental, wordless, sung | `voice_mode` | How voices should participate |
| Length | Auto and common lengths | `duration_s`, 10–240 | Exact duration requested from the engine and checked after rendering |
| Versions | 1–4 | `takes`, 1–4 | Independent seeded performances, rendered sequentially |
| Starting recipe | Sound I liked | `recipe_id` | Flute focus, warm ensemble, Hindi ballad; an unrated fusion recipe stays hidden by default |
| Lead | Lead picker | `lead.instrument` | The instrument that should carry the musical identity |
| Lead phrasing | Simple, singing, ornate | `lead.style` | Restraint, connected phrasing or ornamented playing |
| Ensemble | Instrument choices | Up to 14 `supports` entries | Named instruments in priority order |
| Supporting jobs | Inferred and shown in plan | Each support has `role` | Rhythm, drone, harmony, answer or texture; a competing lead is resolved by the compiler |
| Presence | Arrangement/fullness choices | Per-support `presence`: sparse, gentle, full | Qualitative prominence, not a gain fader |
| Mood | Feeling choices | Up to 8 `feeling` terms | Colour the arrangement and performance |
| Pace | Slow, medium, lively; tempo override | `pace.bucket`, `pace.bpm` 60–140 | A tempo target, with bucket defaults of 74, 88 and 108 BPM |
| Key | Song-page key override | `key`, e.g. D major or F# minor | An input target; the output is not verified for exact harmony |
| Meter | Inferred/shown in song plan | `meter`: 4/4, 3/4, 6/8, 2/4 | Full meter retained in the plan; ACE receives the supported time-signature metadata |
| Density | Spare, balanced, full | `fullness` | How much accompaniment is requested |
| Energy arc | Story of the piece | `arc`: steady, slow_build, quiet_middle_bloom | How the arrangement should evolve |
| Sections | Song map display | `form`, `require_sections` | Genre-aware form plus explicit required sections |
| Singer | Auto, male, female, duet | `voices.singer` | A vocal assignment request; duet separation requires listening |
| Backing voices | Background-voice options | `voices.background`: none, light, choir, big | Harmonies and choir scale, not exact headcounts |
| Language | Language picker | `voices.language` | Language metadata; Hindi singing remains experimental |
| Lyrics | Write for me / use my words | `lyrics.policy`: none, write, exact | Source-preservation and optional songwriting policy |
| Lyric topic | Brief / song intention | `lyrics.topic` | Subject for original writing with a smart provider |
| Avoid | Advanced input | Up to 10 `avoid` terms | Excluded from compiled direction; not a strong engine negative-prompt guarantee |
| Short musical detail | Brief / plan suggestion | `flavour`, up to 120 characters | A concise extra arrangement or performance direction |
| Refinement | Chips and free text | Plan patches and new rounds | New performances, with an explicit record of changed fields |

The table intentionally includes fields that are available through the plan/API rather than a standalone
browser control. The UI remains approachable; the configuration is still expressive.

## Instruments with jobs

The 56-instrument vocabulary includes Indian melodic and percussion instruments, acoustic ensembles, drums,
brass, keyboards, electronic textures, basses and voices. [Full catalogue](CATALOGUE.md).

For example, the stored plan for **River waking up** contains:

```json
{
  "lead": {"instrument": "bansuri", "style": "singing"},
  "supports": [
    {"instrument": "tanpura", "role": "drone", "presence": "gentle"},
    {"instrument": "tabla", "role": "rhythm", "presence": "sparse"},
    {"instrument": "santoor", "role": "texture", "presence": "sparse"}
  ],
  "duration_s": 120,
  "pace": {"bucket": "slow", "bpm": 78},
  "meter": "4/4",
  "voice_mode": "instrumental"
}
```

This is an excerpt, not a complete API request. The point is the relationship: bansuri leads, tanpura anchors,
tabla supports the pulse and santoor adds occasional colour. The compiler budgets the available caption space
and reports anything that could not fit. The model still has to realise the relationship musically.

## Form and development

Styles carry a typical form and production vocabulary. Song blueprints fit sections to requested tempo and
duration, assign section energy and instrument entrances, and mark hook returns. Available section kinds are:

`intro`, `verse`, `pre_chorus`, `chorus`, `bridge`, `solo`, `interlude`, `break`, `build`, `drop`, `outro`.

Genre-specific names can describe their jobs more naturally: alaap, jor, gat and taans for a bansuri journey;
mukhda and antara for an Indian song; build, drop and breakdown for EDM. Required sections are protected
when fitting the form. These maps are planned structure, not measured timestamps in the generated audio.

## Lyrics and voices

**Use my words:** exact lyrics retain the supplied words and ordering through compilation. They are protected
from LLM rewriting. Tagged sections and an engine language code carry structure; they cannot guarantee every
word will be sung intelligibly.

**Write for me:** an explicitly enabled Claude provider drafts for the section blueprint. The songwriter checks
line length, syllable fit, hook repetition and simple craft concerns, with one bounded revision. These are writing
checks, not a judgment of the generated singer. A song's repeated chorus and its backing choir are separate ideas.

**Duet:** the plan requests perspectives and voice handoffs, and tags can identify who sings. It does not split
the result into independent singer tracks. **Rap:** a style/lyric direction can request conversational verses and
a melodic hook; rap flow and the sung/rap contrast need listening.

## Engine profiles

| Profile | DiT | Shift | Steps | 5Hz LM | Status |
| --- | --- | --- | --- | --- | --- |
| `classic` | ACE-Step 1.5 turbo | 1.0 | 8 | Off | Historical accepted-recipe settings |
| `shift3` | ACE-Step 1.5 turbo | 3.0 | 8 | Off | Default song profile; used for all twelve showcase takes |
| `lm` | ACE-Step 1.5 turbo | 3.0 | 8 | 1.7B, on | Optional separate install; not evaluated in the showcase |
| `xl` | XL turbo | 3.0 | 8 | Off | Optional separate install; not evaluated in the showcase |
| `xl_lm` | XL turbo | 3.0 | 8 | 1.7B, on | Optional separate install; not evaluated in the showcase |

The Settings value `auto` follows the pipeline default. Turbo overrides CFG guidance to **1.0**; the result
records requested and effective settings so an ineffective higher guidance value is not presented as stronger
obedience. The Qwen embedding model remains required with LM off; it is not the 5Hz music planner.

Seeds are recorded for reproducibility. The UI's “Another take” generates another seed and a new performance;
it does not lock the melody or singer. Cross-version numerical/runtime differences can also change the audio.

## What is exact, and what is a target?

| Exact software behaviour | Performance target |
| --- | --- |
| Validated schema, preset selection and provenance | Genre, emotional character and virtuosity |
| Exact text sent for an exact-lyrics request | Diction, intelligibility and sung-word fidelity |
| Checkpoint, seed, steps, shift and LM selection | A repeated melody or unchanged singer in a new take |
| Duration requested; decoded duration checked | Requested BPM, key, meter and section boundaries in the waveform |
| Whole-mix trim, fade, export and loudness processing | Individual instrument loudness and exact ensemble/choir size |

The native output is a stereo performance. Independent faders, score locks and guaranteed phrase repair would
need additional representations or engines. Technical checks detect breakage; listening establishes quality.

## Runtime configuration

Environment variables are read at startup; `.env.example` is reference documentation rather than an executed file.

| Variable | Default / purpose |
| --- | --- |
| `RAAG_TOOLS_DIR` | `runtime/`; contains `acestep-venv/` and `ace-step-1.5/` |
| `RAAG_DATA_DIR` | `data/`; SQLite library and temporary state |
| `RAAG_RUNS_DIR` | `runs/`; native takes, previews, receipts and exports |
| `RAAG_PORT` | `8477`; local server port |
| `RAAG_VIDEO_QUEUE_URL` | `http://127.0.0.1:8388/queue`; competing ComfyUI-job gate |
| `RAAG_SONG_PIPELINE` | `1`; `0` selects the historical classic pipeline for new songs |
| `RAAG_ENGINE` | Unset for real music; `fake` is an explicitly labelled development/test engine |
| `ANTHROPIC_API_KEY` | Optional, only for the explicitly enabled API planner |

Advanced application settings include the minimum free-disk gate (5 GiB), queue depth (5), job timeout (1800 s),
silence warning/failure fractions (5% / 40%), and one retry on technical failure. That retry is a normal-app policy;
the fixed showcase disables retries and counts each brief once. No artistic score triggers a retry.

Keep the server on localhost. See [installation](INSTALLATION.md), [API](API.md) and [security](../SECURITY.md).
