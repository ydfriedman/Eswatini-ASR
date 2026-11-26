"""Make the experiment copy of the app: the same code with environment switches for the overnight experiments.

usage: python3 make_exp_app.py SRC_APP_DIR DST_APP_DIR
Every switch defaults to the app's own behaviour, so with no EXP_* variables set the copy behaves exactly like the
source (checked by comparing retrieval runs). Switches:
  EXP_DOC_CAP (3), EXP_PAGE_CAP (2)          per-document / per-page caps in search()
  EXP_KW_LIMIT (40), EXP_RRF_K (60), EXP_KW_WEIGHT (1.0)   hybrid fusion inside search()
  EXP_RERANK (off), EXP_RERANK_N (30), EXP_RERANK_MAXLEN (512), EXP_RERANK_QUERY (query|question)
  EXP_RAW_QUESTION (1)                       add the user's question as a search query
  EXP_MAX_QUERIES (3)                        planner queries used
  EXP_FOLLOWUP_APPEND (1)                    append the previous user question for short follow-ups
"""
import shutil, sys
from pathlib import Path

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '.env'))
if (src / '.env').exists():
    shutil.copy(src / '.env', dst / '.env')
path = dst / 'app.py'
code = path.read_text(encoding='utf-8')

def sub(old, new, count=1):
    global code
    assert code.count(old) == count, (old, code.count(old))
    code = code.replace(old, new)

def env_int(name, default):
    return f"int(os.environ.get('{name}', '{default}'))"

# --- ai_answer(): query construction
sub("    search_queries = list(queries[:3])\n    if question not in search_queries:",
    f"    _EXP['question'] = question\n    search_queries = list(queries[:{env_int('EXP_MAX_QUERIES', 3)}])\n"
    "    if os.environ.get('EXP_RAW_QUESTION', '1') == '1' and question not in search_queries:")
sub("    if previous_user_question and len(question.split()) <= 12:",
    "    if os.environ.get('EXP_FOLLOWUP_APPEND', '1') == '1' and previous_user_question and len(question.split()) <= 12:")
# --- search(): hybrid fusion
sub("        fused = {row[0]: 1 / (60 + position) for position, (_, row) in enumerate(ranked, 1)}\n"
    "        for position, chunk_id in enumerate(keyword_ranking(question, allowed), 1):\n"
    "            if chunk_id in fused:\n"
    "                fused[chunk_id] += 1 / (60 + position)",
    f"        _k = {env_int('EXP_RRF_K', 60)}; _w = float(os.environ.get('EXP_KW_WEIGHT', '1.0'))\n"
    "        fused = {row[0]: 1 / (_k + position) for position, (_, row) in enumerate(ranked, 1)}\n"
    f"        for position, chunk_id in enumerate(keyword_ranking(question, allowed, limit={env_int('EXP_KW_LIMIT', 40)}), 1):\n"
    "            if chunk_id in fused:\n"
    "                fused[chunk_id] += _w / (_k + position)")
# --- search(): optional cross-encoder rerank of the top candidates, before caps and dedup
sub("    # 4) Skip duplicates and diversify the retrieved passages.\n",
    "    if os.environ.get('EXP_RERANK', '') == '1':\n"
    "        ranked = _exp_rerank(question, ranked)\n"
    "    # 4) Skip duplicates and diversify the retrieved passages.\n")
sub("        if doc_counts.get(doc_id, 0) >= 3 or page_counts.get(page_key, 0) >= 2:",
    f"        if doc_counts.get(doc_id, 0) >= {env_int('EXP_DOC_CAP', 3)} or page_counts.get(page_key, 0) >= {env_int('EXP_PAGE_CAP', 2)}:")

# --- search(): number of hits each search returns (default: RETRIEVAL_TOP_K)
sub("    # 4) Skip duplicates and diversify the retrieved passages.\n    limit = answer_source_limit()\n",
    "    # 4) Skip duplicates and diversify the retrieved passages.\n"
    "    limit = int(os.environ.get('EXP_SEARCH_K') or answer_source_limit())\n")
# --- ai_answer(): optional final rerank of the fused hit pool against the user's question
sub("    ranked_items = sorted(fused.values(), key=lambda item: item['score'], reverse=True)\n",
    "    ranked_items = sorted(fused.values(), key=lambda item: item['score'], reverse=True)\n"
    "    if os.environ.get('EXP_RERANK_FINAL', '') == '1':\n"
    "        ranked_items = _exp_rerank_final(question, ranked_items)\n")

# --- llm_json(): temperature
sub("'options': {'temperature': 0,", "'options': {'temperature': float(os.environ.get('EXP_TEMPERATURE', '0')),")

code += '''

# Answer-step switches, applied around the model call (the code above is unchanged):
#   EXP_LENGTH="5:150"   allow N blocks and W words instead of 3 and 80 (prompt, contract, retry messages, check)
#   EXP_QUESTION_LAST=1  put the question after the sources in the request (it stays first too in 'question_first' off)
#   EXP_TABLE_FORMAT=html  give tables as their HTML (merged cells) instead of markdown text
def _exp_len(text):
    spec = os.environ.get('EXP_LENGTH', '')
    if not spec or not isinstance(text, str):
        return text
    blocks, words = spec.split(':')
    return (text.replace('at most 3 short blocks', f'at most {blocks} short blocks')
                .replace('about 80 words', f'about {words} words'))

if os.environ.get('EXP_LENGTH'):
    MAX_ANSWER_WORDS = int(os.environ['EXP_LENGTH'].split(':')[1])
_orig_prompt = guideline_rag_system_prompt
def guideline_rag_system_prompt():
    return _exp_len(_orig_prompt())

_HTML_BY_TEXT = {}
def _exp_html():
    if not _HTML_BY_TEXT:
        for line in CHUNKS_FILE.open(encoding='utf-8'):
            c = json.loads(line)
            if c.get('html') and c.get('text'):
                _HTML_BY_TEXT[c['text']] = c['html']
    return _HTML_BY_TEXT

_orig_llm_json = llm_json
def llm_json(instructions, content, schema, name):
    if name == 'guideline_answer' and isinstance(content, dict):
        content = dict(content)
        if 'previous_answer_error' in content:
            content['previous_answer_error'] = _exp_len(content['previous_answer_error'])
        if os.environ.get('EXP_TABLE_FORMAT') == 'html':
            html = _exp_html()
            content['sources'] = [dict(s, passage=html.get(s['passage'], s['passage'])) for s in content['sources']]
        if os.environ.get('EXP_QUESTION_LAST') == '1':
            question = content.pop('question')
            content['question'] = question
        if os.environ.get('EXP_REASON_FIRST') == '1':
            # The JSON schema's property order is the generation order: facts first, then the answer.
            schema = dict(schema, properties={'key_facts': {'type': 'array', 'items': {'type': 'string'}},
                                              **schema['properties']},
                          required=['key_facts'] + list(schema['required']))
            instructions = instructions + REASON_FIRST_RULE
            result = _orig_llm_json(instructions, content, schema, name)
            if isinstance(result, dict):
                _EXP['key_facts'] = result.pop('key_facts', None)
            return result
    return _orig_llm_json(instructions, content, schema, name)

REASON_FIRST_RULE = \'\'\'
- Before "kind" and "blocks", fill "key_facts": 1-4 short facts copied from the sources that decide the answer,
  each with the group or condition it applies to and the source id, in the form "[source id] <group or condition>: <rule, number or dose as written>".
  Compare the patient's details with these facts, then write blocks that agree with them. key_facts is not shown
  to the user.\'\'\'
'''

code += '''

def _exp_rerank_final(question, ranked_items):
    """Re-order the best EXP_RERANK_POOL fused hits by cross-encoder score against the user's question."""
    pool = int(os.environ.get('EXP_RERANK_POOL', '30'))
    hits = [i for i in ranked_items if i['score'] > 0][:pool]
    hit_set = {id(i) for i in hits}
    rest = [i for i in ranked_items if id(i) not in hit_set]
    def passage(s):
        return ((s.get('heading_path') or '') + '\\n' + ((s.get('caption') or '') + '\\n' if s.get('caption') else '')
                + (s.get('text') or ''))[:4000]
    key = lambda i: (question, i['source'].get('chunk_id'))
    todo = [i for i in hits if key(i) not in _RERANK_CACHE]
    if todo:
        started = time.perf_counter()
        scores = _exp_reranker().predict([(question, passage(i['source'])) for i in todo], batch_size=16,
                                         show_progress_bar=False)
        RERANK_SECONDS[0] += time.perf_counter() - started; RERANK_SECONDS[1] += 1
        for i, s in zip(todo, scores):
            _RERANK_CACHE[key(i)] = float(s)
    hits.sort(key=lambda i: _RERANK_CACHE[key(i)], reverse=True)
    for i in hits:
        i['rerank'] = _RERANK_CACHE[key(i)]
    return hits + rest
'''

code += '''

# ---- Experiment helpers (not part of the app) ----
_EXP = {'question': ''}
_RERANKER = {}
_RERANK_CACHE = {}
RERANK_SECONDS = [0.0, 0]

def _exp_reranker():
    if 'model' not in _RERANKER:
        from sentence_transformers import CrossEncoder
        import torch
        device = 'mps' if torch.backends.mps.is_available() else 'cpu'
        kwargs = {'torch_dtype': torch.float16} if device == 'mps' else {}
        _RERANKER['model'] = CrossEncoder('BAAI/bge-reranker-v2-m3', device=device, model_kwargs=kwargs,
                                          max_length=int(os.environ.get('EXP_RERANK_MAXLEN', '512')))
    return _RERANKER['model']

def _exp_rerank(query, ranked):
    """Re-order the top EXP_RERANK_N candidates by cross-encoder score; the rest keep their order."""
    n = int(os.environ.get('EXP_RERANK_N', '30'))
    if os.environ.get('EXP_RERANK_QUERY', 'query') == 'question' and _EXP.get('question'):
        query = _EXP['question']
    head, tail = ranked[:n], ranked[n:]
    def passage(row):
        heading, text, caption = row[3] or '', row[13] or '', row[14] or ''
        return (heading + '\\n' + (caption + '\\n' if caption else '') + text)[:4000]
    todo = [row for _, row in head if (query, row[0]) not in _RERANK_CACHE]
    if todo:
        started = time.perf_counter()
        scores = _exp_reranker().predict([(query, passage(row)) for row in todo], batch_size=16,
                                         show_progress_bar=False)
        RERANK_SECONDS[0] += time.perf_counter() - started; RERANK_SECONDS[1] += 1
        for row, score in zip(todo, scores):
            _RERANK_CACHE[(query, row[0])] = float(score)
    head = sorted(head, key=lambda item: _RERANK_CACHE[(query, item[1][0])], reverse=True)
    return head + tail
'''
path.write_text(code, encoding='utf-8')
print('wrote', path)
