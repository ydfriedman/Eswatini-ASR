#!/bin/zsh
# Retrieval sweep with the recorded planner queries (production path). Run from 08_Clinical_Guidelines_Chat/.
# usage: scripts/sweep.sh LABEL [VAR=value ...]   e.g. sweep.sh topk8 RETRIEVAL_TOP_K=8
set -e
label=$1; shift
P=${PYTHON:-~/.local/venvs/oeval/bin/python}
R=retrieval_eval/results
Q=${QUERIES:-$R/planner_baseline.json}
APP=${APP:-retrieval_eval/work/exp_app}
env EMBED_CACHE=$R/../work/embed_cache.pkl "$@" $P retrieval_eval/scripts/retrieval_eval.py $APP \
  benchmark_review/revised_questions.jsonl benchmark_review/review_data.json $R/ret_$label.json --label "$label $*" \
  --queries $Q 2>&1 | grep -v -E '^\[(Latency|Ollama|Amendment)'
