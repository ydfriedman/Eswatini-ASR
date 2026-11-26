# Retrieval and answer evaluation

Tools for measuring the guideline chat against the 188-question benchmark, and the overnight experiment plan.

| Path | What it is |
|---|---|
| `OVERNIGHT_PLAN.md` | Instructions for the overnight experiment session (setup on macOS, experiments, grading, report). |
| `scripts/` | `rank_eval.py` (ceiling check), `retrieval_eval.py` (passages that reach the model), `score.py`, `planner_run.py` (llama's search queries), `answer_run.py` (full answers with every model call logged). |
| `app_snapshot/guideline_chat/` | The app as received on 25 Nov 2026 (before the review directive), for reproducibility. Not the live app. |
| `results/` | Run outputs and grades. |

The scripts use the app's own code: they import `app.py` from a given folder and replace only the model calls
where noted, so retrieval is measured exactly as the app does it. See `OVERNIGHT_PLAN.md` for commands.
