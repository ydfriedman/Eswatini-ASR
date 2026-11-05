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
from sti_headings import _norm

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


GENERIC = set("""definition definitions classification diagnosis diagnostic criteria investigation investigations pharmacological
non nonpharmacological treatment treatments management managing referral refer monitoring follow up followup patient patients
assessment clinical presentation features feature complications prevention special populations population pregnancy key messages
targets target risk factors signs symptoms introduction notes note general principles adults adult children child drug drugs
choice therapy medical definitive approach staging summary supportive care epidemiology causes aetiology etiology overview screening
history examination laboratory tests test recommendations recommended indications contraindications dose doses dosing maintenance
initial acute chronic emergency emergencies health education counselling counseling side effects adverse when what how goals goal
other others further common types type specific related based including immediate actions action plan steps step options option
first second line lines level levels important points summary table figure algorithm flowchart flow chart protocol protocols
inpatient outpatient hospital facility home community primary secondary tertiary severity severe mild moderate""".split())
STOP = {"of", "and", "the", "for", "in", "on", "to", "with", "a", "an", "by", "at", "or", "as", "from", "into"}


def is_generic(t):
    """'Pharmacological Treatment', 'Diagnostic Criteria', 'Management in Special Populations' carry no topic."""
    words = [w for w in re.findall(r"[a-z]+", t.lower()) if w not in STOP]
    return bool(words) and all(w in GENERIC or len(w) <= 2 for w in words)


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
    cur_chap = cur_entry = cur_sub = cur_topic = None
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
                cur_chap, cur_entry, cur_sub, cur_topic, changed = m.group(1), None, None, None, True
                pending_chap = None if m.group(2).strip() else cur_chap
            elif pending_chap and t:
                pending_chap = None          # 'CHAPTER 2' followed by its title line: already labelled
            else:
                hit = next((n for n, ct in chap_title.items() if _similar(t, ct)), None) if is_head else None
                if hit and hit != cur_chap and ahead(hit):
                    cur_chap, cur_entry, cur_sub, cur_topic, changed = hit, None, None, None, True
                else:
                    pool = [e for c, e in entries if c == cur_chap] if cur_chap else []
                    e = next((e for e in pool if _similar(t, e)), None)
                    heading_ok = (is_head and cur_chap and 3 <= len(t) <= 80 and not t.endswith('.')
                                  and not CAPTION.match(t) and not re.match(r'^(note|caution|key|source)\b', t, re.I))
                    if e and not is_generic(e):
                        cur_entry, cur_topic, cur_sub, changed = e, None, None, True   # entry from the printed TOC
                    elif heading_ok and not is_generic(t) and len(t) <= 70 and ':' not in t:
                        cur_topic, cur_sub, changed = t, None, True    # topic heading under it (e.g. 'Hypothyroidism')
                    elif e or heading_ok:
                        cur_sub, changed = (e or t), True              # generic heading: 'Pharmacological Treatment'
            if changed and cur_chap:
                stack = [label_chap(cur_chap)] + [x for x in (cur_entry, cur_topic, cur_sub) if x]
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


def _locate_text(text):
    """Chunk text used for locating: no heading lines, no table header rows (they repeat across tables)."""
    lines, out = text.split('\n'), []
    for i, line in enumerate(lines):
        st = line.strip()
        if re.match(r'^#{1,6}\s', st):
            continue
        if re.match(r'^\|[\s:|-]+\|$', st):                       # separator row
            continue
        if st.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            continue                                                  # header row
        out.append(line)
    return _norm('\n'.join(out))


def _occurrences(full, snippet):
    out, i = [], full.find(snippet)
    while i >= 0:
        out.append(i)
        i = full.find(snippet, i + 1)
    return out


def _stack_at(pos, marks):
    stack = None
    for off, st in marks:
        if off > pos:
            break
        stack = st
    if stack and not any(re.search(r'list of|contents|toc-heading', t, re.I) for t in stack):
        return [tidy_case(re.sub(r'\{[^}]*\}', '', t).strip()) for t in stack]
    return None


def _locate(text, full, after):
    """Position of a chunk in the document. Prefer a snippet that occurs exactly once; otherwise the first
    occurrence at or after the previous chunk's position; otherwise the first occurrence."""
    n = _locate_text(text)
    if len(n) < 30:
        return None
    snippets = [n[k:k + 60] for k in sorted({0, len(n) // 4, len(n) // 2, (3 * len(n)) // 4}) if len(n[k:k + 60]) >= 30]
    occ = [o for o in (_occurrences(full, sn) for sn in snippets) if o]
    if not occ:
        return None
    unique = [o[0] for o in occ if len(o) == 1]
    if unique:
        later = [u for u in unique if after is None or u >= after]
        return min(later) if later else min(unique)
    every = sorted(set(x for o in occ for x in o))
    later = [x for x in every if after is None or x >= after]
    return later[0] if later else every[0]


def toc_paths(chunks, md_text):
    """Path per chunk (list of parts) or None; unmatched chunks inherit the previous match.

    Chunks are in document order, so chapter numbers must never go down. A chunk whose text also occurs in
    another chapter can be located in the wrong place; we keep the longest non-decreasing run of chapter
    numbers and treat matches outside it as unmatched.
    """
    full, marks = heading_index(md_text)
    raw, pos = [], None
    for c in chunks:
        p = None
        if c.get('type') == 'diagram' and c.get('caption'):
            # diagram text is derived from the flowchart and is not in the source: use its caption heading
            cap = clean_part(c['caption'])
            p = next((off for off, st in marks if (pos is None or off >= pos) and _similar(st[-1], cap)), None)
        if p is None:
            p = _locate(c['text'], full, pos)
        if p is not None:
            pos = p
        raw.append(_stack_at(p, marks) if p is not None else None)
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
