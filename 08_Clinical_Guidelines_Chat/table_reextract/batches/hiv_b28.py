exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.211-215 (Chapter 9: treatment optimisation, formulations, VL-guided transition, CPT). From the page images.
C9 = "Chapter 9: ART for Children and Adolescents"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
VLA = "Superseded by the 2024 Amendment (Chapter 7): suppression <200 copies/mL, low-level viraemia 200-999, VL at 3 and 9 months after (re)initiation then every 6 months for children and adolescents."
ITEMS = [
 T("tbl-9.7-optimize-art", 211, C9 + " > 9.6 Treatment Optimization > Table 9.7", "Table 9.7 Strategies to Optimize ART", ["0575"],
   [r("Optimal ART", "Optimal formulations")],
   [r("Early therapy/ Treatment", "Use of fixed-dose combinations (FDCs) e.g., ABC/3TC (120/60mg) or TLD for older children and adolescents"),
    r("The optimal sequence of new drugs from birth to adolescence", "Age-appropriate formulations (syrup, granules, dispersible tablets, solid tablets, capsules) depend on the age of the infant/child and their ability to swallow"),
    r("Less toxic drug regimens with high barriers to drug resistance", "Flexible administration e.g., dispersible tablets (e.g., pDTG10mg, ABC/3TC (120/60mg)) can be dissolved in liquid and administered to young infants, crushed and swallowed, chewed or swallowed whole"),
    r("Simplified dosing by weight bands", "Heat stable (e.g., LPV/r 125mg tablets)"), r("Harmonizing Paediatric recommendations with adult regimens", "Improved palatability (pDTG 10mg with strawberry taste)")],
   source_flags=["'LPV/r 125mg tablets' as the heat-stable example; the paediatric LPV/r tablet is 100/25 mg (section 9.6.1)."]),
 D("fig-9.3-treatment-optimisation", 211, C9 + " > 9.6 Treatment Optimization > Figure 9.3", "Figure 9.3 Key Components of Treatment Optimization", ["0577"],
   "Treatment optimisation has four components:\n- STARTING children on preferred ART regimens in optimal formulations\n- CHANGING formulations as children grow and can take more optimal formulations\n- TRANSITIONING to better regimens and formulations as improved regimens are available\n- SWITCHING to appropriate 2nd or 3rd line regimens in optimal formulations when VL failure occurs"),
 D("fig-9-formulation-sequence", 213, C9 + " > 9.6.1 Transitioning regimens and formulations in children and adolescents > Sequence of transition to optimal ARV drug formulations", "The sequence of transition to optimal ARV drug formulations for stable children and adolescents", ["0582"],
   "With ABC/3TC 120/60mg scored dispersible tablet:\n1. pDTG 10mg dispersible tablet: cannot swallow tablets whole, >1 month of age, weighs >3kg to <20kg.\n2. DTG 50mg film coated tablet: weighs >20kg and can swallow tablet whole.\n3. TLD: weighs >30kg.\n"
   "It is NOT recommended to co-administer DTG with anticonvulsants such as phenytoin or phenobarbital (consult expert or consider substituting DTG with EFV as alternative). Iron, aluminum, magnesium and calcium-containing medicines bind with and reduce absorption of DTG; if co-administered, DTG should be taken with food to enhance DTG absorption or taken at alternate times (6 hours apart).",
   flags=["pDTG and DTG 50 mg film-coated tablets are not interchangeable (section 9.6.1); DTG 50 mg FCT is for children ≥20 kg ('>20kg' in the figure)."]),
 T("tbl-9.8-vl-guided-transition", 213, C9 + " > 9.6.1 > Transition to optimal ARV drug regimens for stable children and adolescents > Table 9.8", "Table 9.8 General guidance on the use of VL results for clinical decision-making for treatment optimization for CALHIV on ART", ["0584"],
   [r("VL Test Result in the past 6 months", "Consideration", "Action")],
   [r("Undetectable < 200 copies/mL", "The client is adherent and doing well<br/>The client is eligible for substitution to an optimal regimen", "Transition to an optimal regimen immediately"),
    [C("> 200 - 1000 copies/mL (detectable and ≤400 copies/mL)"), C("The client may be experiencing adherence challenges and is at risk of treatment failure", rs=2),
     C("Provide a once-off special counselling session on the day of the visit and repeat the viral load in 3 months<br/>If repeat viral load is >200- 1000 copies/ml, manage as treatment failure (conduct 3 SUAC sessions and repeat viral load in 3 months)<br/>If third VL is still 200 - 1000 copies/mL, refer the client to the doctor/multi-disciplinary team for switching to second-line or third-line therapy")],
    r("> 1000 copies/mL", "Manage as treatment failure (conduct 3 SUAC sessions and repeat VL in 3 months)")],
   source_flags=["Row 2 reads '>200 - 1000 copies/mL (detectable and ≤400 copies/mL)': two contradictory ranges in one cell.", "'Undetectable <200' conflicts with Table 7.8 (undetectable <50).", VLA]),
 T("tbl-9.9-optimisation-stable-calhiv", 214, C9 + " > 9.6.1 > Table 9.9", "Table 9.9 Treatment Optimization Recommendations for stable CALHIV", ["0585"],
   [r("Current 1st Line Regimen", "Weight", "Optimal regimen for transition", "Consideration")],
   [[C("AZT + 3TC + EFV (or NVP)<br/>ABC + 3TC + EFV (or NVP)<br/>ABC + 3TC + LPV/r<br/>AZT + 3TC + LPV/r<br/>TDF +3TC+ EFV", rs=2), C("<30Kg"), C("ABC + 3TC plus DTG"), C("If undetectable, transition immediately. If detectable, manage as treatment failure urgently. If <3kg, OR < 4 weeks of age refer to Table 9.5 for treatment alternatives.", rs=2)],
    r(">30Kg", "TDF+3TC + DTG (TLD)"),
    [C("Children and adolescents on 2nd Line PI-based regimens should be maintained on their regimens. If not suppressed, contact the national HIVDR clinical expert committee (snapthirdline@mohcoag.org) for evaluation of drug resistance and the need for genotyping urgently.", cs=4)]],
   footnotes=["Support for those not ready to transition: discuss the reasons behind their concerns and address them; refill ART for 1 month and ask the client to bring questions to the next visit; be honest and understanding with caregivers."],
   source_flags=["Weight bands '<30Kg' and '>30Kg' leave exactly 30 kg uncovered (Table 9.4 uses ≥30 kg)."]),
 T("tbl-9.10-ctx-children", 214, C9 + " > 9.7 Prophylaxis Therapy for HIV-Exposed or -Infected Infants and Children > 9.7.1 Cotrimoxazole Preventive Therapy (CPT) > Table 9.10", "Table 9.10 Co-trimoxazole Preventive Therapy for Children and Adolescent Clients", ["0587", "0588"],
   [r("Group", "When to start Co-trimoxazole preventive therapy?", "When to discontinue Co-trimoxazole preventive therapy? *")],
   [r("All HIV-exposed infants/ children", "From 6 weeks of age (or at the first encounter with health services, if later than 6 weeks of age)", "HIV-negative status has been confirmed and there is no longer exposure"),
    r("All HIV-infected infants and children up to 5 years of age", "Irrespective of WHO clinical stage or CD4 count or CD4 %", "≥5 years of age and after 1 year on ART if:<br/>" + B_("WHO clinical T-stage 1 or 2", "CD4 count ≥350 cells/mm³ and", "Viral load is undetectable")),
    r("All HIV-infected children ≥ 5 years of age", "WHO clinical stages 3 and 4 irrespective of CD4 OR CD4 ≤350 cells/mm³ irrespective of WHO clinical stage OR Detectable Viral Load irrespective of CD4 count", "≥5 years of age and after 1 year on ART if:<br/>" + B_("WHO clinical T-stage stage 1 or 2", "CD4 count ≥350 cells/mm³ and", "Viral load is undetectable")),
    r("As secondary prophylaxis", "After completion of treatment for Pneumocystis jirovecii pneumonia (PJP)", "<5 years old:<br/>" + B_("Do not stop") + "<br/>≥ 5 years old, stop if:<br/>" + B_("CD4 count ≥350 cells/mm³ and", "Viral load is undetectable"))],
   pages=[214, 215], footnotes=["*Can also be stopped due to adverse drug reactions (See Chapter 5, Section 5.4)"],
   source_flags=["The continuation page is captioned 'Table 9.12' (Table 9.10 continued), so later Chapter 9 tables have duplicate numbers (two Table 9.12s)."]),
]
