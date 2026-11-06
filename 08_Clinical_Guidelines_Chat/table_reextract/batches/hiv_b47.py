exec(open("batches/hiv_common.py").read())
# HIV 2022 part 5, pp.292-294 (Annexes 11.18 Tanner staging, 11.19 birth-tested infants flowchart, 11.20 holding regimen dosing).
# From the page images (the Tanner table is an image; its text is transcribed, the drawings described).
AN = "Chapter 11: Annexes"
ITEMS = [
 T("tbl-11.18-tanner-staging", 292, AN + " > 11.18 Tanner staging", "Annex 11.18 Tanner staging", ["0785"],
   [r("Tanner stage", "Male genital description", "Female pubic hair description", "Breast description")],
   [r("1", "Testicular volume <3ml", "No pubic hair", "Elevation of papilla only"),
    r("2", "Testicular volume <3ml, change in texture to scrotal skin", "Sparse growth chiefly along the labia/base of penis", "Breast bud stage"),
    r("3", "Increase in size of penis with further testicular enlargement", "Darker, coarser, more curled hair", "Enlargement of breast and areola"),
    r("4", "Further enlargment of penis and testicles with development of glans penis", "Adult type hair over a smaller area", "Projection of the areola and papilla"),
    r("5", "Adult size and shape", "Spread to the medial surface of the thighs", "Recession of the areola to the contour of the breast, projection of papilla only")],
   footnotes=["Source: BMJ 2020;368:l6597. The printed table also has drawing columns (male genital appearance, female pubic hair appearance, breast appearance) illustrating each stage."],
   source_flags=["Annex 11.18 Tanner stage 2 gives testicular volume '<3ml' (same as stage 1); stage 2 is usually testicular volume ≥4 ml (>3 ml)."]),
 D("fig-11.19-birth-tested-infants", 293, AN + " > 11.19 Special Dosing Considerations in Birth Tested Infants", "Annex 11.19 Special Dosing Considerations in Birth Tested Infants", ["0787", "0788"],
   "Positive birth HIV PCR test: actively trace and link to care to start treatment ASAP; ensure mother is on ART.\n"
   "- If neonate is UNWELL or PREMATURE (<35 weeks): call Mother Facility Doctor or Baylor Hotline for support.\n"
   "- If neonate ≥35 weeks gestation & STABLE: start ART SAME DAY. Baselines: repeat HIV PCR, FBC & CD4 count/% (if possible).\n"
   "   - If 0-4 weeks old use syrups: AZT (4mg/kg/dose BD) + 3TC (2mg/kg/dose BD) + *NVP (see dosing chart) (*no lead-in needed, see dosing chart). Review at 1 week, 2 weeks & 4 weeks for counseling and *dose adjustments of NVP (see dosing chart).\n"
   "      → At 4 weeks of age: bloods: FBC; start CTX prophylaxis. CHANGE REGIMEN: if ≥3kg: ABC/3TC FDC + DTG; if <3kg: AZT (12mg/kg/dose BD) + 3TC (4mg/kg/dose BD) + NVP (200 mg/m² of BSA/dose BD).\n"
   "   - If ≥4 weeks old but <3kg: AZT (12mg/kg/dose BD) + 3TC (4mg/kg/dose BD) + NVP (200 mg/m² of BSA/dose BD). Optimize to ABC/3TC/DTG once ≥3kg.\n"
   "   - If ≥4 weeks old AND ≥3kg: ABC/3TC FDC + DTG.",
   flags=["Superseded in part by the 2024 Amendment: pALD (ABC/3TC/DTG 60/30/5 mg) is the formulation from 6 kg; separate ABC/3TC + pDTG remain for 3-5.9 kg (Amendment 9.2)."]),
 T("tbl-11.20-holding-regimen-dosing", 294, AN + " > 11.20 Holding Regimen Dosing for Birth Tested Infants", "Annex 11.20 Holding Regimen Dosing for Birth Tested Infants 0-4 weeks old and ≥35 Weeks Gestation (Or after 4 weeks until ≥3kg)", ["0789", "0790"],
   [r("Drug", "Weeks Gestation at Birth", "Current Age (weeks)", "Dose")],
   [[C("AZT", rs=2), C("≥35 Weeks", rs=2), C("0-4 weeks"), C("4 mg/kg/dose BD")], r("≥ 4 weeks", "12 mg/kg/dose BD"),
    [C("3TC", rs=2), C("≥35 Weeks", rs=2), C("0-4 weeks"), C("2 mg/kg/dose BD")], r("≥ 4 weeks", "4 mg/kg/dose BD"),
    [C("*NVP", rs=5), C("≥35 to <37 Weeks", rs=3), C("0-1 week"), C("4 mg/kg/dose BD")], r("1-4 weeks", "6 mg/kg/dose BD"), r("≥ 4 weeks", "⁺200 mg/m² of BSA/dose BD"),
    [C("≥37 Weeks", rs=2), C("0-4 weeks"), C("6 mg/kg/dose BD")], r("≥ 4 weeks", "⁺200 mg/m² of BSA/dose BD")],
   footnotes=["*No NVP lead in dosing needed.", "⁺ Body Surface Area calculator can be found at: mdcalc.com/body-mass-index-bmi-body-surface-area-bsa"]),
]
