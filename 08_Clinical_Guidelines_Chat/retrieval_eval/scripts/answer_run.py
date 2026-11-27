"""Run benchmark questions through the real app (planner, retrieval, answer, validation) and record everything.

usage: python3 answer_run.py APP_DIR REVISED_QUESTIONS OUT.jsonl [--ids Q001,Q005] [--label X]
Resumes: questions already in OUT.jsonl are skipped. Settings come from APP_DIR/.env and the environment.
Each line: id, question, label, settings, answer blocks, references, notices, kind/mode, error, seconds,
the retrieved chunk ids, every model call (name, input/output tokens) and every rejected attempt with its reason.
"""
import argparse, json, os, sys, time
ap = argparse.ArgumentParser()
ap.add_argument('app_dir'); ap.add_argument('revised'); ap.add_argument('out')
ap.add_argument('--ids', default=''); ap.add_argument('--label', default='')
args = ap.parse_args()
sys.path.insert(0, args.app_dir)
import app  # noqa: E402

calls = []
tokens = []
real_log = app._log_ollama_token_usage
def logged_tokens(call, model, input_tokens, output_tokens=None):
    if call != 'embed':
        tokens.append({'call': call, 'in': input_tokens, 'out': output_tokens})
    return real_log(call, model, input_tokens, output_tokens)
app._log_ollama_token_usage = logged_tokens
real_llm = app.llm_json
def logged_llm(instructions, content, schema, name):
    entry = {'name': name, 'retry_reason': content.get('previous_answer_error') if isinstance(content, dict) else None}
    t = time.time()
    try:
        result = real_llm(instructions, content, schema, name)
        entry['ok'] = True
        if name == 'guideline_answer':
            entry['raw_blocks'] = result.get('blocks')
            if getattr(app, '_EXP', {}).get('key_facts') is not None:
                entry['key_facts'] = app._EXP.pop('key_facts')
        return result
    except Exception as exc:
        entry['ok'] = False; entry['error'] = str(exc)[:300]
        raise
    finally:
        entry['seconds'] = round(time.time() - t, 2)
        calls.append(entry)
app.llm_json = logged_llm

done = set()
if os.path.exists(args.out):
    done = {json.loads(l)['id'] for l in open(args.out, encoding='utf-8') if l.strip()}
want = set(filter(None, args.ids.split(',')))
settings = {k: os.environ.get(k) for k in ('LLM_MODEL', 'LLM_NUM_CTX', 'LLM_NUM_PREDICT', 'RETRIEVAL_TOP_K',
            'RETRIEVAL_EXPANSION', 'RETRIEVAL_MODE', 'AMENDMENT_SCORE_MARGIN', 'RETRIEVAL_EXPANSION_HITS')}
app.build_index()
with open(args.out, 'a', encoding='utf-8') as fh:
    for line in open(args.revised, encoding='utf-8'):
        q = json.loads(line)
        if q['id'] in done or (want and q['id'] not in want):
            continue
        calls.clear(); tokens.clear()
        t = time.time()
        rec = {'id': q['id'], 'question': q['question'], 'label': args.label, 'settings': settings}
        try:
            res = app.answer({'question': q['question'], 'program': 'All programs', 'history': [], 'include_drafts': True})
            rec.update(kind=res.get('kind'), mode=res.get('mode'), blocks=res.get('blocks'),
                       references=res.get('references'), notices=res.get('notices'), message=res.get('message'),
                       sources=[{'n': i, 'chunk_id': s.get('chunk_id'), 'type': s.get('type'),
                                 'tokens': s.get('approx_tokens')} for i, s in enumerate(res.get('sources', []), 1)])
        except Exception as exc:
            rec['error'] = f'{type(exc).__name__}: {exc}'[:500]
        if getattr(app, '_EXP', {}).get('verify') is not None:
            rec['verify'] = app._EXP.pop('verify')
        rec['seconds'] = round(time.time() - t, 1)
        rec['calls'] = list(calls)
        rec['tokens'] = list(tokens)
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n'); fh.flush()
        print(q['id'], rec['seconds'], 's', rec.get('kind') or rec.get('error', '')[:80], flush=True)
