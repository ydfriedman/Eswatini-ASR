exec(open('batches/tb_common.py').read())
# Flowcharts checked against the page images and found faithful; kept as the old chunk text (minus the 'Diagram:' line) so source flags can be attached.
import json as _j
_old = {}
for _l in open('../chunks_v2/chunks.jsonl'):
    _c = _j.loads(_l)
    if _c['chunk_id'] in ('tb-2025-0470', 'tb-2025-0478', 'tb-2025-0543'): _old[_c['chunk_id'][-4:]] = _c
def _body(k): return '\n'.join(l for l in _old[k]['text'].split('\n') if not l.startswith('Diagram:'))
AE = "Chapter 9: Pharmacovigilance and Adverse Event Management > 9.9 Algorithms for Management of Adverse Events with Second-line Anti-TB Drugs"
ITEMS = [
 D("fig-qtc-management", 186, AE + " > Figure 28: Management of QTc Prolongation", "Figure 28. Management of QTcF prolongation on second-line TB drugs (BDQ, CFZ, MFX, DLM, LFX): ECG monitoring, grades 1-4 and actions, order of stopping drugs", ["0470", "0471"], _body('0470'),
   ["Grade 1 is printed as '45 - 480 msec' (presumably 451-480 msec); grade 4 as '> 501 msec or 60 msec change' (usually >500 msec or >60 msec increase from baseline).", "'CTcF' typo in the drug-stopping note."]),
 D("fig-liver-management", 189, AE + " > Figure 31: Management of Liver Function Abnormalities", "Figure 31. Management of liver function abnormalities on TB drugs (PZA, INH, BDQ, CFZ, Eto, PAS): LFT monitoring, grades 1-4 by ULN, stop and reintroduce drugs, liver-sparing regimen", ["0478", "0479"], _body('0478') + "\nLiver-sparing regimen drugs: EMB, DLM, CS, amikacin (with caution) and likely the FQs. People with underlying liver disease, heavy alcohol use or viral hepatitis should start a modified shorter regimen that includes CS and does NOT include INH or PZA.",
   ["Grade 3 reads '> 5 to 10 ULN or any asymptomatic elevations' – probably 'symptomatic' (drug-induced liver injury is usually ALT >3×ULN with symptoms or >5×ULN without)."]),
 D("fig-tpt-adult-contacts", 210, "Chapter 11: TB Preventive Treatment > 11.6 Ruling out Active TB Disease > Figure 35: HIV-negative Household Contacts >10 Years and Other Risk Groups", "Figure 35. Ruling out active TB before TPT in HIV-negative household contacts >10 years and other risk groups: symptom screen/CXR, TB infection test, start TPT", ["0543"], _body('0543') + "\nNeither CXR nor a TB infection (TBI) test is mandatory to decide to start TPT. Other risk groups: silicosis, immunosuppressive drugs (long steroid therapy, cancer chemotherapy), anti-TNF treatment, transplantation (including candidates), health care workers and offenders.",
   ["An indeterminate TB infection test leads to 'No TPT'; an indeterminate IGRA is usually repeated or the decision made clinically.", "'CXC' printed for CXR."]),
]
