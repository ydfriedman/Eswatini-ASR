# Repairs from the completeness audit (audit/REPAIR_WORKLIST.md). Loaded after fp_b02.
import copy as _c, json as _j
_prev = {t['table_id']: t for t in _j.load(open('fp-2021_tables.json'))['tables']}
_t = _c.deepcopy(_prev['fp-2021-tbl-p116-0210'])
for row in _t['body']:
    for c in row:
        if isinstance(c, dict) and '<br/>Condom<br/>IUD' in c.get('t', ''):
            c['t'] = c['t'].split('<br/>Condom<br/>IUD')[0]  # decorative icon labels from the page border, not table content
ITEMS = [_t]
