exec(open('batches/prep_common.py').read())
D3 = CH3 + " > 3.1 PrEP Delivery Overview"
IV = CH3 + " > 3.2 PrEP Initiation Visit"
ITEMS = [
 T("tbl-community-prep-services", 35, D3 + " > Community-based PrEP Services", "Table 8. Community-based PrEP services: community initiation and referral, community initiation and refill, PrEP ring distribution by community workers", ["0081"],
   [[C("Approach"), C("Description")]],
   [r("Community PrEP initiation and referral", "PrEP can be initiated at community level by trained providers. Clients should be referred and linked to a PrEP service delivery point of their choice for refills."),
    r("Community PrEP initiation and refill", "If a community provider returns to the same community for clinical services, clients can continue to receive PrEP refills in the community."),
    [C("Community PrEP ring distribution by community workers"), C("Community healthcare workers trained and competent in HIVST and PrEP can distribute the PrEP ring to HIV-negative women in the following situations:<br/>- An individual wants to use the ring for HIV prevention.<br/>- An individual is undecided about the preferred PrEP method: a ring can be offered for immediate insertion and the client is encouraged to come to the nearest facility within 4 weeks for either ring refill or switching to another preferred PrEP method.")]]),
 T("tbl-hiv-testing-initiation", 36, IV + " > Component 1: HIV Testing and Counseling", "Table 9. HIV testing services at PrEP initiation: HIVST for oral PrEP/ring, RDT for CAB-LA/LEN, positive or inconclusive results, risk assessment, referral", ["0084"],
   [[C("PrEP initiation steps"), C("Plan of action")]],
   [r("Counselling and information", "Refer to HIV testing services (HTS) guidelines."),
    [C("HIV test (HIV testing services [HTS] guidelines)"), L("An HIV test needs to be performed on the day of PrEP initiation.", "An HIVST is the preferred test for initial screening or prior to oral PrEP or PrEP ring initiation.", "If the HIV test is negative, clients should be linked to HIV prevention services.", "For clients choosing CAB-LA or LEN, a rapid diagnostic test (RDT) is needed prior to PrEP initiation.", "If positive, confirm the HIV-positive result as per the national testing algorithm. Do not initiate the client on PrEP.", "Initiate the client on antiretroviral therapy (ART) as per national guidelines.", "If the test result is inconclusive, defer PrEP and follow the national HIV testing algorithm until a definitive HIV test result has been obtained.")],
    r("Risk assessment", "Assess and discuss risk of acquiring HIV with HIV-negative clients."),
    r("Referral and linkages", "Provide information on HIV prevention services and link to appropriate prevention services. See the HIV Prevention Referral and Linkages Job Aid for detailed guidance.")]),
 B("box-ahi-signs-suspicion", 37, IV + " > Component 2: PrEP Eligibility Assessment > Acute HIV Infection (AHI) Assessment", "Boxes 11-12. Acute HIV infection (AHI): common signs and symptoms, and when to suspect AHI and defer PrEP", ["0087", "0089"],
   "Box 11. Common signs and symptoms of AHI: fever; swollen lymph glands; skin rash; headache; sore throat; aches and pains; mouth sores.\n"
   "Box 12. Suspicion of AHI:\n- If the client has symptoms of AHI (currently or in the past fourteen days) AND has been exposed to HIV in the 14 days prior to the HIV test, defer PrEP and repeat the HIV test after four weeks to reassess HIV status.\n- PEP should be provided if exposure is reported within 72 hours."),
 D("fig-initiation-exposure-ahi", 38, IV + " > Component 2: PrEP Eligibility Assessment > Acute HIV Infection (AHI) Assessment", "Figure 11. PrEP initiation flowchart: HIV test result, exposure in past 72 hours (PEP), AHI symptoms in past 14 days, start PrEP or delay and retest", ["0090", "0091", "0092"],
   "1. Is the client's HIV test result negative?\n"
   "   - No: refer the client to confirmatory testing and HIV treatment.\n"
   "   - Yes: 2.\n"
   "2. Was the client potentially exposed to HIV in the past 72 hours? (⁰)\n"
   "   - Yes: start PEP standard of care (SOC). If PEP is started, retest for HIV in 28 days; if the client is seronegative upon PEP completion, continue with PrEP SOC.\n"
   "   - No: 3.\n"
   "3. Does the client have AHI symptoms now, or have they had AHI symptoms in the past 14 days? (¹)\n"
   "   - No: start PrEP SOC. (²)\n"
   "   - Yes: 4.\n"
   "4. Did the client have a potential exposure to HIV in the 14 days before symptom onset?\n"
   "   - No: start PrEP SOC. (²)\n"
   "   - Yes: the symptoms may be due to AHI (a prevention method was not being used effectively around the time of exposure). Provider and client should weigh the risks and benefits of delaying PrEP initiation and retesting per the national algorithm 28 days from potential exposure, or earlier if HIV testing that can reliably detect HIV is available.\n"
   "Notes: ⁰ 'No' means no potential exposure at all, or exposure 72 or more hours ago. ¹ Two-thirds of people have AHI symptoms within two to four weeks of acquiring HIV; symptoms that mimic AHI (sore throat, fever, sweats, swollen glands, mouth ulcers, headache, rash, muscle aches) are commonly due to other illnesses, so use discretion. ² Before starting PrEP the client should know that the HIV test may not detect HIV acquired fewer than 28 days ago (and possibly beyond 28 days), and that without AHI symptoms they could be pre-symptomatic or among the one-third who never develop symptoms.",
   pages=[38, 39]),
 T("tbl-product-eligibility", 39, IV + " > Component 2: PrEP Eligibility Assessment > Product-specific Eligibility Assessment", "Table 10. Product-specific PrEP eligibility criteria for oral PrEP, PrEP ring, CAB-LA and LEN: follow-up attendance, age ≥16, body weight, pregnancy/breastfeeding, contraindications", ["0093", "0094"],
   [[C("Criterion"), C("Oral PrEP"), C("PrEP ring"), C("CAB-LA"), C("LEN")]],
   [[C("Able/willing to attend PrEP visits"), C("For all products, clients should be committed to attend scheduled follow-up appointments", cs=4)],
    [C("Age"), C("≥16 years*", cs=4)],
    [C("Body weight"), C("≥30 kg", cs=2), C("≥35 kg"), C("≥35 kg")],
    [C("Pregnancy / breastfeeding"), C("All available PrEP products are safe to use in pregnant or breastfeeding women.", cs=4)],
    r("No contraindications for PrEP method", "Not using nephrotoxic medication or having known creatinine clearance <60 ml/min", "Not using vaginally administered antimicrobial products and no allergies to dapivirine", "Not using rifampin, rifapentine, carbamazepine, oxcarbazepine, phenobarbital, phenytoin, and does not have allergy to CAB-LA", "No allergy or previous reaction to LEN")],
   footnotes=["*In case of a mature minor between the age of 12-15 years, oral PrEP can be considered as per the discretion of the healthcare provider."],
   source_flags=["The ≥30 kg weight cell appears to span oral PrEP and the PrEP ring; the PrEP ring is for people assigned female at birth only, which is not repeated here.", "LEN's contraindications in this table omit the drug interactions listed in Table 7 (rifamycins, carbamazepine, phenobarbital, phenytoin, ketamine), while CAB-LA's include them."]),
 T("tbl-prescription-by-method", 40, IV + " > Component 4: PrEP Prescription", "Table 11. PrEP prescription at initiation by method: oral PrEP and ring 3 months + HIVST at 1 month; CAB-LA injection 1 then injection 2 at one month; LEN injections and oral loading", ["0098"],
   [[C("PrEP method"), C("PrEP prescription")]],
   [[C("Oral PrEP (daily or ED)"), L("Maximum 3 months prescription (3 bottles) of TDF/3TC.", "Distribute an HIVST for self-test at 1 month.", "Schedule next visit date after 3 months.")],
    [C("PrEP ring"), L("Maximum 3 months prescription (3 DPV rings).", "Distribute an HIVST for self-test at 1 month.", "Schedule next visit date after 3 months.")],
    [C("CAB-LA"), L("Initiation injection 1 is given.", "Schedule next visit date for initiation injection 2 after one month (±7 days).")],
    [C("LEN"), L("Initiation injections 1 and 2 are given.", "2 oral loading tablets on day 1.", "2 oral loading tablets are given to take at home on day 2.")]],
   table_note="The one-month visit for clients starting oral PrEP, the PrEP ring and LEN is optional; they are given an HIVST to use at home after one month (if positive, return for confirmatory testing). CAB-LA clients must come back after one month for HIV testing and initiation injection 2."),
 T("tbl-community-initiation-referral", 41, IV + " > Component 4: PrEP Prescription > Community-based PrEP Initiation and Referrals for Refills", "Table 12. Community-based PrEP: initiation with referral for refills, community initiation and refill, community peer distribution of the PrEP ring; registers, referral tool, reporting", ["0100"],
   [[C("Community-based PrEP")]],
   [[C("Community initiation with referrals for refill")],
    [L("Clients should be willing to be linked to a PrEP-offering facility of their choice.",
       "Enter each initiated client in the PrEP register and document them as an initiated and transferred-out client, with the referral serial number and referred facility noted in the notes section.",
       "Complete the national referral tool with: PrEP initiation date; results of baseline laboratory tests (if applicable); contact information of a health care worker who can support any follow-up questions.",
       "Provide the client with the national referral tool and an appointment card for the next scheduled visit.",
       "When the client comes for a follow-up visit after three months in the receiving facility, record as a 'transfer in'; put the referral serial number and referring organisation/clinic in the notes section.",
       "Follow up with the clinic three days after the scheduled follow-up visit to see if the client came to the appointment.",
       "If the client attended the scheduled appointment, the client has successfully been linked to the clinic.",
       "If the client has not attended, the client needs continued follow-up and documentation of status in the Community Outreach Provider PrEP register (STOP, LTFU, etc.).",
       "Utilise a provider-specific PrEP register.",
       "Report monthly on PrEP use through existing regional reporting structures.",
       "For ordering, storage, and reconciliation of PrEP commodities, follow routine Central Medical Store (CMS) ordering and standard operating procedures.")],
    [C("Community initiation and refill")],
    [L("Provide PrEP services monthly at the same outreach location to ensure clients can receive their refills.",
       "Align PrEP refills with other services, e.g. contraceptive refills, refills for non-communicable diseases (NCD), etc.",
       "For oral PrEP and the vaginal ring, up to three months' worth of refills can be given at initiation.",
       "Record the initiated client in the PrEP register / Client Management Information System (CMIS).",
       "Provide each client with an appointment card and indicate the next scheduled visit; the card should include all relevant information (PrEP method, refill date, etc.) for a client who may need to access a health care worker between visits.",
       "Utilise a PrEP register specific to that provider.",
       "Report monthly on PrEP use through existing regional reporting structures.",
       "For ordering, storage, and reconciliation of PrEP commodities, follow routine CMS ordering and standard operating procedures.")],
    [C("Community peer distribution of the PrEP ring")],
    [L("For the PrEP ring, dispensing can be done by trained community cadres already conducting HIVST in the community when: a woman testing HIV negative can be given the ring for some protection until she comes to the facility to start oral or injectable PrEP;",
       "a woman is not willing/able to come to a PrEP facility to start another PrEP method;",
       "a woman prefers the ring over another method, or is already using the ring and due for a refill.")]], rhc=0, pages=[41, 42]),
]
