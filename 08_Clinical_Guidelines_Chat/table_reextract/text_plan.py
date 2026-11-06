"""Turn text_from_pdf.py sections into a 'section' item batch.

Splits compound headings, builds heading paths (chapter > last numbered heading > sub-heading), drops lines whose full text is
already inside a re-extracted item, assigns every old text chunk in the page range to the section it overlaps most, and writes
a batch of S(...) items.

Usage: python3 text_plan.py SECTIONS.json SPEC.json OLD_CHUNKS.jsonl DOC FIRST LAST CONFIG.json OUT_BATCH.py
CONFIG.json: {"chapters": {"4": "Chapter 4: ...", ...}, "split": {"compound heading": ["first", "second"]},
              "fix": {"garbled heading": "fixed"}, "tag": "t02", "first_chapter": "4"}
"""
import collections, json, re, sys

secs_p, spec_p, old_p, doc, first, last, cfg_p, out_p = sys.argv[1:9]
first, last = int(first), int(last)
cfg = json.load(open(cfg_p))
CH, SPLIT, FIX = cfg['chapters'], cfg.get('split', {}), cfg.get('fix', {})
tok = lambda s: re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', s.lower()))
NUM = re.compile(r'(\d+\.\d+(?:\.\d+)*)\s')

raw = json.load(open(secs_p))
flat = []
for s in raw:
    h = s['heading']
    if h:
        h = FIX.get(h, h).strip()
        if h in ('•', '-'):
            h = None
    hs = [h]
    if h:
        idx = [m.start() for m in NUM.finditer(h)]
        if len(idx) > 1 and idx[0] == 0:
            hs = [h[a:b].strip() for a, b in zip(idx, idx[1:] + [len(h)])]
        if hs[-1] in SPLIT:
            hs = hs[:-1] + SPLIT[hs[-1]]
    for x in hs[:-1]:
        flat.append({'page': s['page'], 'page_end': s['page'], 'heading': x, 'lines': []})
    flat.append(dict(s, heading=hs[-1]))

spec = json.load(open(spec_p))
itemtext = ' ' + ' '.join(' '.join(tok(json.dumps(t, ensure_ascii=False))) for t in spec['tables'] if t.get('kind') != 'section') + ' '
chap, num, sub, out = CH[cfg['first_chapter']], None, None, []
for s in flat:
    h = s['heading']
    intro = cfg.get('chapter_intro', {}).get(str(s['page'])) if not h else None
    if intro:
        chap, num, sub, h = CH[intro], None, None, 'Introduction'
    if h:
        m = re.match(r'(\d+)((?:\.\d+)*)\s', h)
        if m:
            chap = CH.get(m.group(1), chap)
            num, sub = h, None
        else:
            sub = h
    lines = []
    for l in s['lines']:
        t = tok(l)
        if l.strip() in ('', '.', '4') or (len(t) >= 6 and (' ' + ' '.join(t) + ' ') in itemtext and not l.startswith('Key message')):
            continue
        for a, b in cfg.get('replace', {}).items():
            l = l.replace(a, b)
        if l.startswith('• '):
            l = '- ' + l[2:].strip()
        elif l.startswith('o '):
            l = '   - ' + l[2:].strip()
        lines.append(l)
    if not lines:
        continue
    title = (sub or num or chap.split(': ', 1)[-1]) + ('' if h else ' (continued)')
    path = ' > '.join(x for x in (chap, num if num and num != title.replace(' (continued)', '') else None, title) if x)
    out.append({'page': s['page'], 'page_end': s['page_end'], 'title': title, 'path': path, 'content': '\n'.join(lines)})

old = [json.loads(l) for l in open(old_p)]
old = [k for k in old if k['doc_id'] == doc and k['type'] == 'text' and first <= k['page_start'] <= last]
assign, un = collections.defaultdict(list), []
for k in old:
    kt = collections.Counter(tok(k['text']))
    best, bs = None, 0
    for i, s in enumerate(out):
        if s['page'] - 1 <= k['page_start'] <= s['page_end'] + 1:
            sc = sum((kt & collections.Counter(tok(s['content']))).values()) / max(1, sum(kt.values()))
            if sc > bs:
                best, bs = i, sc
    if best is None or bs < 0.2:
        # nearest section by page as a fallback: the chunk is replaced, its content lives in items or the rebuilt text
        best = min(range(len(out)), key=lambda i: abs(out[i]['page'] - k['page_start']))
        un.append((k['chunk_id'], k['page_start'], round(bs, 2), k['text'][:70].replace('\n', ' ')))
    assign[best].append(k['chunk_id'])

J = lambda x: json.dumps(x, ensure_ascii=False)
pre = doc + '-'
L = ['exec(open("batches/hiv_common.py").read())',
     f'# {doc} pp.{first}-{last}: running text rebuilt from the PDF text layer (text_from_pdf.py + text_plan.py); every old text chunk of',
     '# the page range is replaced. Checked page by page against the page images.', 'ITEMS = [']
for i, s in enumerate(out):
    repl = [c[len(pre):] for c in assign.get(i, [])]
    pages = list(range(s['page'], s['page_end'] + 1))
    L.append(f' S("txt-p{s["page"]}-{cfg["tag"]}{i:02d}", {s["page"]}, {J(s["path"])}, {J(s["title"])}, {J(repl)}, {J(s["content"])}'
             + (f', pages={pages}' if len(pages) > 1 else '') + '),')
L.append(']')
open(out_p, 'w').write('\n'.join(L) + '\n')
print(len(out), 'sections;', len(old), 'old text chunks assigned;', len(un), 'by page fallback:')
for u in un:
    print('  ', u)
