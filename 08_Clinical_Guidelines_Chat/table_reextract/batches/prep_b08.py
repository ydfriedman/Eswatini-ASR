exec(open('batches/prep_common.py').read())
ITEMS = [
 B("box-creatinine-clearance-apri", 55, CH4 + " > 4.1 Management of Clients with Elevated Creatinine Levels", "Boxes 15-17. Creatinine clearance formula (Cockcroft-Gault, µmol/L: ×1.23 men, ×1.04 women), management of creatinine elevation on oral PrEP, causes of renal insufficiency, APRI score for hepatitis B", ["0138"],
   "Box 15. Calculating creatinine clearance (ml/min):\n- Male: (140 − age) × weight in kg × 1.23 ÷ serum creatinine (µmol/L)\n- Female: (140 − age) × weight in kg × 1.04 ÷ serum creatinine (µmol/L)\n"
   "In case of creatinine elevation:\n- Stop oral PrEP if creatinine elevation is confirmed and estimated creatinine clearance decreases to <60 ml/min.\n- Evaluate for additional causes of creatinine elevation and manage in consultation with the medical officer (MO).\n- After oral PrEP is stopped, check creatinine for another one to three months; oral PrEP can be restarted if CrCl returns to >60 ml/min.\n"
   "Box 16. Common causes of chronic or severe renal insufficiency: diabetes mellitus; uncontrolled systemic hypertension; pre-eclampsia during pregnancy; hepatitis C infection; liver failure.\n"
   "Box 17. APRI score (hepatitis B, section 4.2): APRI = [AST level ÷ AST upper limit of normal] ÷ platelet count (10⁹/L) × 100.",
   ["The creatinine clearance and APRI formulas are printed as images only (no text layer).", "'Evaluate for additional causes of creatinine elevations (see Box 12)' – Box 12 is about AHI; the causes are in Box 16."]),
 D("fig-seroconverters", 57, CH4 + " > 4.3 HIV Seroconversion", "Figure 14. Identifying and reporting PrEP seroconverters: current PrEP client (≤3 or >3 months since initiation), previous PrEP client, no PrEP history – what to document; genotype for CAB-LA/LEN tail period", ["0144", "0145"],
   "HIV-positive client:\n"
   "- Current PrEP client, PrEP initiation ≤3 months ago: document as missed AHI in the PrEP register / CMIS; document previous PrEP exposure in the ART chronic care file / CMIS.\n"
   "- Current PrEP client, PrEP initiation >3 months ago: document PrEP seroconverter in the PrEP register / CMIS; document previous PrEP exposure in the ART chronic care file / CMIS.\n"
   "- Previous PrEP client who tested HIV negative after stopping PrEP: document seroconverter after PrEP discontinuation in the PrEP register / CMIS; document previous PrEP exposure in the ART chronic care file / CMIS.\n"
   "- No history of PrEP use: document no previous ARV exposure in the ART chronic care file / CMIS.\n"
   "Note: all clients testing HIV positive should be initiated on the first-line recommended ART regimen regardless of previous PrEP/PEP exposure. A genotype test for HIV drug resistance should be taken for clients seroconverting during the CAB-LA or LEN tail period.",
   ["Section 4.3 says genotyping should be done for all PrEP seroconverters and anyone exposed to CAB-LA in the last 12 months; the note under Figure 14 limits it to seroconversion during the CAB-LA or LEN tail period."]),
 B("box-pbfw-opt-out", 58, CH4 + " > 4.6 Pregnancy and Breastfeeding", "Box 19. PrEP as a routine opt-out approach for pregnant and breastfeeding women at ANC, maternity and PNC (eMTCT)", ["0148"],
   "Box 19. PrEP should be provided routinely as an opt-out approach at ANC, maternity and PNC services.\n- HIV prevention, including PrEP, is a key intervention in the elimination of mother-to-child HIV transmission (eMTCT).\n- PrEP has been shown to be very effective in reducing HIV acquisition and is also safe among PBFW.\n- Universal PrEP provision, using an opt-out approach, is thus part of the national eMTCT strategy."),
]
