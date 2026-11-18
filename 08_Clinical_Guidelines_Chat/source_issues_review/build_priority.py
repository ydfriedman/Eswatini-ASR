"""Build the prioritised source-issue list for clinician review from ../SOURCE_ISSUES.md and tiers.py.
Run from 08_Clinical_Guidelines_Chat/:  python3 source_issues_review/build_priority.py"""
import csv, re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
exec((HERE / 'tiers.py').read_text())          # defines T: issue number -> tier

DOCS = {
    'HIV Amendment 2024': 'HIV Management Amendment 2024',
    'NCDIMH': 'NCDs, Injuries and Mental Health Guidelines 2025',
    'Text sections': 'NCDs, Injuries and Mental Health Guidelines 2025',
    'PrEP Implementation Guidelines 2025': 'PrEP Implementation Guidelines 2025',
    'ANC Guidelines': 'Antenatal Care Guidelines',
    'UNAIDS Linkages SOP': 'Enhanced Linkages Case Management SOP 2021',
    'TB Guidelines 2025': 'Integrated TB Management Guidelines 2025',
    'Family Planning Guidelines 2021': 'Family Planning Services Guidelines 2021',
    'Mental Health Desk Guide': 'Mental Health Desk Guide 2022',
    'HIV Integrated Management Guidelines 2022': 'Integrated HIV Management Guidelines 2022',
    'STI and Viral Hepatitis Guidelines': 'STI and Viral Hepatitis Guidelines 2026 (draft)',
}

# Tier 1A: could harm a patient if followed as printed (wrong dose, drug, route or emergency step).
# The rest of tier 1 is 1B: the guidelines disagree, or are unclear, on a clinical decision.
TIER_1A = set(int(n) for n in '''38 42 46 70 78 81 89 95 110 113 119 120 121 124 125 126 130 134 154 158 172 185 195 248
    250 252 307 308 322 336 340 341 359 381 385 388 394 395 535 538 541 603 622 689 695 713 728 749 763 766 772 773
    780 788 789 790 791 799 808 819 148 306 320 356 379 380'''.split())

# The same problem reported more than once (often in different documents): shown as "see also".
GROUPS = [(4, 5), (15, 18), (32, 33, 34), (36, 794), (44, 45), (110, 125), (113, 808), (248, 250), (327, 520),
          (379, 380), (394, 395), (441, 610, 614), (541, 622), (749, 772, 773), (790, 791), (235, 741), (13, 402),
          (756, 782, 785, 786), (307, 308), (209, 210), (162, 163)]
SEE_ALSO = defaultdict(list)
for g in GROUPS:
    for n in g:
        SEE_ALSO[n] += [m for m in g if m != n]

# Remove notes about how the text was extracted; clinicians only need what the guideline says.
CLEAN = {
    32: ("; '[Breakfast]' and '[Evening]' are inferred from their text", ''),
    108: (" The old chunk had 2¼ and 4¼ for B and 2¼ for C (5-9).", ''),
    146: (", as written here", ''),
    162: (" The chat repeated it as written.", ''),
    163: (" The chat answers from whichever it retrieves.", ''),
    240: (" Cleaned up here; the order of the overflow text was inferred.", ''),
    247: ("it is read here as applying to all three diagnoses", 'it presumably applies to all three diagnoses'),
    280: (" The earlier chunk wrongly sent it to 'further clinical evaluation'.", ''),
    316: ("; the earlier chunk omitted the branch", ''),
}

def load():
    rows, doc = [], None
    for ln in (HERE.parent / 'SOURCE_ISSUES.md').read_text(encoding='utf-8').splitlines():
        if ln.startswith('## '):
            doc = ln[3:].split(' (')[0].strip()
            continue
        if ln.startswith('| ') and not ln.startswith('| Page') and not ln.startswith('|---'):
            cells = [c.strip() for c in ln.strip().strip('|').split(' | ')]
            if len(cells) >= 3 and re.match(r'^[0-9]', cells[0]):
                n = len(rows) + 1
                issue = ' | '.join(cells[2:])
                if n in CLEAN:
                    old, new = CLEAN[n]
                    assert old in issue, n
                    issue = issue.replace(old, new)
                item = re.sub(r'\s*\(`[^`]+`\)\s*$', '', cells[1]) or '(text section)'
                tier = T[n]
                label = {0: '0', 2: '2', 3: '3'}.get(tier) or ('1A' if n in TIER_1A else '1B')
                rows.append(dict(n=n, tier=label, document=DOCS[doc], page=cells[0], item=item, issue=issue,
                                 see_also=', '.join(f'#{m}' for m in SEE_ALSO.get(n, []))))
    assert len(rows) == len(T) == 825, (len(rows), len(T))
    return rows

TIER_TEXT = {
    '1A': 'Could harm a patient if followed as printed',
    '1B': 'Guidelines disagree or are unclear on a clinical decision',
    '2': 'Confusing or inconsistent; a clinician would probably read it correctly',
    '3': 'Editorial: typos, captions, numbering, cross-references, layout',
    '0': 'No clinical review needed: extraction notes, or 2022 HIV text replaced by the 2024 Amendment / 2025 PrEP guidelines',
}

def main():
    rows = load()
    with open(HERE / 'source_issues_tiered.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['issue_no', 'tier', 'tier_meaning', 'document', 'pdf_page', 'table_or_section', 'issue', 'see_also',
                    'clinician_decision', 'correct_reading', 'send_to_authors', 'reviewer', 'comments'])
        order = {'1A': 0, '1B': 1, '2': 2, '3': 3, '0': 4}
        for r in sorted(rows, key=lambda r: (order[r['tier']], r['document'], r['n'])):
            w.writerow([r['n'], r['tier'], TIER_TEXT[r['tier']], r['document'], r['page'], r['item'], r['issue'],
                        r['see_also'], '', '', '', '', ''])
    counts = Counter(r['tier'] for r in rows)
    md = ['# Source issues: priority list for clinical review', '',
          'The guideline documents behind the chat contain 825 issues found while checking every table, flowchart and '
          'text section against the PDFs (full list: `../SOURCE_ISSUES.md`). They are errors or inconsistencies **in '
          'the guidelines themselves**. Each was read and sorted by how much it could matter to a patient:', '',
          '| Tier | Meaning | Issues |', '|---|---|---|']
    for t in ('1A', '1B', '2', '3', '0'):
        md.append(f'| {t} | {TIER_TEXT[t]} | {counts[t]} |')
    md += ['', f"**Suggested review:** Tier 1A first ({counts['1A']} issues), then Tier 1B ({counts['1B']}). Tier 2 can be "
           'reviewed by programme leads as time allows; Tier 3 is for the guideline editors; Tier 0 needs no action. '
           'Some problems appear more than once (the same error in two places, or in two documents); these are '
           'cross-referenced under "See also".', '',
           'Record decisions in `source_issues_tiered.csv` (one row per issue, Tier 1A first, with columns for the '
           'decision, the correct reading, and whether to send it to the guideline authors). Issue numbers follow the '
           'order of `SOURCE_ISSUES.md`.', '']
    for t, title in (('1A', 'Tier 1A: could harm a patient if followed as printed'),
                     ('1B', 'Tier 1B: guidelines disagree or are unclear on a clinical decision')):
        md += [f'## {title}', '']
        by_doc = defaultdict(list)
        for r in rows:
            if r['tier'] == t:
                by_doc[r['document']].append(r)
        for d in sorted(by_doc, key=lambda d: -len(by_doc[d])):
            md += [f'### {d} ({len(by_doc[d])})', '', '| # | PDF page | Table or section | Issue | See also |', '|---|---|---|---|---|']
            for r in by_doc[d]:
                md.append(f"| {r['n']} | {r['page']} | {r['item']} | {r['issue']} | {r['see_also']} |")
            md.append('')
    md += ['## Tiers 2, 3 and 0', '', 'Listed in `source_issues_tiered.csv` (and in full in `../SOURCE_ISSUES.md`). '
           'By document:', '', '| Document | 1A | 1B | 2 | 3 | 0 |', '|---|---|---|---|---|---|']
    per = defaultdict(Counter)
    for r in rows:
        per[r['document']][r['tier']] += 1
    for d in sorted(per):
        c = per[d]
        md.append(f"| {d} | {c['1A']} | {c['1B']} | {c['2']} | {c['3']} | {c['0']} |")
    (HERE / 'PRIORITY_REVIEW.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(dict(counts))

main()
