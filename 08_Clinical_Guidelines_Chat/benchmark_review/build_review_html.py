"""Build clinician_review.html: review_template.html with review_data.json inlined.

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
out = HERE / 'clinician_review.html'
out.write_text(tpl.replace(marker, blob), encoding='utf-8')
print(f'{out.name}: {len(data)} questions, {out.stat().st_size // 1024} KB')
