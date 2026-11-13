"""Quality sweep of every chunk in chunks_v3 against the PDF text layer.

For each document:
  gap    - a run of >= 6 words on a PDF page that appears in no chunk covering that page (+/-1): skipped content
  dup    - a sentence (>= 10 words) that appears in two different chunks/items: overlap
  trunc  - a text chunk that ends mid-sentence (no closing punctuation) or on a lead-in (':') while the
           next chunk starts a new section, or a chunk that starts mid-sentence (lower-case first word)
  tiny   - a text chunk with fewer than 15 words of content (orphan)
Page headers/footers are ignored: lines that recur on >= 15% of a document's pages.

Usage: python3 audit/full_sweep.py CHUNKS OUT_JSON   (run from table_reextract/; page text dirs in RAW below)
"""
import collections, json, re, sys

S = '/tmp/claude-0/-home-user-Eswatini-ASR/b17a5174-f3cc-5b8b-8e76-60220ba4e212/scratchpad/'
RAW = {'hiv-2022': 'hiv_raw', 'hiv-amendment-2024': 'amd_work', 'ncdimh': 'ncd_work', 'prep-2025': 'prep_work',
       'anc': 'anc_work', 'sti-vh-draft-2026': 'sti_raw', 'unaids-linkages-sop': 'lk_work4', 'tb-2025': 'tb_raw',
       'fp-2021': 'fp_raw', 'mental-health-deskguide': 'mh_raw'}
tok = lambda s: re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', (s or '').lower()))
def norm(s): return ' '.join(tok(s))

chunks_path, out_path = sys.argv[1], sys.argv[2]
K = [json.loads(l) for l in open(chunks_path)]
report = {}
for doc, raw in RAW.items():
    D = [k for k in K if k['doc_id'] == doc]
    units = collections.OrderedDict()
    for k in D:
        units.setdefault(k.get('table_id') or k['chunk_id'], k)
    U = list(units.values())
    import os
    pages = sorted(int(f[1:-4]) for f in os.listdir(S + raw) if re.fullmatch(r'p\d+\.txt', f))
    ptext = {p: open(f'{S}{raw}/p{p}.txt', errors='ignore').read() for p in pages}
    # boilerplate lines
    linecount = collections.Counter()
    for p in pages:
        for ln in set(norm(l) for l in ptext[p].split('\n')):
            if ln: linecount[ln] += 1
    boiler = {ln for ln, c in linecount.items() if c >= max(3, 0.15 * len(pages))}
    flags = collections.defaultdict(list)
    # gaps
    bypage = collections.defaultdict(set)
    for u in U:
        t = tok(u['text']); g = {tuple(t[i:i + 3]) for i in range(len(t) - 2)}
        for p in range(int(u['page_start']) - 1, int(u.get('page_end') or u['page_start']) + 2):
            bypage[p] |= g
    # trigrams that recur on >= 15% of pages (footers with page numbers, overprinted abbreviation lists)
    dfreq = collections.Counter()
    for p in pages:
        w = [x for x in tok(ptext[p]) if not x.isdigit()]
        dfreq.update({tuple(w[i:i + 3]) for i in range(len(w) - 2)})
    common = {g for g, c in dfreq.items() if c >= max(3, 0.15 * len(pages))}
    for p in pages:
        lines = [norm(l) for l in ptext[p].split('\n')]
        words = [x for x in tok(' '.join(l for l in lines if l and l not in boiler)) if not x.isdigit() or len(x) > 1]
        cov = [False] * len(words)
        for i in range(len(words) - 2):
            g = tuple(words[i:i + 3])
            if g in bypage[p] or tuple(x for x in g) in common:
                cov[i] = cov[i + 1] = cov[i + 2] = True
        run = []
        for w, c in zip(words + ['§'], cov + [True]):
            if not c: run.append(w)
            else:
                if len(run) >= 6: flags[p].append(('gap', ' '.join(run)[:200]))
                run = []
    # duplicates
    sent_owner = collections.defaultdict(set)
    for u in U:
        key = u.get('table_id') or u['chunk_id']
        for s in re.split(r'(?<=[.;!?])\s+|\n|<br/?>|\|', u['text']):
            n = norm(s)
            if len(n.split()) >= 10: sent_owner[n].add(key)
    seenpair = set()
    for s, owners in sent_owner.items():
        if len(owners) > 1:
            o = sorted(owners); pair = tuple(o)
            if pair in seenpair: continue
            seenpair.add(pair)
            p = int(units[o[0]]['page_start'])
            flags[p].append(('dup', ' + '.join(x[len(doc) + 1:] for x in o) + ' :: ' + s[:120]))
    # truncation / tiny (text chunks in document order)
    T = [u for u in U if u['type'] == 'text']
    for i, u in enumerate(T):
        body = re.sub(r'^\s*#+.*\n', '', u['text']).strip()
        last = re.sub(r'[*_`\s]+$', '', body.split('\n')[-1]) if body else ''
        p = int(u['page_start'])
        wc = len(tok(body))
        if wc < 15:
            flags[p].append(('tiny', u['chunk_id'][len(doc) + 1:] + ' :: ' + body[:100].replace('\n', ' ')))
            continue
        if last and not re.search(r'[.!?)\]:;”"’%]$', last) and not last.lstrip().startswith(('|', '-', '*', '•', '#')):
            flags[p].append(('trunc-end', u['chunk_id'][len(doc) + 1:] + ' :: …' + last[-90:]))
        elif last.endswith(':'):
            flags[p].append(('lead-in-end', u['chunk_id'][len(doc) + 1:] + ' :: …' + last[-90:]))
        first = re.sub(r'^[\s*_#>-]+', '', body)[:1]
        if first.islower():
            flags[p].append(('trunc-start', u['chunk_id'][len(doc) + 1:] + ' :: ' + body[:90].replace('\n', ' ')))
    report[doc] = {str(p): v for p, v in sorted(flags.items())}
    c = collections.Counter(f[0] for v in flags.values() for f in v)
    print(f'{doc:26} units {len(U):4}  pages {len(pages):3}  flagged pages {len(flags):3}  ', dict(c))
json.dump(report, open(out_path, 'w'), ensure_ascii=False, indent=1)
