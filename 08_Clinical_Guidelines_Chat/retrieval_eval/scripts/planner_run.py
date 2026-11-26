"""Collect the real planner output (route + search queries) from the deployed model for each benchmark question.
Calls the app's own planner step in ai_answer() with the real model, then stops before retrieval.

usage: python3 planner_run.py APP_DIR REVISED_QUESTIONS OUT.json   (resumes if OUT.json exists)
"""
import json, os, sys, time
sys.path.insert(0, sys.argv[1])
import app  # noqa: E402

os.environ.setdefault('LLM_MODEL', 'llama3.1:8b')
out_path = sys.argv[3]
done = json.load(open(out_path)) if os.path.exists(out_path) else {}
real_llm = app.llm_json

class Stop(Exception):
    pass

record = {}
def planner_only(instructions, content, schema, name):
    if name == 'retrieval_queries':
        result = real_llm(instructions, content, schema, name)
        record.setdefault('calls', []).append(result)
        if result.get('route') == 'answer' and [q for q in result.get('queries', []) if q.strip()]:
            raise Stop()
        return result
    raise Stop()
app.llm_json = planner_only

for line in open(sys.argv[2], encoding='utf-8'):
    q = json.loads(line)
    if q['id'] in done:
        continue
    record.clear()
    t = time.time()
    try:
        res = app.ai_answer(q['question'], [], 'All programs', True)
        routed = res.get('kind')
    except Stop:
        routed = None
    except Exception as exc:   # keep going; record the failure
        routed = 'error: ' + str(exc)[:200]
    calls = record.get('calls', [])
    done[q['id']] = {'calls': calls, 'routed': routed, 'seconds': round(time.time() - t, 1)}
    json.dump(done, open(out_path, 'w'), indent=1)
    print(q['id'], done[q['id']]['seconds'], 's', calls[-1].get('route') if calls else routed,
          (calls[-1].get('queries') if calls else ''), flush=True)
