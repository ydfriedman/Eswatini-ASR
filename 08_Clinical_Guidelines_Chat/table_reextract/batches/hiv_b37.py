# HIV 2022 part 4 (pp.199-263): where the 2024 Amendment supersedes this content (Amendment Chapters 9-10). Matches items by id or
# heading; appends a source flag. Loaded after hiv_t04.
import copy as _c, json as _j, re as _re
_all = _j.load(open('hiv-2022_tables.json'))['tables']
A = "Superseded by the 2024 Amendment: "
PRES = A + ("any ill-appearing HIV-exposed child <5 years is at risk of advanced HIV disease: if same-day HIV diagnostics are exhausted, start ART "
            "presumptively while awaiting PCR results, sending two DNA PCR samples before initiation (no need to await results); the Amendment lists the "
            "criteria for a presumptive diagnosis of severe HIV disease (Amendment 9.1).")
PALD = A + ("paediatric ABC/3TC/DTG 60/30/5 mg dispersible fixed-dose tablet (pALD) is added for children 6-24.9 kg; separate ABC/3TC + pDTG remain for "
            "children 3-5.9 kg, children on rifampicin-based TB treatment, and 2nd/3rd-line clients not previously on DTG. Use the updated paediatric "
            "dosing chart (Amendment 9.2, Annex 11.17).")
TPT = A + ("TPT dosing chart for CALHIV added: on DTG or EFV, 3HP + vitamin B6 preferred for ≥14 years and ≥30 kg, 6H + B6 preferred for <14 years or "
           "<30 kg (TPT under 12 months only with a new known pulmonary TB contact); on PI-based ART, 6H (Amendment 9.3). See also the 2025 TB guidelines.")
TBART = A + ("ART changes for children starting TB treatment while on ART: DTG to twice daily; LPV/r to DTG if DTG-naive, otherwise super-boosted LPV/r; "
             "DRV/r or ATV/r replaced by DTG (DTG-naive) or LPV/r (DTG-experienced); neonates on NVP switched to DTG or LPV/r; all dose adjustments kept "
             "for 2 weeks after TB treatment ends (Amendment 9.4).")
MMD = A + ("children on ART >1 year with 2 undetectable VLs and clinically stable may have 3-month refills; >2 years with 1 undetectable VL 3-month "
           "refills and with 2 undetectable VLs 6-month refills; stable children on ART >1 year are no longer treated as advanced disease for MMD "
           "(Amendment Figure 9.4).")
VL = A + ("baseline and 3-month VL are additional tests (aligned with child welfare visits): VL at 0, 3, 9 and 15 months, then every 6 months for "
          "ages 0-19, CD4 at baseline, 6 and 12 months; VL suppression is now <200 copies/mL, low-level viraemia 200-999 (Amendment 9.6 and Chapter 7).")
SL = A + ("all DTG and PI treatment failures need a genotype-guided switch: refer to the National HIVDR Clinical Expert Committee and switch to 2nd line "
          "only if the resistance test shows DTG (or PI) resistance, with the regimen set by the genotype; LPV/r can be changed to ATV/r once ≥40 kg "
          "regardless of VL; DRV/r only for confirmed INSTI resistance (Amendment 9.7, updated second-line table).")
MH = A + ("the Amendment adds psychological screening for all PLHIV at baseline and within 3 months of diagnosis (depression PHQ-9, suicide risk, "
          "anxiety BAI, substance use ASSIST, social issues), psychological first aid for IPV clients, psychotherapy within SUAC, and escalation of "
          "clients failing treatment to psychological support (Amendment Chapter 10).")
RULES = [
 (r'tbl-9\.1-art-timing|9\.3 When to Start ART', PRES),
 (r'fig-9\.3-treatment-optim|tbl-9\.7-optimize|9\.6 Treatment Optimization|9\.6\.1 Transitioning|Paediatric DTG \(pDTG\)|fig-9-formulation-sequence|tbl-9\.9-optimisation|tbl-9\.4-first-line-children', PALD),
 (r'9\.8 Tuberculosis Preventive Therapy', TPT),
 (r'9\.9 ART for Children and Adolescents with TB|Drug-Sensitive TB/HIV|tbl-9\.6-special-situations', TBART),
 (r'fig-9\.4-follow-up|9\.10 Clinical Monitoring of Children$|Multiple months dispensing|9\.16 Differentiated Service Delivery for children and adolescents$', MMD),
 (r'fig-9\.5-vl-cd4|tbl-9\.11-repeat-vl|9\.11 Laboratory Monitoring.*Viral Load|tbl-9\.19-monitoring|tbl-9\.8-vl-guided|tbl-9\.12-failure-def|9\.12 Managing Treatment Failure in Children and Adolescents$', VL),
 (r'tbl-9\.15-second-line|box-9\.12\.1-second-line|9\.12\.1 Second-Line ART for Children and Adolescents > When to Switch|fig-9\.7-treatment-failure', SL),
 (r'10\.6 Care and Management of Depression and HIV$|tbl-10\.7-depression', MH),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('hiv-2022-') or not (199 <= t['page'] <= 263):
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if any(f.startswith(A[:-2] + ' (Chapter 7)') for f in t.get('source_flags', [])):
        notes = [n for n in notes if n is not VL]          # already carries the Chapter 7 VL note
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
