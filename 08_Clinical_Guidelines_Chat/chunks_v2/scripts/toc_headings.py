"""Heading paths for guidelines without section numbers (NCDIMH, MH Deskguide), anchored on the printed
table of contents.

The parser's '#' levels in these documents are unreliable (callouts and tables appear as H1/H2), but the
table of contents gives a trustworthy two-level skeleton: chapter > TOC entry. We walk the body, switch
chapter / entry when a heading matches the TOC, and use the latest other short heading as a third level.
Each chunk is then located in the document text (as for STI) and takes the stack at that position.
"""
import difflib
import re

from fix_headings import CAPTION, clean_part, tidy_case
from sti_headings import _norm, path_for

TOC_START = re.compile(r'^#+\s*\**\s*table of contents?\b', re.I)
TOC_END = re.compile(r'^#+\s*\**\s*(preface|foreword|list of|acronyms?|abbreviations?|acknowledge?ments?)\b', re.I)
SKIP_ENTRY = re.compile(r'^(preface|foreword|acknowledge?ments?|abbreviations?|acronyms?|definition of terms|'
                        r'references|mental health deskguide)$', re.I)
CHAP_NCD = re.compile(r'^chapter\s+(\d+)\s*:?\s*(.*)$', re.I)
CHAP_NUM = re.compile(r'^(\d{1,2})\.\s+(\S.*)$')


def _strip_toc(line):
    s = re.sub(r'<!--.*?-->', '', line)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'^\s*[-*]\s+', '', s)
    s = s.replace('**', '').replace('\\', '')
    s = re.sub(r'^#+\s*', '', s)
    s = re.sub(r'\.{3,}.*$', '', s)                       # dot leaders + page number
    s = re.sub(r'\s+[ivxlc\d]+\s*$', '', s, flags=re.I)  # trailing page number
    return re.sub(r'\s+', ' ', s).strip(' .:')


def parse_toc(lines):
    """Return (chapters {num: title}, entries [(chapter_num, title)], body_start_line)."""
    start = next((i for i, l in enumerate(lines) if TOC_START.match(l.strip())), None)
    if start is None:
        return {}, [], 0
    end = next((i for i in range(start + 1, len(lines)) if TOC_END.match(lines[i].strip())), len(lines))
    chapters, entries, cur = {}, [], None
    for raw in lines[start + 1:end]:
        s = _strip_toc(raw)
        if len(s) < 3 or SKIP_ENTRY.match(s):
            continue
        m = CHAP_NCD.match(s) or CHAP_NUM.match(s)
        if m:
            cur = m.group(1)
            chapters[cur] = m.group(2).strip()
            continue
        if cur:
            entries.append((cur, s))
    # body = after the front matter that follows the TOC: first body chapter heading
    body = end
    return chapters, entries, body


def _similar(a, b):
    a, b = _norm(a), _norm(b)
    if not a or not b:
        return False
    if a == b or (min(len(a), len(b)) >= 10 and (a.startswith(b) or b.startswith(a))):
        return True
    return difflib.SequenceMatcher(None, a, b).ratio() >= 0.88


def heading_index(md_text):
    """Normalised full text + [(offset, stack)] built from the TOC skeleton."""
    lines = md_text.split('\n')
    chapters, entries, body = parse_toc(lines)
    chap_title = {n: t for n, t in chapters.items()}
    cur_chap = cur_entry = cur_sub = None
    pending_chap = None
    marks, buf, pos = [], [], 0

    def label_chap(n):
        return f'Chapter {n}: {tidy_case(chap_title.get(n, ""))}'.rstrip(': ')

    for i, line in enumerate(lines):
        st = line.strip()
        is_head = bool(re.match(r'^#{1,6}\s', st))
        is_bold = st.startswith('**') and st.rstrip().endswith('**') and len(st) < 120
        if i >= body and (is_head or is_bold):
            t = clean_part(re.sub(r'^#+\s*', '', st))
            t = re.sub(r'<!--.*?-->', '', t).strip()
            changed = False
            m = CHAP_NCD.match(t)
            if not m and is_head:
                m2 = CHAP_NUM.match(t)       # '3. OVERVIEW ...' but not a numbered step '2. Conduct ...'
                m = m2 if m2 and _similar(m2.group(2), chap_title.get(m2.group(1), '')) else None
            ahead = lambda n: cur_chap is None or int(n) >= int(cur_chap)   # chapters only move forward
            if m and m.group(1) in chap_title and ahead(m.group(1)):
                cur_chap, cur_entry, cur_sub, changed = m.group(1), None, None, True
                pending_chap = None if m.group(2).strip() else cur_chap
            elif pending_chap and t:
                pending_chap = None          # 'CHAPTER 2' followed by its title line: already labelled
            else:
                hit = next((n for n, ct in chap_title.items() if _similar(t, ct)), None) if is_head else None
                if hit and hit != cur_chap and ahead(hit):
                    cur_chap, cur_entry, cur_sub, changed = hit, None, None, True
                else:
                    pool = [e for c, e in entries if c == cur_chap] if cur_chap else []
                    e = next((e for e in pool if _similar(t, e)), None)
                    if e:
                        cur_entry, cur_sub, changed = e, None, True
                    elif (is_head and cur_chap and 3 <= len(t) <= 80 and not t.endswith('.')
                          and not CAPTION.match(t) and not re.match(r'^(note|caution|key|source)\b', t, re.I)):
                        cur_sub, changed = t, True
            if changed and cur_chap:
                stack = [label_chap(cur_chap)] + [x for x in (cur_entry, cur_sub) if x]
                marks.append((pos, stack))
            if is_head:
                continue
        n = _norm(line)
        if n:
            buf.append(n)
            pos += len(n) + 1
    return ' '.join(buf), marks


def _chap(p):
    m = re.match(r'Chapter (\d+)', p[0]) if p else None
    return int(m.group(1)) if m else None


def toc_paths(chunks, md_text):
    """Path per chunk (list of parts) or None; unmatched chunks inherit the previous match.

    Chunks are in document order, so chapter numbers must never go down. A chunk whose text also occurs in
    another chapter can be located in the wrong place; we keep the longest non-decreasing run of chapter
    numbers and treat matches outside it as unmatched.
    """
    full, marks = heading_index(md_text)
    raw = [path_for(c['text'], full, marks, min_len=30) for c in chunks]
    idx = [i for i, p in enumerate(raw) if _chap(p) is not None]
    seq = [_chap(raw[i]) for i in idx]
    # longest non-decreasing subsequence (O(n^2) is fine for ~1000 chunks)
    best, back = [1] * len(seq), [-1] * len(seq)
    for j in range(len(seq)):
        for i in range(j):
            if seq[i] <= seq[j] and best[i] + 1 > best[j]:
                best[j], back[j] = best[i] + 1, i
    keep, j = set(), (max(range(len(seq)), key=best.__getitem__) if seq else -1)
    while j >= 0:
        keep.add(idx[j])
        j = back[j]
    out, prev = [], None
    for i, p in enumerate(raw):
        if p is not None and (i in keep or _chap(p) is None):
            prev = p
        out.append(prev if (p is None or (i not in keep and _chap(p) is not None)) else p)
    return out
