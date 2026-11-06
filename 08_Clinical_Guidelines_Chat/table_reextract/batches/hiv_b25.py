# HIV 2022 part 3 (pp.143-198): where the 2024 Amendment supersedes this content (Amendment Chapters 7-8). Matches items by id or
# heading; appends a source flag. Loaded after hiv_t03.
import copy as _c, json as _j, re as _re
_all = _j.load(open('hiv-2022_tables.json'))['tables']
A = "Superseded by the 2024 Amendment: "
VL = A + "viral suppression is now VL <200 copies/mL; low-level viraemia 200-999 (blips 50-200 are watched, not switched); adherence counselling for any VL >200; first routine VL 3 months after (re)initiation and again at 9 months, then annually for adults and every 6 months for children, adolescents, pregnant and breastfeeding women and 3rd-line clients; pretreatment VL for new initiators only (Amendment Chapter 7, Figures 7.1-7.3)."
PREG = A + "same-day management of viraemia (VL >50) in pregnant and breastfeeding women: intensive adherence interventions, same-day genotype if VL >1000 on DTG >18 months, empiric DRV/r or ATV/r added to TLD for a 3rd-trimester or second detectable VL, and DR-committee consultation if VL stays >50 after 1 month (Amendment Chapter 8, Figures 8.1-8.2)."
SERO = A + "breastfeeding infants of mothers found to have seroconverted get 3-drug PEP after appropriate testing (Amendment Chapter 8)."
RULES = [
 (r'fig-7\.2-vl-cd4|fig-7\.3-vl-testing|tbl-7\.8-vl-interp|fig-7\.4-high-vl|tbl-7\.7-lab-monitoring|7\.10\.2 Viral load monitoring|Point of care viral load|7\.10\.3 Management of a high|Treatment Failure$|Management of Virological Failure', VL),
 (r'tbl-8\.7-hiv-positive-anc|tbl-8\.8-follow-up|fig-8\.1-vl-cd4-pregnant|tbl-8\.9-detectable-vl|8\.4\.4 Viral load', PREG),
 (r'tbl-8\.15-eip-special|fig-8\.3-infant-testing-approach', SERO),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('hiv-2022-') or not (143 <= t['page'] <= 198):
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
