exec(open('batches/prep_common.py').read())
CB = CH2 + " > 2.3 CAB-LA Injectable PrEP"
LN = CH2 + " > 2.4 LEN Injectable PrEP"
ITEMS = [
 T("tbl-cab-la-drug-interactions", 26, CB + " > CAB-LA and Other Drug Interactions", "Table 6. CAB-LA (cabotegravir) drug interactions: anticonvulsants and rifampicin/rifapentine contraindicated; hormones safe; methadone, rifabutin, high-dose aspirin cautions", ["0057", "0058"],
   [[C("Drug"), C("Interaction")]],
   [{"section": "CAB-LA should not be co-administered"},
    [L("Anticonvulsants: carbamazepine", "oxcarbazepine", "phenobarbital", "phenytoin"), L("Significant reduction of cabotegravir concentrations in blood plasma and therefore decreasing its efficacy.", "These drugs should not be co-administered with CAB-LA; clients using them may need to select a different PrEP method or HIV prevention strategy.")],
    [L("Antimycobacterial medications: rifampicin", "rifapentine"), L("Significant reduction of cabotegravir concentrations in blood plasma and therefore decreasing its efficacy.", "These drugs should not be co-administered with CAB-LA; clients using them may need to select a different PrEP method or HIV prevention strategy.", "CAB-LA can be considered two weeks after a client completes rifampin or rifapentine.")],
    {"section": "Safe to co-administer"},
    r("Contraceptive hormones; gender-affirming hormones", "No known interactions"),
    {"section": "Clients may still be eligible for CAB-LA, but additional cautions may be warranted"},
    r("Methadone; rifabutin", "Clients could require medication dose adjustments to maintain the effectiveness of these medications while they are using CAB-LA."),
    r("High-dose aspirin (>325 mg)", "Clients using high-dose aspirin in the past week, other nonsteroidal anti-inflammatory drugs for pain, or anticoagulants or other antiplatelets may have a higher likelihood of bruising or bleeding at the injection site and should be made aware and counselled on mitigation strategies, if relevant.")],
   pages=[26, 27]),
 D("fig-len-initiation-schedule", 29, LN + " > Starting LEN", "LEN (lenacapavir) initiation and dosing schedule: day 1 two subcutaneous injections + 2 oral tablets, day 2 two oral tablets, follow-up injections every 6 months (±14 days); injection sites and angle (Figure 8)", ["0067"],
   "Initiation (Day 1): provider gives initiation injection 1 and initiation injection 2 (each 1.5 ml / 463.5 mg, subcutaneous) in separate preferred injection sites; client takes 2 oral LEN loading tablets (2 × 300 mg).\n"
   "Initiation (Day 2): client takes another 2 oral LEN loading tablets.\n"
   "Follow-up: two subcutaneous injections every 6 months (26 weeks), ±14 days (window 24–28 weeks).\n"
   "Injection technique (diagram): needle 22-gauge (1.27 cm) for most clients; inject subcutaneously into the abdomen (preferred; at least 5 cm from the navel, second injection at least 10 cm from the first) or the thigh (alternative); insert the needle fully, 90° angle preferred, 45° acceptable; choose an area with enough skin to pinch and avoid intradermal injection.",
   ["The injection-site diagram labels the distance from the navel as 'at least 2 inches', the text as 'at least 5 cm'."], pages=[29, 30]),
 D("fig-len-bridging", 31, LN + " > Bridging for an Anticipated Delayed Follow-up Injection", "Figure 9. Maintaining LEN concentrations with oral bridging (LEN 300 mg weekly) when a follow-up injection will be delayed; restart from Day 1 if >28 weeks", ["0072"],
   "Figure 9 (curve of mean LEN plasma concentration over 65 weeks, log scale):\n"
   "- LEN for PrEP initiation regimen on Day 1 and Day 2 (injections + oral loading) keeps concentrations above the protective level (IQ4).\n"
   "- If the next injection cannot be given within the 24–28-week window: oral bridging with LEN 300 mg PO once weekly, starting around week 26, keeps concentrations up.\n"
   "- Resume LEN subcutaneous injections 7 days after the last oral LEN dose (gap must not exceed 7 days).\n"
   "- If >28 weeks have elapsed since the last injection and bridging tablets have not been taken, restart LEN for PrEP from Day 1.\n"
   "Bridging is only for exceptional circumstances, for short periods, not exceeding three months.",
   ["The figure is a pharmacokinetic curve with no numeric values to transcribe; the earlier chunk listed week-by-week concentrations that are not in the PDF."]),
 T("tbl-len-drug-interactions", 32, LN + " > LEN and Other Drug Interactions", "Table 7. LEN (lenacapavir) drug interactions: TB rifamycins, anticonvulsants, ketamine contraindicated; supplemental LEN with rifampicin; erectile dysfunction drugs; hormones safe", ["0075", "0076"],
   [[C("Drug"), C("Interaction")]],
   [{"section": "LEN should not be co-administered"},
    [L("Drugs used in the treatment of tuberculosis: rifabutin", "rifampicin", "rifapentine"), L("These drugs cause significant reduction of LEN concentration and therefore decrease its efficacy.", "Clients should not initiate LEN if currently on TB treatment and may need to select a different PrEP or HIV prevention strategy.", "For clients already on LEN and wanting to continue, supplemental LEN can be given to maintain adequate LEN concentrations (see Figure 10).")],
    [L("Medication used in the treatment of epilepsy: carbamazepine", "phenobarbital", "phenytoin"), L("Significant reduction of LEN concentration and therefore decreasing its efficacy.", "These drugs should not be co-administered with LEN; clients using them may need to select a different PrEP method or HIV prevention strategy.")],
    [C("Anaesthetic drugs: ketamine"), L("Ketamine concentrations may increase and may increase side effects associated with ketamine such as respiratory depression and hallucinations.", "This potential interaction may persist after discontinuation of LEN.", "These drugs should not be co-administered with LEN; clients using them may need to select a different PrEP method or HIV prevention strategy.")],
    {"section": "Drug that might need a dose adjustment"},
    [C("Clients already on LEN and newly diagnosed with TB and starting rifampicin"), L("Clients already using LEN when diagnosed with TB can continue LEN, but a dose adjustment needs to be made in consultation with the MO.", "Supplemental LEN dosing for co-administration with rifampicin-based TB regimens consists of repeating the LEN initiation dosing when rifampicin is started (see Figure 10) and continuing supplemental LEN every 6 months until completing TB treatment.")],
    [L("Drugs used in treatment of erectile dysfunction: avanafil", "sildenafil", "tadalafil", "vardenafil"), L("There is a potential interaction which may persist after discontinuation of LEN.", "The concentrations of these drugs may increase; start with a lower than regular dose and work up to higher doses until the desired effect is achieved.", "Dose adjustments should be done by the MO.")],
    {"section": "Safe to co-administer"},
    r("Gender-affirming hormones and hormonal contraceptives", "No known interactions")],
   pages=[32, 33],
   source_flags=["Rifabutin is listed under 'LEN should not be co-administered', while the dose-adjustment row covers only rifampicin; supplemental dosing for rifabutin or rifapentine is not addressed."]),
 D("fig-len-rifampicin", 33, LN + " > LEN and Other Drug Interactions", "Figure 10. Maintaining LEN concentrations during rifampicin-based TB treatment: supplemental LEN doses (repeat initiation dosing) every 6 months alongside routine injections", [],
   "Figure 10 (timeline, January to January): routine LEN use with routine injections every 6 months. When a strong CYP3A inducer (rifampicin) is started (example: March), give supplemental LEN doses – repeat the initiation dosing (first day: injections + 2 tablets; second day: 2 tablets). While the CYP3A inducer continues (>6 months), give supplemental doses every 6 months (example: September) in addition to routine injections (example: June). After the strong CYP3A inducer is stopped (example: November), continue with routine LEN injections only.\n"
   "Text: rifampicin is a strong CYP3A inducer and can reduce LEN concentrations below therapeutic levels. For the duration of concomitant LEN and rifampicin use, give routine LEN doses (6 months apart) and supplemental LEN doses (6 months apart). Repeating LEN initiation dosing (SC and PO) beginning Day 3 of LEN for PrEP maintains target LEN concentrations when rifampicin is started no sooner than 2 days after starting LEN for PrEP."),
]
