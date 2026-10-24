# Security and privacy

Raag Studio is an early-access **local, single-user application**. It binds to localhost by default and has
no user-account/authentication layer for internet hosting. Do not expose it with a public bind address,
reverse proxy or tunnel as though it were a hosted multi-user service.

The app enforces local host/origin checks. Render subprocesses block non-loopback TCP and load only installed,
allowed checkpoints. Basic planning is local; optional Claude providers send text to Anthropic under your
configuration. Provider keys are read from the environment, not stored in settings.

Your SQLite library, audio, prompts and logs remain under `data/` and `runs/`. These folders are ignored by Git.
Review bug-report attachments before sharing them: engine logs and plan receipts can contain your lyrics,
briefs, local paths and other material you do not want published.

## Reporting a vulnerability

Use [GitHub private vulnerability reporting](https://github.com/siddhant68/raag-studio/security/advisories/new).
Describe the affected revision, impact and a minimal reproduction. Do not post credentials or an exploitable
security issue in a public issue. The latest early-access revision is the current maintenance target; no
guaranteed response-time or long-term support policy is offered yet.
