exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.225-227 (Chapter 9: second- and third-line ART for children and adolescents). From the page images (merged
# cells of Table 9.15 set from the image).
C9 = "Chapter 9: ART for Children and Adolescents"
ITEMS = [
 T("tbl-9.15-second-line-children", 225, C9 + " > 9.12.1 Second-Line ART for Children and Adolescents > Table 9.15", "Table 9.15 Recommended Second-Line Regimens for Children and Adolescents", ["0618", "0619"],
   [r("Weight", "Current 1st Line", "Preferred 2nd Line", "Alternative 2nd Line")],
   [[C("3-29.9 Kg", rs=6), C("ABC + 3TC + DTG"), C("Regimen guided by genotype", rs=2), C("AZT + 3TC + ᵃPI")],
    r("AZT + 3TC + DTG", "ABC + 3TC + ᵃPI"),
    r("ABC + 3TC + EFV", "AZT + 3TC + DTG", "ABC + 3TC + ᵃPI"),
    r("AZT + 3TC + EFV", "ABC + 3TC + DTG", "ABC + 3TC + ᵃPI"),
    [C("ABC + 3TC + LPV/r"), C("AZT + 3TC + DTG"), C("Consult National HIVDR Expert Clinical Committee and/or Baylor Hotline.", rs=2)],
    r("AZT + 3TC + LPV/r", "ABC + 3TC + DTG"),
    [C("≥30 kg", rs=6), C("TDF + 3TC + DTG"), C("Regimen guided by genotype results", rs=3), C("TDF + 3TC + ᵃPI<br/>AZT + 3TC + ᵃPI")],
    r("ABC + 3TC + DTG", "AZT + 3TC + ᵃPI"),
    r("AZT + 3TC + DTG", "TDF + 3TC + ᵃPI"),
    [C("TDF + 3TC + EFV"), C("TDF + 3TC + DTG", rs=2), C("AZT + 3TC + ᵃPI<br/>ABC + 3TC + ᵃPI")],
    r("AZT + 3TC + EFV", "TDF + 3TC + ᵃPI"),
    r("ABC + 3TC + EFV", "AZT + 3TC + DTG", "AZT + 3TC + ᵃPI")],
   rhc=2,
   footnotes=["ᵃPI should be chosen based on availability and convenience: DRV can only be used for second line in cases of confirmed INSTI resistance on genotype. It must always be co-administered with ritonavir. It can only be given to children ≥3 years of age and 10 kg. See Annex 11.17 for DRV/r dosing which depends on prior PI exposure. DRV/r CANNOT be co-administered with rifampicin containing TB treatment. DRV should be used with caution in patients with known sulfonamide allergies. ATV/r can only be given if ≥40 kg. LPV/r is given twice daily for all clients >4 weeks and 3kg.",
              "HIV resistance testing should be done for all clients failing on a DTG-based ART regimen. Only switch to 2nd line if the resistance test shows DTG resistance and the 2nd line regimen should be a boosted PI + 2 NRTIs determined by the genotype results.",
              "Use of ATV/r 300/100 mg in second line: ATV/r should NOT be used with clients on rifampicin; adolescents with TB/HIV coinfection should use super-boosted LPV/r or double-dose LPV/r (LPV/r 800 mg/200 mg twice daily). ATV/r should NOT be used in clients with active hepatitis; pre-existing jaundice or hyperbilirubinaemia may be worsened by ATV/r. Use ATV/r with caution with clarithromycin, hormonal contraceptives, antacids, inhaled steroids, proton pump inhibitors, H2 blockers and lipid-lowering agents; avoid combination with etravirine and NVP. Clinicians can substitute clients on an LPV/r-containing second-line regimen to an ATV/r-containing regimen for all children or adolescents >40 kg."],
   pages=[225, 226],
   source_flags=["'TDF + 3TC + ᵃPI' is listed as an alternative second line for children ≥30 kg failing AZT + 3TC + DTG and AZT + 3TC + EFV, and TDF + 3TC + DTG as preferred after TDF + 3TC + EFV failure (recycling TDF), consistent with adult Table 7.11.",
                 "ATV/r 'only if ≥40 kg' (footnote) vs 'children or adolescents >40 kg' (callout) - 40 kg exactly is ambiguous."]),
 T("tbl-9.16-third-line-children", 227, C9 + " > 9.12.2 Third-Line ART for Children and Adolescents > Table 9.16", "Table 9.16 Potential Third-Line Regimens for Children and Adolescents", ["0624"],
   [r("Age", "Potential Third-Line Regimens")],
   [[C("Children (0-10 years)", rs=3), C("DTG + 2 NRTIs")], r("DRV/r + 2 NRTIs"), r("DRV/r + DTG ± 1-2 NRTIs"),
    [C("Adolescents(10-19 years)", rs=3), C("DRV/r + DTG ± 1-2 NRTIs")], r("DRV/r + 2 NRTIs ± NNRTI"), r("Optimize regimen using genotype profile")],
   footnotes=["DRV/r should not be given to children below 3 years of age"],
   context_before="Evaluation for third-line ART is supported by the Eswatini National HIVDR Clinical Expert Committee; contact the Baylor clinicians in Mbabane, Manzini or Hlatikhulu, the Baylor HIV/TB Hotline or your clinical mentor for each case. Before third line, intensify adherence interventions; if there is still no viral suppression and the client has been on second line >2 years (or was on anti-TB treatment during second line), perform a resistance test while the client is still taking the failing regimen (request form to snapthirdline@mohcoag.org). Genotyping is done for clients failing PI- or DTG-based regimens with VL above 1000 copies/ml and evidence of improved adherence.",
   source_flags=["'Children (0-10 years)' and 'Adolescents (10-19 years)' overlap at 10 years; DRV/r options for children 0-10 conflict with the footnote (not below 3 years)."]),
]
