# Contributing

Thanks for helping build Raag Studio. Good contributions make music creation clearer, more reliable or more
expressive without obscuring what the model can actually do.

1. Open an issue for a substantial change and describe the user problem.
2. Fork the repository, create a focused branch and follow [development setup](docs/DEVELOPMENT.md).
3. Keep the patch small enough to review. Add regression coverage for changed behaviour.
4. Run the full Python suite, Node UI tests and `scripts/check_release.py` before opening a pull request.
5. Include what changed, why and how you verified it. For a musical change, separate software checks from
   listening results and include the relevant settings/seed where sharing is permitted.

## Working principles

- Preserve exact supplied lyrics, previous takes and favourites.
- Name the real planner and engine. Make fallbacks visible.
- Treat tempo, meter, arrangement and diction as targets until evaluated in the audio.
- Keep heavy model environments separate; never upgrade a shared runtime casually.
- Prefer local defaults. External text providers stay optional and explicitly enabled.
- Do not add generated tracks to a PR without the input/provenance needed to review them.
- Never include credentials, personal libraries, installed models or private logs.

Useful areas: installation on additional Macs, accessibility, lyric delivery evaluation, reproducible presets,
resource handling and independently tested platform support. See the [roadmap](docs/ROADMAP.md).

By contributing, you agree that your contribution can be distributed under the project's MIT license.
Be considerate and specific in reviews. Discuss the work; respect the people doing it.
