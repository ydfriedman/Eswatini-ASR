"""Build clinician_review.html (offline file) and hf_space/static/index.html (hosted page that saves answers to the
review server) from review_template.html with review_data.json inlined; also writes hf_space/qids.json.

Run from 08_Clinical_Guidelines_Chat/:
    python3 benchmark_review/build_review_data.py
    python3 benchmark_review/build_review_html.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'review_data.json').read_text(encoding='utf-8'))
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
blob = blob.replace('</', '<\\/').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
tpl = (HERE / 'review_template.html').read_text(encoding='utf-8')
marker = '/*__DATA__*/[]'
assert tpl.count(marker) == 1
server = '/*__SERVER__*/false'
assert tpl.count(server) == 1
page = tpl.replace(marker, blob)
for out, hosted in ((HERE / 'clinician_review.html', False), (HERE / 'hf_space' / 'static' / 'index.html', True)):
    out.write_text(page.replace(server, 'true' if hosted else 'false'), encoding='utf-8')
    print(f'{out.relative_to(HERE)}: {len(data)} questions, {out.stat().st_size // 1024} KB')
(HERE / 'hf_space' / 'qids.json').write_text(json.dumps([q['id'] for q in data]), encoding='utf-8')
