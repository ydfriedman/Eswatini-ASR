"""Build the prioritised source-issue list for clinician review from ../SOURCE_ISSUES.md and tiers.json.
Run from 08_Clinical_Guidelines_Chat/:  python3 source_issues_review/build_priority.py

tiers.json gives each issue (keyed by its exact text in SOURCE_ISSUES.md) a tier, assigned by reading it:
1A could harm a patient if followed as printed; 1B guidelines disagree or are unclear on a clinical decision;
2 clarify; 3 editorial. "group" links issues that are the same problem reported more than once.
Notes that need no clinical review are listed in no_review_flags.json; table_reextract/make_source_issues.py leaves
them out of SOURCE_ISSUES.md (they stay in the table data)."""
import csv, json, re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TIERS = {}
for e in json.loads((HERE / 'tiers.json').read_text(encoding='utf-8')):
    TIERS.setdefault(e['issue'], (e['tier'], e['group']))

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

# Remove notes about how the text was extracted; clinicians only need what the guideline says.
CLEAN = [
    ("; '[Breakfast]' and '[Evening]' are inferred from their text", ''),
    (" The old chunk had 2¼ and 4¼ for B and 2¼ for C (5-9).", ''),
    (", as written here", ''),
    (" Cleaned up here; the order of the overflow text was inferred.", ''),
    ("it is read here as applying to all three diagnoses", 'it presumably applies to all three diagnoses'),
    (" The earlier chunk wrongly sent it to 'further clinical evaluation'.", ''),
    ("; the earlier chunk omitted the branch", ''),
]

def load():
    rows, doc, missing = [], None, []
    for ln in (HERE.parent / 'SOURCE_ISSUES.md').read_text(encoding='utf-8').splitlines():
        if ln.startswith('## '):
            doc = ln[3:].split(' (')[0].strip()
            continue
        if ln.startswith('| ') and not ln.startswith('| Page') and not ln.startswith('|---'):
            cells = [c.strip() for c in ln.strip().strip('|').split(' | ')]
            if len(cells) >= 3 and re.match(r'^[0-9]', cells[0]):
                raw = ' | '.join(cells[2:])
                if raw not in TIERS:
                    missing.append(raw[:100])
                    continue
                tier, group = TIERS[raw]
                issue = raw
                for old, new in CLEAN:
                    issue = issue.replace(old, new)
                item = re.sub(r'\s*\(`[^`]+`\)\s*$', '', cells[1]) or '(text section)'
                rows.append(dict(n=len(rows) + 1, tier=tier, group=group, document=DOCS[doc], page=cells[0],
                                 item=item, issue=issue))
    assert not missing, 'issues with no tier in tiers.json: ' + ' || '.join(missing)
    by_group = defaultdict(list)
    for r in rows:
        if r['group']:
            by_group[r['group']].append(r['n'])
    for r in rows:
        r['see_also'] = ', '.join(f'#{m}' for m in by_group.get(r['group'], []) if m != r['n'])
    return rows

TIER_TEXT = {
    '1A': 'Could harm a patient if followed as printed',
    '1B': 'Guidelines disagree or are unclear on a clinical decision',
    '2': 'Confusing or inconsistent; a clinician would probably read it correctly',
    '3': 'Editorial: typos, captions, numbering, cross-references, layout',
}

def main():
    rows = load()
    with open(HERE / 'source_issues_tiered.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['issue_no', 'tier', 'tier_meaning', 'document', 'pdf_page', 'table_or_section', 'issue', 'see_also',
                    'clinician_decision', 'correct_reading', 'send_to_authors', 'reviewer', 'comments'])
        order = {'1A': 0, '1B': 1, '2': 2, '3': 3}
        for r in sorted(rows, key=lambda r: (order[r['tier']], r['document'], r['n'])):
            w.writerow([r['n'], r['tier'], TIER_TEXT[r['tier']], r['document'], r['page'], r['item'], r['issue'],
                        r['see_also'], '', '', '', '', ''])
    counts = Counter(r['tier'] for r in rows)
    md = ['# Source issues: priority list for clinical review', '',
          f'The guideline documents behind the chat contain {len(rows)} issues found while checking every table, '
          'flowchart and text section against the PDFs (full list: `../SOURCE_ISSUES.md`). They are errors or '
          'inconsistencies **in the guidelines themselves**. Each was read and sorted by how much it could matter to a '
          'patient:', '',
          '| Tier | Meaning | Issues |', '|---|---|---|']
    for t in ('1A', '1B', '2', '3'):
        md.append(f'| {t} | {TIER_TEXT[t]} | {counts[t]} |')
    md += ['', f"**Suggested review:** Tier 1A first ({counts['1A']} issues), then Tier 1B ({counts['1B']}). Tier 2 can be "
           'reviewed by programme leads as time allows; Tier 3 is for the guideline editors. '
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
    md += ['## Tiers 2 and 3', '', 'Listed in `source_issues_tiered.csv` (and in full in `../SOURCE_ISSUES.md`). '
           'By document:', '', '| Document | 1A | 1B | 2 | 3 |', '|---|---|---|---|---|']
    per = defaultdict(Counter)
    for r in rows:
        per[r['document']][r['tier']] += 1
    for d in sorted(per):
        c = per[d]
        md.append(f"| {d} | {c['1A']} | {c['1B']} | {c['2']} | {c['3']} |")
    (HERE / 'PRIORITY_REVIEW.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(dict(counts))

main()
