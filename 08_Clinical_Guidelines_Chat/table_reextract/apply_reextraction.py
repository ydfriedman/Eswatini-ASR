"""Merge re-extracted tables/boxes/flowcharts into the chunk set: chunks_v2 -> chunks_v3.

For each re-extracted guideline (a *_tables.json spec plus its *_chunks.jsonl records):
  1. remove the chunks listed in each item's replaces_chunks and insert the new records in their place
  2. clean neighbouring text chunks: drop 'Flowchart: ...' and figure-caption lines, decorative image lines,
     and lines that are now duplicated inside a new record; drop text chunks left with no content
  3. fix chapter labels from the PDF page -> chapter map in the spec ('chapters'), and give unnumbered
     text chunks the numbered section of the chunk before them in the same chapter
  4. merge very small text chunks into a neighbouring text chunk of the same chapter
  5. recompute section_id, parent_section_id, prev/next ids (all parts of one table share neighbours),
     sizes, and embed_text for text chunks that changed
Guidelines not re-extracted yet pass through unchanged.

Usage: python3 apply_reextraction.py ../chunks_v2 ../chunks_v3 SPEC.json RECORDS.jsonl [SPEC2.json RECORDS2.jsonl ...]
"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'chunks_v2', 'scripts'))
from build_v2 import norm, page_label, plain, sid  # noqa: E402
from fix_headings import tidy_case  # noqa: E402

SMALL_TOKENS, MERGED_MAX_TOKENS = 80, 400
NEW_SECTION = re.compile(r'^\s*#*\s*[*_<u>\s]*\d+\.\d+(\.\d+)*\s+\S')
DROP_LINE = re.compile(r'^\s*[*_\\]*\s*(Flowchart:|Diagram:|image:\s*decorative|Figure\s+\d+(\.\d+)*\b)', re.I)
NUMBERED = re.compile(r'^\d+(\.\d+)+\s')
BAD_PART = re.compile(r'^(Flowchart:|Figure\s+\d|Diagram:|Refer to\b)', re.I)


TINY_TOKENS = 60
# lines of a replaced chunk that are never kept as leftover text: parser placeholders and figure labels
REST_SKIP = re.compile(r'^[\s*_>#-]*(image:|photo:|drawing:|flow_?chart\b|diagram:|flowchart:|figure\s+\d|table\s+\d|sections:|items:|<)|\s->\s', re.I)


def tok(s):
    return re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', (s or '').lower()))


def grams(s):
    t = tok(s)
    return {tuple(t[i:i + 3]) for i in range(len(t) - 2)}


def in_fix_range(spec, c):
    r = spec.get('text_fix_pages')
    return bool(r) and c['doc_id'] == spec['doc_id'] and r[0] <= c['page_start'] <= r[1]


def denoise(text):
    """Embedding text only: drop image/icon/photo placeholder lines and escaped markdown asterisks."""
    lines = [l for l in text.split('\n') if not re.match(r'^\W*(image|icon|photo):', l.strip(), re.I)]
    text = '\n'.join(lines).replace('\\*', '').replace('\\_', '_')
    text = re.sub(r'\*{2,}', '', text)
    text = re.sub(r'(?i)\bicon:\s*\w+(\s\w+)?', '', text)
    return re.sub(r'[ \t]{2,}', ' ', text).strip()


def strip_divider(text):
    """Remove a chapter title page ('**CHAPTER 10:**', '**HIV**', '**NON-COMMUNICABLE**', ...)."""
    lines, out, i = text.split('\n'), [], 0
    while i < len(lines):
        if re.match(r'^\s*\*\*\s*CHAPTER\s+\d+:?\s*\*\*\s*$', lines[i]):
            i += 1
            while i < len(lines) and (not lines[i].strip() or re.match(r'^\s*\*\*[^*a-z]{1,40}\*\*\s*$', lines[i])):
                i += 1
            continue
        out.append(lines[i]); i += 1
    return '\n'.join(out)


def key(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def main(src, out, pairs):
    chunks = [json.loads(l) for l in open(os.path.join(src, 'chunks.jsonl'))]
    removed, log = [], []
    for spec_path, rec_path in pairs:
        spec = json.load(open(spec_path))
        doc = spec['doc_id']
        recs = [json.loads(l) for l in open(rec_path)]
        for r in recs:
            r['doc_id'] = doc
        replaced = {c for r in recs for c in r['replaces_chunks']}
        # 1. replace, inserting each item's records where its first replaced chunk was
        first_pos = {}
        for i, c in enumerate(chunks):
            if c['chunk_id'] in replaced:
                first_pos.setdefault(c['chunk_id'], i)
        anchor, last = {}, 0
        for r in recs:      # records are in page order; an item that replaces nothing (it was missing) goes after the previous one
            found = [first_pos[c] for c in r['replaces_chunks'] if c in first_pos]
            pos = min(found) if found else last
            last = pos
            anchor.setdefault(pos, []).append(r)
        # 1a. text a replaced chunk held besides the item (the heading above a table, an intro sentence, a note under
        # it) must not be lost: lines of the replaced chunk that no record and no other chunk of the document contains
        # are kept as a '<chunk>-rest' text chunk next to the item (before it if they came before the item's content)
        doc_grams = set()
        for r in recs:
            doc_grams |= grams(r['text'])
        for c in chunks:
            if c['doc_id'] == doc and c['chunk_id'] not in replaced:
                doc_grams |= grams(c['text'])
        rest = {}
        for c in chunks:
            if c['chunk_id'] not in replaced or c['chunk_id'] in spec.get('text_drop', []) or c['type'] != 'text':
                continue   # an old flowchart/table chunk was replaced on purpose: its leftovers are its own garbled text
            before, after, seen_cov = [], [], False
            for ln in c['text'].split('\n'):
                s = ln.strip()
                if not s or s.startswith('|') or REST_SKIP.match(s):
                    continue
                g = grams(s)
                if not g or sum(x in doc_grams for x in g) / len(g) >= 0.5:
                    if g: seen_cov = True
                    continue
                (after if seen_cov else before).append(ln)
            def keep(ls):   # at least 8 words of prose besides headings
                return ls if len(tok(' '.join(l for l in ls if not l.lstrip().startswith('#')))) >= 8 else []
            before, after = keep(before), keep(after)
            if before or after:
                rest[c['chunk_id']] = (before, after)
        new = []
        for i, c in enumerate(chunks):
            for r in anchor.get(i, []):
                b = [x for cid in r['replaces_chunks'] for x in rest.get(cid, ([], []))[0]]
                a = [x for cid in r['replaces_chunks'] for x in rest.get(cid, ([], []))[1]]
                src = next((chunks[first_pos[cid]] for cid in r['replaces_chunks'] if cid in first_pos), None)
                if b and src:
                    new.append(dict(src, chunk_id=src['chunk_id'] + '-rest-a', text='\n'.join(b), type='text', _changed=True))
                    log.append((src['chunk_id'], 'text kept beside item', r['table_id']))
                new.append(r)
                if a and src:
                    new.append(dict(src, chunk_id=src['chunk_id'] + '-rest', text='\n'.join(a), type='text', _changed=True))
                    log.append((src['chunk_id'], 'text kept beside item', r['table_id']))
                for cid in r['replaces_chunks']:
                    rest.pop(cid, None)
            if c['chunk_id'] in replaced:
                by = next(r['table_id'] for r in recs if c['chunk_id'] in r['replaces_chunks'])
                removed.append(dict(c, drop_reason=f'replaced by {by}'))
                log.append((c['chunk_id'], 'replaced', by))
            else:
                new.append(c)
        chunks = new
        # text already inside new records; an item's context_before is NOT counted, because it is not in the
        # item's embedding text, so the neighbouring text chunk must keep it to stay searchable
        ctx = {t['table_id']: t.get('context_before', '') for t in spec['tables']}
        # a line counts as duplicated only if it is inside an item printed within 2 pages of the text chunk
        # (matching against the whole document stripped list items that merely recur far away)
        item_pages = {t['table_id']: set(t.get('pages') or [t['page']]) for t in spec['tables']}
        rec_keys = {}
        for r in recs:
            rec_keys.setdefault(r['table_id'], key(r['text'].replace(ctx.get(r['table_id'], '') or '\x00', ' ')))
        def near_text(c):
            lo, hi = c['page_start'] - 2, c.get('page_end', c['page_start']) + 2
            return ' '.join(v for tid, v in rec_keys.items() if any(lo <= p <= hi for p in item_pages.get(tid, ())))
        chapters = sorted(spec.get('chapters', []), key=lambda x: x['page'])
        # 2-3. clean text chunks and fix labels
        prev_section = {}
        out_chunks = []
        for c in chunks:
            if c['doc_id'] != doc or c.get('table_id') or c['type'] != 'text':   # only plain text chunks are cleaned/relabelled
                if c['doc_id'] == doc and c.get('table_id'):
                    parts = c['heading_path'].split(' > ')
                    num = [i for i, p in enumerate(parts) if NUMBERED.match(p)]
                    if num:
                        prev_section[parts[0]] = parts[:num[-1] + 1]
                out_chunks.append(c)
                continue
            orig_text = c['text']
            lines, kept = strip_divider(c['text']).split('\n'), []
            doc_text = near_text(c)
            for ln in lines:
                k = key(ln)
                if DROP_LINE.match(ln) or (len(k) >= 25 and k in doc_text):
                    continue
                kept.append(ln)
            text = re.sub(r'\n{3,}', '\n\n', '\n'.join(kept)).strip()
            body = key(' '.join(l for l in text.split('\n') if not l.lstrip().startswith('#')))
            if len(body) < 40 and text != c['text']:    # only drop chunks that the cleaning itself emptied
                removed.append(dict(c, drop_reason='emptied: content now in re-extracted items'))
                log.append((c['chunk_id'], 'emptied', ''))
                continue
            if text != c['text']:
                c = dict(c, text=text, _changed=True)
                log.append((c['chunk_id'], 'cleaned', ''))
            parts = [p for p in c['heading_path'].split(' > ') if not BAD_PART.match(p)] or [c['heading_path']]
            if chapters:
                ch = [x['label'] for x in chapters if x['page'] <= c['page_start']]
                m = re.search(r'(?im)^[#*\s]*CHAPTER\s+(\d+)', orig_text)
                in_text = [x['label'] for x in chapters if m and x['label'].startswith(f'Chapter {m.group(1)}:')]
                if in_text:      # the chunk starts a new chapter: label it by that chapter and its first numbered heading
                    first = re.search(r'(?m)^#+\s*\**\s*(\d+(?:\.\d+)+\s+[^*\n]+)', text)
                    parts = in_text + ([tidy_case(first.group(1).strip())] if first else [])
                    ch = in_text
                if ch:
                    if parts[0].lower().startswith('chapter'):
                        if parts[0] != ch[-1]:
                            parts[0] = ch[-1]
                    else:
                        parts = [ch[-1]] + parts
                    if not any(NUMBERED.match(p) for p in parts[1:]) and parts[0] in prev_section:
                        sec = prev_section[parts[0]]
                        parts = sec + [p for p in parts[1:] if p not in sec]
                    num = [i for i, p in enumerate(parts) if NUMBERED.match(p)]
                    if num:
                        prev_section[parts[0]] = parts[:num[-1] + 1]
                    new_path = ' > '.join(dict.fromkeys(parts))
                    if new_path != c['heading_path']:
                        log.append((c['chunk_id'], 'label', f"{c['heading_path']} => {new_path}"))
                        c = dict(c, heading_path=new_path, _changed=True)
            fixed = spec.get('text_labels', {}).get(c['chunk_id'])
            if fixed and fixed != c['heading_path']:     # hand-reviewed label from the PDF's headings
                log.append((c['chunk_id'], 'label', f"{c['heading_path']} => {fixed}"))
                c = dict(c, heading_path=fixed, _changed=True)
            if in_fix_range(spec, c):
                c = dict(c, _changed=True, _noise=True)  # rebuild embed text without markdown noise
            out_chunks.append(c)
        chunks = out_chunks
        # 3b. a heading stranded at the end of a text chunk moves to the start of the next chunk
        for i, c in enumerate(chunks):
            if c['doc_id'] != doc or c['type'] != 'text' or c.get('table_id') or not in_fix_range(spec, c):
                continue
            lines = c['text'].rstrip().split('\n')
            tail = []
            while lines and (re.match(r'^\s*#{1,6}\s', lines[-1]) or not lines[-1].strip()):
                tail.insert(0, lines.pop())
            tail = [t for t in tail if t.strip()]
            if tail and lines:
                c['text'] = '\n'.join(lines).rstrip()
                c['_changed'] = True
                nxt = chunks[i + 1] if i + 1 < len(chunks) else None
                if nxt and nxt['doc_id'] == doc and nxt['type'] == 'text' and not nxt.get('table_id'):
                    nxt['text'] = '\n'.join(tail) + '\n\n' + nxt['text']
                    nxt['_changed'] = True
                    log.append((c['chunk_id'], 'heading moved to', nxt['chunk_id']))
                else:
                    log.append((c['chunk_id'], 'trailing heading dropped (next is a table/flowchart)', ' '.join(tail)))
        # 4. merge small text chunks of this document (chunks listed in text_drop are dropped first, never merged)
        pre_drop = set(spec.get('text_drop', []))
        for c in [c for c in chunks if c['chunk_id'] in pre_drop]:
            removed.append(dict(c, drop_reason='heading-only fragment (text_drop)'))
            log.append((c['chunk_id'], 'dropped', ''))
        chunks = [c for c in chunks if c['chunk_id'] not in pre_drop]
        merged = []
        for c in chunks:
            small = (c['doc_id'] == doc and c['type'] == 'text' and not c.get('table_id')
                     and len(c['text']) // 4 < SMALL_TOKENS
                     and not NEW_SECTION.match(c['text']))   # a chunk that opens a numbered section keeps its own label
            prev = merged[-1] if merged else None
            if (small and prev and prev['doc_id'] == doc and prev['type'] == 'text' and not prev.get('table_id')
                    and prev['heading_path'].split(' > ')[0] == c['heading_path'].split(' > ')[0]
                    and (len(prev['text']) + len(c['text'])) // 4 <= MERGED_MAX_TOKENS):
                prev['text'] = prev['text'].rstrip() + '\n\n' + c['text']
                prev['page_end'] = max(prev['page_end'], c['page_end'])
                prev['absorbed_chunk_ids'] = prev.get('absorbed_chunk_ids', []) + [c['chunk_id']]
                prev['_changed'] = True
                removed.append(dict(c, drop_reason=f'merged into {prev["chunk_id"]}'))
                log.append((c['chunk_id'], 'merged into', prev['chunk_id']))
                continue
            merged.append(dict(c))
        chunks = merged
        # 4b. tiny fragments that could not join the chunk before (a table or flowchart) join the next text chunk
        out2, carry = [], None
        for c in chunks:
            if carry is not None:
                if (c['doc_id'] == doc and c['type'] == 'text' and not c.get('table_id')
                        and c['heading_path'].split(' > ')[0] == carry['heading_path'].split(' > ')[0]
                        and (len(carry['text']) + len(c['text'])) // 4 <= MERGED_MAX_TOKENS):
                    c = dict(c, text=carry['text'].rstrip() + '\n\n' + c['text'], page_start=min(c['page_start'], carry['page_start']),
                             absorbed_chunk_ids=c.get('absorbed_chunk_ids', []) + [carry['chunk_id']], _changed=True)
                    removed.append(dict(carry, drop_reason=f'merged into {c["chunk_id"]}'))
                    log.append((carry['chunk_id'], 'merged into', c['chunk_id']))
                else:
                    out2.append(carry)
                carry = None
            tiny = (c['doc_id'] == doc and c['type'] == 'text' and not c.get('table_id') and in_fix_range(spec, c)
                    and len(c['text']) // 4 < TINY_TOKENS)
            if tiny:
                carry = c
                continue
            out2.append(c)
        if carry is not None:
            out2.append(carry)
        chunks = out2
        # 4c. hand-chosen merges for fragments that sit between tables/flowcharts: spec 'text_merge' {src: dst}
        # (src text is appended to dst; dst keeps its label and position)
        drop = set(spec.get('text_drop', []))          # heading-only leftovers (content now in a re-extracted item)
        for c in [c for c in chunks if c['chunk_id'] in drop]:
            removed.append(dict(c, drop_reason='heading-only fragment (text_drop)'))
            log.append((c['chunk_id'], 'dropped', 'heading-only fragment'))
        chunks = [c for c in chunks if c['chunk_id'] not in drop]
        tm = spec.get('text_merge', {})
        if tm:
            by_id = {c['chunk_id']: c for c in chunks}
            for s_id, d_id in tm.items():
                s_c, d_c = by_id.get(s_id), by_id.get(d_id)
                if not s_c or not d_c:
                    continue
                d_c['text'] = d_c['text'].rstrip() + '\n\n' + s_c['text']
                d_c['page_end'] = max(d_c['page_end'], s_c['page_end'])
                d_c['absorbed_chunk_ids'] = d_c.get('absorbed_chunk_ids', []) + [s_id] + s_c.get('absorbed_chunk_ids', [])
                d_c['_changed'] = True
                removed.append(dict(s_c, drop_reason=f'merged into {d_id}'))
                log.append((s_id, 'merged into', d_id))
            chunks = [c for c in chunks if c['chunk_id'] not in tm or c['chunk_id'] not in by_id or by_id.get(tm[c['chunk_id']]) is None]
        # 4e. page furniture and page-break splits (quality sweep): running-header lines that recur in >= 4% of the
        # document's text chunks and page-number tags are removed; a sentence cut at a page break (chunk ends without
        # closing punctuation, next text chunk starts in lower case) is re-joined into the first chunk
        T = [c for c in chunks if c['doc_id'] == doc and c['type'] == 'text' and not c.get('table_id')]
        hc = {}
        for c in T:
            for ln in set(l.strip() for l in c['text'].split('\n')):
                bare = ln.lstrip('#').strip(' *_')
                if re.match(r'^# [^#]', ln) and len(tok(ln)) <= 8 and bare == bare.upper():   # top-level ALL-CAPS line only
                    hc[ln] = hc.get(ln, 0) + 1
        furniture = {l for l, n in hc.items() if n >= max(4, 0.04 * len(T)) and not re.search(r'\d+\.\d+', l)}
        foot = {}        # page footers: a short ALL-CAPS non-heading line, page number aside, recurring in >= 4 chunks
        for c in T:
            seen_f = set()
            for ln in set(l.strip() for l in c['text'].split('\n')):
                pl_ = re.sub(r'<[^>]+>', '', ln)
                w = [t for t in tok(ln) if not t.isdigit()]
                if ln and not ln.startswith(('#', '|')) and 2 <= len(w) <= 6 and pl_ == pl_.upper():
                    fk = ' '.join(w)
                    e = foot.setdefault(fk, [set(), 0]); e[0].add(ln)
                    if fk not in seen_f: e[1] += 1; seen_f.add(fk)
        for lines_f, n_f in foot.values():
            if n_f >= 4: furniture |= lines_f
        for c in T:
            lines = [l for l in c['text'].split('\n') if l.strip() not in furniture]
            txt = re.sub(r'<circle>\s*\d+\s*</circle>|^\s*\d{1,3}\s*$', '', '\n'.join(lines), flags=re.M)
            txt = re.sub(r'\n{3,}', '\n\n', txt).strip()
            txt = re.sub(r'(?<=[a-z,])\n\n(?=[a-z])(?!(?:image|photo|drawing|flow_?chart|diagram|icon)\b)(?![a-z][.)]\s)',   # sentence broken
                         lambda m: '\n\n' if txt[:m.start()].rsplit('\n', 1)[-1].lstrip().startswith('#') else ' ', txt)  # at a page break
            if txt != c['text']:
                c['text'] = txt; c['_changed'] = True
        for i, c in enumerate(chunks[:-1]):
            nx = chunks[i + 1]
            if c not in T or nx not in T or not c['text'] or not nx['text']:
                continue
            last = c['text'].rstrip().split('\n')[-1].rstrip(' *_')
            m = re.match(r'([a-z][^\n]*?[.;:!?])(\s|$)', nx['text'].lstrip())
            if last and not re.search(r'[.!?:;)\]|]$', last) and not last.lstrip().startswith(('#', '|')) and m:
                frag = m.group(1)
                c['text'] = c['text'].rstrip() + ' ' + frag
                nx['text'] = nx['text'].lstrip()[len(frag):].lstrip()
                c['_changed'] = nx['_changed'] = True
                log.append((c['chunk_id'], 'page-break sentence re-joined from', nx['chunk_id']))
        # 4d. hand-checked repairs from the page images (quality sweep):
        #   'text_replace' {chunk_id: text}   - the chunk's text rewritten from the PDF text layer (skipped lines restored)
        #   'text_add' [{after, page, heading_path, text}] - a passage missing from every chunk, inserted after chunk/item `after`
        for cid, txt in spec.get('text_replace', {}).items():
            for c in chunks:
                if c['chunk_id'] == cid:
                    if isinstance(txt, dict):          # {text, page_end}: a passage joined across a page break
                        c['page_end'] = max(c['page_end'], txt.get('page_end') or c['page_end'])
                        c['heading_path'] = txt.get('heading_path') or c['heading_path']; txt = txt['text']
                    c['text'] = txt; c['_changed'] = True
                    log.append((cid, 'text rewritten from page', ''))
        for cid, ins in spec.get('text_insert', {}).items():     # [anchor, text]: a skipped paragraph put back after the anchor
            for c in chunks:                                     # line (anchor '' = at the start of the chunk)
                if c['chunk_id'] == cid:
                    for anchor, add_t in ins:
                        if anchor == '':
                            c['text'] = add_t + '\n\n' + c['text']
                        elif anchor in c['text']:
                            i = c['text'].index(anchor) + len(anchor)
                            j = c['text'].find('\n', i); j = len(c['text']) if j < 0 else j
                            c['text'] = c['text'][:j] + '\n\n' + add_t + c['text'][j:]
                        else:
                            log.append((cid, 'text_insert anchor missing', anchor[:60])); continue
                        c['_changed'] = True; log.append((cid, 'paragraph restored from page', add_t[:60]))
        for cid, subs in spec.get('text_strip', {}).items():     # decorative image captions etc. cut out of a chunk
            for c in chunks:
                if c['chunk_id'] == cid:
                    t0 = c['text']
                    for sub in subs:
                        c['text'] = c['text'].replace(sub, '')
                    c['text'] = re.sub(r'\n{3,}', '\n\n', c['text']).strip()
                    if c['text'] != t0:
                        c['_changed'] = True; log.append((cid, 'text stripped', '; '.join(subs)[:80]))
                    else:
                        log.append((cid, 'text_strip no match', '; '.join(subs)[:80]))
        for n, a in enumerate(spec.get('text_add', [])):
            pos = next((i for i, c in enumerate(chunks) if c['chunk_id'] == a['after'] or c.get('table_id') == a['after']), None)
            if pos is None:
                log.append((a['after'], 'text_add anchor missing', a['text'][:60])); continue
            while pos + 1 < len(chunks) and chunks[pos + 1].get('table_id') and chunks[pos + 1].get('table_id') == chunks[pos].get('table_id'):
                pos += 1     # after the last part of a split item
            base = chunks[pos]
            nc = {k: base[k] for k in ('doc_id', 'doc_title') if k in base}
            nc.update(chunk_id=f"{doc}-add-p{a['page']}-{n}", type='text', heading_path=a['heading_path'], page_start=a['page'],
                      page_end=a.get('page_end', a['page']), text=a['text'], _changed=True)
            chunks.insert(pos + 1, nc)
            log.append((nc['chunk_id'], 'added from page', a['after']))

        # 4f. section items rebuilt from the PDF text layer ('txt-*', one record each) that hold under 40 words (a bare
        # list of organisms, a one-line note) join the neighbouring section item of the same chapter, up to
        # MERGED_MAX_TOKENS; the merged record keeps the first item's id and heading path
        nrec = {}
        for c in chunks:
            if c.get('table_id'): nrec[c['table_id']] = nrec.get(c['table_id'], 0) + 1
        def sec1(c):
            return (c['doc_id'] == doc and c['type'] == 'text' and '-txt-' in (c.get('table_id') or '')
                    and nrec.get(c['table_id']) == 1)
        out3 = []
        for c in chunks:
            prev = out3[-1] if out3 else None
            if (prev is not None and sec1(c) and sec1(prev)
                    and prev['heading_path'].split(' > ')[0] == c['heading_path'].split(' > ')[0]
                    and (len(tok(prev['text'])) < 40 or len(tok(c['text'])) < 40)
                    and (len(prev['text']) + len(c['text'])) // 4 <= MERGED_MAX_TOKENS):
                prev['text'] = prev['text'].rstrip() + '\n\n' + c['text']
                prev['page_end'] = max(prev['page_end'], c['page_end'])
                prev['absorbed_chunk_ids'] = prev.get('absorbed_chunk_ids', []) + [c['chunk_id']]
                prev['_changed'] = True
                removed.append(dict(c, drop_reason=f'merged into {prev["chunk_id"]}'))
                log.append((c['chunk_id'], 'small section merged into', prev['chunk_id']))
                continue
            out3.append(c)
        chunks = out3

        # 4g. a plain text chunk grown past ~470 tokens (restored paragraphs) is split at the paragraph boundary nearest
        # its middle, so each embedding part stays under the 512-token limit; the second part repeats the section name
        def split_long(c, depth=0):
            t = c['text']
            if (depth > 3 or c['doc_id'] != doc or c['type'] != 'text' or c.get('table_id') or (len(t) + len(c.get('doc_title', '')) + len(c['heading_path']) + 30) // 4 <= 505):   # embed_text = title | path + text
                return [c]
            cuts = [m.start() for m in re.finditer(r'\n\n', t) if 0.25 * len(t) <= m.start() <= 0.75 * len(t)]
            if not cuts:
                cuts = [m.start() for m in re.finditer(r'\n(?=[-*•] |\d+\. )', t) if 0.25 * len(t) <= m.start() <= 0.75 * len(t)]
            if not cuts:
                return [c]
            cut = min(cuts, key=lambda x: abs(x - len(t) // 2))
            name = c['heading_path'].split(' > ')[-1]
            a = dict(c, text=t[:cut].rstrip(), _changed=True)
            b = dict(c, text=f'## {name} (continued)\n\n' + t[cut:].strip(), _changed=True,
                     chunk_id=f"{c['chunk_id']}-s{depth + 1}", absorbed_chunk_ids=[])
            log.append((c['chunk_id'], 'long chunk split into', b['chunk_id']))
            return split_long(a, depth + 1) + split_long(b, depth + 1)
        out4 = []
        for c in chunks:
            out4 += split_long(c)
        chunks = out4

    # 5. ids, neighbours, sizes, embed text
    groups = []          # consecutive records of one table_id form a group
    for c in chunks:
        if groups and c.get('table_id') and groups[-1][0].get('table_id') == c['table_id']:
            groups[-1].append(c)
        else:
            groups.append([c])
    for gi, g in enumerate(groups):
        before = groups[gi - 1][-1] if gi and groups[gi - 1][-1]['doc_id'] == g[0]['doc_id'] else None
        after = groups[gi + 1][0] if gi + 1 < len(groups) and groups[gi + 1][0]['doc_id'] == g[0]['doc_id'] else None
        for c in g:
            parts = c['heading_path'].split(' > ')
            c['section_id'] = sid(c['doc_id'], c['heading_path'])
            c['parent_section_id'] = sid(c['doc_id'], ' > '.join(parts[:-1])) if len(parts) > 1 else c['section_id']
            c['prev_chunk_id'] = before['chunk_id'] if before else None
            c['next_chunk_id'] = after['chunk_id'] if after else None
            c['n_chars'] = len(c['text'])
            c['approx_tokens'] = len(c['text']) // 4
            noise = c.pop('_noise', False)
            if c.pop('_changed', False):
                body = plain(c['text'])
                if noise:
                    body = denoise(body)
                c['embed_text'] = f"{c['doc_title']} | {c['heading_path']} {page_label(c)}\n\n{body}"
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'chunks.jsonl'), 'w') as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + '\n')
    cols = ['chunk_id', 'doc_id', 'doc_title', 'type', 'table_id', 'table_part', 'heading_path', 'page_start', 'page_end',
            'section_id', 'parent_section_id', 'prev_chunk_id', 'next_chunk_id', 'approx_tokens', 'text', 'embed_text']
    with open(os.path.join(out, 'chunks.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(chunks)
    with open(os.path.join(out, 'removed_chunks.jsonl'), 'w') as fh:
        for c in removed:
            fh.write(json.dumps(c, ensure_ascii=False) + '\n')
    with open(os.path.join(out, 'merge_log.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['chunk_id', 'action', 'detail'])
        w.writerows(log)
    over = [c['chunk_id'] for c in chunks if len(c['embed_text']) // 4 > 512]
    print(f'chunks {len(chunks)} | removed {len(removed)} | log {len(log)} | embed_text >512 est. tokens: {len(over)} {over[:6]}')


if __name__ == '__main__':
    a = sys.argv[1:]
    main(a[0], a[1], list(zip(a[2::2], a[3::2])))
