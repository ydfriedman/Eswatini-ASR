exec(open("batches/hiv_common.py").read())
# HIV 2022 part 5, pp.304-306 (Annexes 11.27 Adverse drug reaction report form, 11.28 Causes of treatment failure). From the page images.
AN = "Chapter 11: Annexes"
ITEMS = [
 B("box-11.27-adr-report-form", 304, AN + " > 11.27 Adverse Drug Reaction Report Form", "Annex 11.27 Adverse Drug Reaction Report Form", ["0813", "0814", "0815", "0816", "0817", "0818"],
   "The report can be returned to Central Medical Stores by Fax: 2518 6279 or via Whatsapp on +268 7655 7303. Email: cms@realnet.co.sz. Post: Adverse Drug Reaction, Central Medical Stores. P.O. Box 72, Kwaluseni.\n\n"
   "Section A: Patient Information: patient initials or reference number; sex (male/female); pregnant (no/yes/unknown); weight (if known) kg; date of birth (dd/mm/yyyy) or age (at last birthday).\n"
   "Section B: Medication History: table of all drug therapies/vaccines before ADR (please use trade names and circle the suspected drug) with batch number, daily dosage, route, date begun, date stopped, indication for use. Allergies or other relevant histories (including medical history, liver/kidney problems, smoking, alcohol use, etc.).\n"
   "Section C: About the Adverse Drug Reaction: date of onset of ADR (dd/mm/yyyy); description of event. Category of ADR (please tick): suspect minor/major reaction from a drug (e.g., allergic reaction); adverse event (e.g., congenital defects); product use error (e.g., use of antibiotic instead of NSAID). Severity (can tick more than one if appropriate): life-threatening; hospitalization (dd/mm/yyyy); hospitalization NOT required. Relevant laboratory result.\n"
   "Section D: Treatment and Outcomes: treatment of ADR (no/yes); details (including dosage, frequency, route, and duration). Outcome: recovered on (dd/mm/yyyy); not yet recovered; unknown; died on (dd/mm/yyyy); persistent disability; birth defect; medically significant events; details.\n"
   "Section E: Reporter Details: name; director of the service (private/public); occupation (doctor, dentist, pharmacist, nurse, other); correspondence address; telephone number; fax number; email; also report to: manufacturer / distributor/importer / others; date of this report (dd/mm/yyyy).\n\n"
   "Instructions/ Notes:\n1. ADR can be briefly described as a noxious and unintended response to a drug or vaccine when the normal dose is used\n"
   "2. This report form is used for voluntary of all suspected ADR\n3. There is no need to put down the full name of the patient\n"
   "4. Please provide information to every section, information of individual reporter will be treated with strict confidence\n"
   "5. Please use another page for additional information if necessary\n6. For further enquiries, please contact the Pharmacist at Central Medical Stores at 2518 4111\n"
   "*Completion of this form is not an admission of guilt or negligence",
   pages=[304, 305]),
 T("tbl-11.28-causes-of-treatment-failure", 306, AN + " > 11.28 Causes of treatment failure", "Annex 11.28 Causes of treatment failure", ["0819", "0820", "0821", "0822"],
   [r("Cause", "Intervention")],
   [{"section": "Medical conditions"},
    r("Comorbidities<br/>Malabsorption<br/>Inter-current illnesses<br/>Advanced immunodeficiency (AHD)", "Consult experienced clinician<br/>Treat current illness following national guidelines<br/>Conduct thorough screening of OIs before ART initiation<br/>Follow AHD guidelines<br/>Assure of correct doses of treatment at every visit"),
    r("Substance use disorder<br/>Depression *", "Consult social worker/psychologist<br/>Consult the psychiatrist and refer if necessary"),
    r("Transmitted resistance", "Counsel patient and trace index contacts<br/>Switch to an appropriate regimen<br/>Identify previous ARV exposure before ART initiation"),
    r("Toxicity or side effects<br/>Drug-drug interactions", "Manage according to the severity of the side effect (see chapter 5, Section 5.12 on pharmacovigilance)<br/>Stop offending drug(s) if necessary<br/>Follow national guidelines when prescribing<br/>Ask about drug history at each refill"),
    {"section": "Psychosocial factors"},
    r("Forgetfulness<br/>Absence of social support<br/>Stigma<br/>Lack of disclosure", "Engage treatment supporter<br/>Home visits<br/>Engage community health care workers"),
    r("Migration and relocation<br/>Unfavourable working hours", "Ensure adequate supply when travelling<br/>Enrol into DSD if eligible"),
    r("Misinformation from the community", "Document presented issues and engaged the APS/health promotion focal persons"),
    r("Poor storage conditions", "Ensure optimal storage conditions of the drug formulations before prescribing MMD"),
    {"section": "Health System Factors (Management)"},
    r("Drug stockouts<br/>Incorrect regimen and drug doses<br/>VL regimen stock out", "Capture correct patient medical data in the correct data collection tools.<br/>Verify M&E data before quantification"),
    r("Service Accessibility", "Encourage patients to access services at their nearest health facilities<br/>Conduct ART readiness assessment before ART initiation<br/>Aim to provide patient-centred care<br/>Conduct routine VL monitoring and use the HVL register effectively")],
   footnotes=["* Follow the PHQ9 screening tool on Annex 0 for Depression screening and manage appropriately (the PHQ-9 is Annex 11.24; 'Annex 0' is a broken cross-reference)."]),
]
