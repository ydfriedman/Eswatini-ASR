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
DROP_LINE = re.compile(r'^\s*[*_\\]*\s*(Flowchart:|Diagram:|image:\s*decorative|Figure\s+\d+(\.\d+)*\b)', re.I)
NUMBERED = re.compile(r'^\d+(\.\d+)+\s')
BAD_PART = re.compile(r'^(Flowchart:|Figure\s+\d|Diagram:|Refer to\b)', re.I)


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
        new = []
        for i, c in enumerate(chunks):
            for r in anchor.get(i, []):
                new.append(r)
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
        doc_text = key(' '.join(r['text'].replace(ctx.get(r['table_id'], '') or '\x00', ' ') for r in recs))
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
            out_chunks.append(c)
        chunks = out_chunks
        # 4. merge small text chunks of this document
        merged = []
        for c in chunks:
            small = (c['doc_id'] == doc and c['type'] == 'text' and not c.get('table_id')
                     and len(c['text']) // 4 < SMALL_TOKENS)
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
            if c.pop('_changed', False):
                c['embed_text'] = f"{c['doc_title']} | {c['heading_path']} {page_label(c)}\n\n{plain(c['text'])}"
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
