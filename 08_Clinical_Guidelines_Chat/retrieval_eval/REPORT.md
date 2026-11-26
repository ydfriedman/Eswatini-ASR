# Overnight evaluation report (in progress)

Branch `overnight-eval-2026-11-25`. This file is updated as runs finish; the summary at the top is written last.

## Setup and decisions

- Machine: Apple M4 (10-core), 16 GB unified memory, macOS 15.6.
- Homebrew is not installed on this Mac and its installer needs an admin password, so Ollama was installed from
  the official GitHub release (`ollama-darwin.tgz` v0.40.18, SHA-256 checked against GitHub's digest, Apple
  Developer ID signed) into `~/.local/opt/ollama`, run as `ollama serve` (no app). Python: the existing
  uv-managed 3.12 (`~/.local/bin/python3.12`), in a venv at `~/.local/venvs/oeval`. The system Python is 3.9.
- App: `retrieval_eval/app_snapshot/guideline_chat` (the updated app, 26 Nov, review directive applied), copied to
  `retrieval_eval/work/guideline_chat` with the deployed `.env`. Its 78 tests pass.

## Run log

| Time | Label | What | Result |
|---|---|---|---|
