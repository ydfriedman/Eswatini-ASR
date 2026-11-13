"""Remove overlapping text between rebuilt text sections and the tables/figures next to them (HIV 2022, STI/VH draft).

Run from table_reextract/ after fixes/v50_review_fixes.py:  python3 fixes/overlap_fixes.py
1. Hand fixes found in review (HIV 2022 pp.180, 190).
2. Generic rule (the user's: keep the table/figure chunk, drop the duplicate text): a text section ALL of whose
   sentences already appear in a table/figure/box within one page is dropped, and its replaced old chunks move
   to that item. Partial overlaps are left alone (trimming them broke lists and dose instructions).
"""
import json, re

def load(doc): return json.load(open(doc + '_tables.json'))
def save(doc, d): json.dump(d, open(doc + '_tables.json', 'w'), ensure_ascii=False, indent=1)
def norm(t): return re.sub(r'\s+', ' ', re.sub(r'\W+', ' ', re.sub(r'<br/?>', ' ', t or ''))).strip().lower()

# ---- 1. hand fixes, HIV 2022 ----
d = load('hiv-2022'); T = {t['table_id']: t for t in d['tables']}
P = 'hiv-2022-'
t811 = T.get(P + 'tbl-8.11-retesting-lactating')
if t811:
    t811.pop('context_before', None)   # was the Caesarean-section paragraph (previous section; its own chunk)
    two = [f for f in t811['footnotes'] if 'every 2 months' in f]
    t811['footnotes'] = [f for f in t811['footnotes'] if 'every 2 months' not in f]
    f82 = T[P + 'fig-8.2-mbp-schedule']
    for f in two:                      # printed directly under Figure 8.2, not under the table
        if f not in f82['footnotes']: f82['footnotes'].append(f)
    if not any('every 2 months' in s for s in f82['source_flags']):
        f82['source_flags'].append("Retesting interval for HIV-negative lactating women conflicts within section 8.7: the sentence under this figure says every 2 months until the end of breastfeeding; Table 8.11 gives 6 and 14 weeks, then every 3 months to 18 months (6, 9, 12, 15, 18 months); Table 8.12 says every 8 weeks for a mother whose status was unknown.")
s190 = T.get(P + 'txt-p190-t0367')
if s190:
    s190['caption'] = 'Follow-Up of Mother-Baby Pairs After Delivery'
    s190['heading_path'] = 'Chapter 8: Prevention of Mother to Child Transmission of HIV > 8.7 Services for Lactating Women and their Children > Follow-Up of Mother-Baby Pairs After Delivery'
    s190['content'] = re.sub(r'^Follow-Up of Mother-Baby Pairs After Delivery\s*', '', s190['content'])
# 8.3 intro on p.180 duplicates Table 8.5's intro: keep the table (its label already names section 8.3)
drop = {P + 'txt-p180-t0359': P + 'tbl-8.5-retesting-pregnant'}
for src, dst in drop.items():
    if src in T:
        T[dst]['replaces_chunks'] += [c for c in T[src]['replaces_chunks'] if c not in T[dst]['replaces_chunks']]
d['tables'] = [t for t in d['tables'] if t['table_id'] not in drop]
save('hiv-2022', d)

# ---- 2. generic overlap removal ----
report = []
for doc in ('hiv-2022', 'sti-vh-draft-2026'):
    d = load(doc); T = d['tables']
    def item_text(v):
        cells = ' '.join(c['t'] for row in v.get('header', []) + [r for r in v.get('body', []) if isinstance(r, list)] for c in row)
        return norm(' '.join([v.get('context_before', ''), ' '.join(v.get('footnotes', [])), cells, v.get('content', '')]))
    items = [v for v in T if v.get('kind') != 'section']
    IT = {v['table_id']: item_text(v) for v in items}
    dropped = set()
    for u in T:
        if u.get('kind') != 'section': continue
        near = [v for v in items if abs(int(v['page']) - int(u['page'])) <= 1]
        lines, removed, holder = [], 0, None
        for line in u['content'].split('\n'):
            n = norm(line)
            # a whole line (paragraph or bullet) is removed only when the entire line is in a neighbouring item;
            # lines are never cut part-way (that broke dose instructions)
            hit = next((v for v in near if len(n.split()) >= 8 and n in IT[v['table_id']]), None)
            if hit: removed += 1; holder = holder or hit
            else: lines.append(line)
        # every sentence of the section already in neighbouring items: drop the whole section (nothing is lost)
        sents = [norm(x) for x in re.split(r'(?<=[.;:])\s+|\n', u['content']) if len(x.split()) >= 4]
        allin = sents and all(any(x in IT[v['table_id']] for v in near) for x in sents)
        if allin and not removed:
            holder = next(v for v in near if sents[0] in IT[v['table_id']])
            removed = len(sents); lines = []
        if not (allin and removed):  # partial overlaps are left alone: removing lines broke lists and dose instructions
            continue
        rest = re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()
        if len(norm(rest).split()) < 8:
            holder['replaces_chunks'] += [c for c in u['replaces_chunks'] if c not in holder['replaces_chunks']]
            dropped.add(u['table_id']); report.append((doc, u['table_id'], 'dropped', holder['table_id']))
        else:
            u['content'] = rest; report.append((doc, u['table_id'], f'{removed} line(s) removed', holder['table_id']))
    d['tables'] = [t for t in T if t['table_id'] not in dropped]
    save(doc, d)
for r in report: print(*r)
print(len(report), 'sections changed;', sum(1 for r in report if r[2] == 'dropped'), 'dropped')
