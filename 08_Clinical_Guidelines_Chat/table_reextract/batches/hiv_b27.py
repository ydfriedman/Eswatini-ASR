exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.208-210 (Chapter 9: first-line, alternative and special-situation regimens for children and adolescents).
# From the page images; text checked against the PDF grid.
C9 = "Chapter 9: ART for Children and Adolescents"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
VLS = "Ensure VL suppressed in the previous 3-6 months OR order urgent/POC VL first"
ITEMS = [
 T("tbl-9.4-first-line-children", 208, C9 + " > 9.5 What to Start: ART for Children and Adolescents > Table 9.4", "Table 9.4 Recommended First-Line ART Regimens for Children and Adolescents", ["0569"],
   [r("Weight/Age", "< 3.0 kg OR <4 weeks old", "≥3-29.9 kg (AND ≥ 4 weeks of age)", "≥ 30 Kg")],
   [r("Regimen", "*AZT + 3TC + NVP (*Holding Regimen)", "ABC + 3TC + DTG", "TDF + 3TC + DTG"),
    [C("Special Considerations"), C("Use Fixed Dose, once-daily combination pills whenever possible.<br/>o *If initiated at <4 weeks of age OR has weight <3 kg for ART initiation:<br/>o Transition to ABC + 3TC + DTG once ≥3kg AND ≥4 weeks of age<br/>See Annex 11.20 for holding regimen dosing guidance or call the clinical mentor/Baylor Hotline<br/>If the neonate is UNWELL, or PREMATURE (<35 weeks gestation), call the clinical mentor/Baylor Hotline (7848-5571)", cs=3)]],
   context_before="Children and adolescents are a priority population. In the absence of severe opportunistic infections like meningitis, initiate ART on the same day and when not possible as soon as the caregiver/child/adolescent is ready, preferably within 7 days (Test and Start), regardless of the availability of baseline results. Before initiating ART, conduct a comprehensive clinical and psychosocial assessment including adherence counselling.",
   footnotes=["See Annex 11.1 for additional information on ARV drugs, Annex 11.17 for the paediatric dosing chart, and Annex 11.19 for special dosing considerations in birth-tested infants."],
   source_flags=["Premature neonates: '<35 weeks gestation' here but '<37 weeks' in Table 9.5.", "Neonatal cut-off: '<3.0 kg' here vs '≤3kg' in Table 9.5, so a 3.0 kg infant falls in different bands."]),
 T("tbl-9.5-alternative-first-line-children", 209, C9 + " > 9.5 > Alternative First-Line ART Regimens for Children and Adolescents > Table 9.5", "Table 9.5 Alternative First-Line ART Regimens for Children and Adolescents", ["0571"],
   [r("Weight/Age", "≤3kg or <4 weeks", "≥3-29.9 kg AND ≥4 weeks of age", "≥ 30 kg")],
   [[C("Regimen"), C("AZT + 3TC + RAL", rs=2), C("AZT + 3TC + DTG<br/>ABC (or AZT) + 3TC + LPV/r<br/>ABC (or AZT) + 3TC + EFV"), C("ABC (or AZT) + 3TC + DTG<br/>TDF (or ABC) + 3TC + EFV 400mg")],
    [C("Special Considerations"), C(B_("EFV should not be used in children < 3 years old OR ≤ 10kg", "In line with ART optimization efforts, NNRTIs should be avoided whenever possible", "LPV/r solid formulations (tablets) should be used as soon as the child can swallow", "LPV/r tablets should never be cut, split, dissolved, chewed or crushed.", "ATV/r can be used instead of LPV/r in children ≥40kg"), cs=2)],
    [C("If the neonate is UNWELL, or PREMATURE (<37 weeks gestation), call the clinical mentor/Baylor Hotline (7848-5571)", cs=4)]]),
 T("tbl-9.6-special-situations-children", 209, C9 + " > 9.5 > Table 9.6 Special Situations for Children and Adolescent", "Table 9.6 Special Situations for Children and Adolescent", ["0572", "0573"],
   [r("Special Situation", "Age/Weight", "ARV Recommended or Substitution", "Comments")],
   [[C("ABC hypersensitivity reaction (rare)", rs=2), C("< 30 kg"), C("AZT"), C("Ensure Hb > 10 g/dL")],
    r("≥ 30 kg", "TDF", "Do not use TDF if: confirmed and/or suspected renal dysfunction (CrCl <50 mL/min)<br/>Use with caution in the presence of nephrotoxic drugs"),
    [C("Anaemia while taking AZT (Hb<10 g/dL)", rs=2), C("< 30 kg"), C("ABC"), C("Do not rechallenge if there is a history of ABC hypersensitivity and consult with an experienced clinician")],
    r("≥ 30 kg", "TDF", "See above"),
    [C("LPV/r (gastrointestinal side effects)", rs=3), C("≥ 3 kg and 4 weeks of age"), C("DTG*"), C(VLS + "<br/>Case-by-case basis, consult with a doctor or call the Baylor HIV/ TB Hotline (7848-5571)", rs=3)],
    r("≥ 3 years OR ≥ 10 kg", "DTG (Preferred)*<br/>EFV*"), r("≥ 40 kg", "ATV/r"),
    [C("Caregiver unable to correctly dose LPV/r granules", rs=2), C("≥ 3 kg and 4 weeks of age"), C("DTG (Preferred)<br/>LPV/r Tablets"), C("LPV/r Tablets can NOT be crushed, chewed or broken so only appropriate if the child can swallow them whole.")],
    r("≥ 3 years OR ≥ 10 kg", "DTG (Preferred)<br/>EFV", VLS + " and consult Baylor HIV/ TB Hotline (7848-5571) OR snapthirdline@mohcoag.org"),
    [C("Unable to tolerate EFV (severe central nervous system side effects or moderate to severe rash); psychiatric history of EFV side effects", rs=2), C("≥ 3 kg"), C("DTG (preferred)<br/>LPV/r (granules/tablets)"), C(VLS + ". On a case-by-case basis, consult with a doctor or call the Baylor HIV/TB Hotline (7848-5571)", rs=2)],
    r("≥ 40 kg", "DTG (preferred)<br/>ATV/r<br/>*DRV/r"),
    [C("Unable to tolerate DTG", rs=2), C("< 3 years OR <10 kg"), C("LPV/r granules"), C(VLS)],
    r("≥ 3 years OR ≥ 10 kg", "LPV/r (granules or tablets)<br/>EFV<br/>*DRV/r", "LPV/r Tablets CANNOT be crushed, chewed or broken so only appropriate if the child can swallow them whole.")],
   pages=[209, 210], footnotes=["*Prescription of DRV/r is guided by genotype results, consult HIVDR clinical expert committee"],
   source_flags=["The footnote explains * as DRV/r, but * is also printed on DTG and EFV in the LPV/r side-effect rows.", "Age/weight cut-offs mix 'AND' and 'OR' (≥3 years OR ≥10 kg for EFV) while Table 9.5 says EFV is not used under 3 years OR ≤10 kg."]),
]
