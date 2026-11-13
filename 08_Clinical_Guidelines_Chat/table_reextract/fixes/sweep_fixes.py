"""Hand-checked repairs from the chunk-by-chunk visual sweep (each verified against the page image).
Writes into the specs: text_drop / text_merge / text_replace / text_add.  Idempotent: run from table_reextract/."""
import atexit, json, os, sys
SPEC = {'anc': 'anc', 'hiv-2022': 'hiv-2022', 'hiv-amendment-2024': 'hiv-amendment-2024', 'ncdimh': 'ncdimh',
        'prep-2025': 'prep-2025', 'sti-vh-draft-2026': 'sti-vh-draft-2026', 'unaids-linkages-sop': 'unaids-linkages-sop',
        'tb-2025': 'tb-2025', 'fp-2021': 'fp-2021', 'mental-health-deskguide': 'mental-health-deskguide'}
_cache = {}
def spec(doc):
    if doc not in _cache:      # text_add / text_replace / text_strip belong to this script alone: rebuilt on every run
        _cache[doc] = json.load(open(SPEC[doc] + '_tables.json'))
        _cache[doc].update(text_add=[], text_replace={}, text_strip={}, text_insert={})
    return _cache[doc]
def drop(doc, *cids):
    s = spec(doc).setdefault('text_drop', [])
    for c in cids:
        c = c if c.startswith(doc) else f'{doc}-{c}'
        if c not in s: s.append(c)
def merge(doc, src, dst):
    spec(doc).setdefault('text_merge', {})[f'{doc}-{src}'] = f'{doc}-{dst}'
def replace(doc, cid, text, page_end=None, heading_path=None):
    v = dict(text=text.strip(), page_end=page_end, heading_path=heading_path) if (page_end or heading_path) else text.strip()
    spec(doc).setdefault('text_replace', {})[f'{doc}-{cid}'] = v
def add(doc, after, page, heading_path, text, page_end=None):
    after = after if after.startswith(doc + '-') else f'{doc}-{after}'
    L = spec(doc).setdefault('text_add', [])
    e = dict(after=after, page=page, heading_path=heading_path, text=text.strip())
    if page_end: e['page_end'] = page_end
    L.append(e)
def add_long(doc, after, page, heading_path, text, max_words=280, page_end=None):
    """add() split at paragraph boundaries into parts of <= max_words (embedding limit); each part keeps the heading"""
    paras = [x for x in text.strip().split('\n\n') if x.strip()]
    head = paras.pop(0) if paras and paras[0].startswith('#') else ''
    parts, cur = [], []
    for x in paras:
        if cur and len(' '.join(cur + [x]).split()) > max_words: parts.append(cur); cur = []
        cur.append(x)
    if cur: parts.append(cur)
    prev = after
    for i, ps in enumerate(parts):
        add(doc, prev, page, heading_path, (head + '\n\n' if head else '') + '\n\n'.join(ps), page_end)
        prev = f'{doc}-add-p{page}-{len(spec(doc)["text_add"]) - 1}'
def strip(doc, cid, *subs):
    d = spec(doc).setdefault('text_strip', {}); k = f'{doc}-{cid}'
    d[k] = sorted(set(d.get(k, [])) | set(subs))
def insert(doc, cid, anchor, text):
    spec(doc).setdefault('text_insert', {}).setdefault(f'{doc}-{cid}', []).append([anchor, text.strip()])
def save():
    for doc, d in _cache.items():
        json.dump(d, open(SPEC[doc] + '_tables.json', 'w'), ensure_ascii=False, indent=1)

atexit.register(save)

# ---------------- ANC ----------------
drop('anc', '0090', '0091-rest')          # definition repeated verbatim in tbl-eclampsia / tbl-prom intro lines
replace('anc', '0061', "### 3.7.4 Birth preparedness\n\nEducate pregnant women about birth preparedness and jointly with the pregnant woman develop a birth preparedness plan including the following:\n- Advise the woman to identify transport, and allocate money that will be required for travel and other expenses.\n- Explain when she needs to go to the facility (Signs of true labour or if she has any complications).\n- Advise on what to bring to the facility for herself and the baby such as: her maternal ANC record /card, clean cloths, towel for drying and wrapping the baby, nappies/diapers, baby blankets, Clean clothes for both the mother and the baby; toiletries including sanitary pads, toothbrush and paste, food and other supplies), carry a travel bag; Birth registration items (National ID card; copy of marriage certificate if married and the copy of father's ID), ultrasound scans, and any medication that she is taking.\n- Review and update the Birth and Emergency Plan at each ANC contact", page_end=29)   # sentence split at p28/p29 page break
drop('anc', '0062')
add_long('anc', '0007', 1, 'Foreword', "## Foreword\n\nThe Global Strategy for Women's, Children's and Adolescent Health 2016 – 2030 prioritizes provision of quality health services to women, newborns, children and adolescents and acknowledges that investing more in their health contributes to the realization of their right to health. The Kingdom of Eswatini aligns itself with this global health and human rights commitment. The Kingdom's efforts in attaining the targets of the Sustainable Development Goals is operationalized through the Eswatini National Sustainable Development Strategy and the Health Sector Strategic plan. The Government of Eswatini has made significant progress in the provision of maternal, newborn and adolescent health. This is evident in the high ANC coverage (at least once at 98%), and institutional deliveries (87.7 %), skilled birth attendance (88%) MICS 2014 and postnatal Care coverage of 71% (SRH Annual report). However, there is a clinical gap in the provision of quality of care evidenced by an unacceptably high Maternal Mortality Ratio (MMR) at 593/100,000 live births (Intercensus Demographic Housing Survey, 2012) and Neonatal Mortality Ratio (NMR) at 20 per 1000 live births MICS 2014. In an effort to respond to the challenges, the MOH has developed the first national ANC guidelines which will improve provision of quality of health services, and implementation of the guidelines will contribute to the well-being of women and families and will further contribute to positive perinatal and maternal outcomes. The benefits of the guidelines are as follows:\n\n- It is a platform to ensure timely and consistent health promotion, screening, diagnosis, disease prevention and management of complications in the context of respectful care.\n- It also serves as a standard for quality health services.\n- Through ANC activity (prevention, screening, diagnosis, management), this guideline will contribute to reducing MMR and incidence of still birth in the country.\n\nThese guidelines are in line with the new WHO ANC recommendations 2016 and are designed for use by all health care providers in the sector (Government, Private, NGOs) both at health facility and community levels. In this regard, all health workers providing ANC services are expected to adhere to these new guidelines. All partners and training institutions involved in-service and pre-service teaching should adjust their training to reflect this new guidance. The Ministry of Health is committed to ensure that the requisite resources are made available for the effective implementation of the guidelines.")   # foreword page had no chunk

# ---------------- Linkages ----------------
replace('unaids-linkages-sop', '0020', """## **5.2 Treatment Navigation Services**

*The purpose of escort and treatment navigation is to facilitate same-day enrollment in care and ART initiation and improve ART retention by making clients more knowledgeable and comfortable about locations of ART services. Escorting clients is not about policing the client, but it should assist him/her to reach the next service point without experiencing challenges. Escorting is done during the first visit as per the need.*

Treatment navigation should follow the steps below (shown as a graphic on the page):
1. Inform clients about the physical layout and all stations of care.
2. Introduce clients to key staff, including facility-based ECs if the client is a referral from the community.
3. Help clients understand what services to expect during their ART visits.
4. Answer questions about ART care and prevent or mitigate negative experiences.
5. Stay with and support the client throughout their entire first ART visit (depending on the client).
6. Inform clients about what to do and services to expect at their next visit.""")   # p20 graphic steps were missing
replace('unaids-linkages-sop', '0030', """### **9.1 Initiating ART on client testing positive HIV diagnosis (Annex 2)**

HIV testing is done by clinicians, the client testing HIV positive shall be provided with the following by the clinician (steps shown as a graphic on the page):
1. ART readiness assessment
2. Initiate client on ART
3. Enroll client into LCM
4. Provide psychosocial support counselling
5. Discussing importance of disclosure including index testing
6. Elicit index contacts and discuss partner notification strategies
7. Distribute HIV self-test kits where necessary""")
drop('unaids-linkages-sop', '0031')        # garbled arrow version of the same graphic
replace('unaids-linkages-sop', '0043', """Figure: Facility-based Linkage Case Management (LCM) model (timeline from HIV diagnosis to discharge at day 180)

- Entry: facility-based HTS, OPD and referrals from other HTS points -> the LCM client is paired with an LCM facilitator.
- ART initiation (Day 0): focused on the importance of early ART initiation, accessing and resolving enrolment barriers; counselling on disclosure and testing partners, family members and associates (PFAs).
- Escort to VCT/ART the same or a subsequent day if needed.
- Treatment navigation: facilitate VCT/ART initiation; provide psychological support during the entire clinic visit; informational counselling on the content, sequence and location of HIV clinical services.
- Follow-up phone calls: Day 3-5 and Day 10-12.
- 1st clinical visit (day 14): preview disclosure progress; assess barriers to ART initiation; follow up on progress on testing of contacts (index); address concerns raised by clients.
- Follow-up phone call: Day 21-30.
- 2nd clinical visit (day 30-45): focused on disclosure and ART adherence counselling, HTS for PFAs, and assessing and resolving barriers to care; assess barriers to ART adherence; address concerns raised by the client.
- Follow-up phone call: Day 44-60.
- 3rd clinical visit (day 45-60): provide HTS for PFAs and additional information and motivational counselling; explore barriers to treatment; graduate the client and confirm availability to assist if they have challenges in future.
- Follow-up phone calls: Day 120-125 and Day 170-175.
- 4th clinical visit (day 180): provide ART service; discuss available ART DSD options; discharge client.""")
replace('unaids-linkages-sop', '0100', """Figure: Community Linkage Case Management (LCM) model

- HTS event (home/venue-based): positive clients are identified and introduced to the LCM officer.
- The HIV+ client is paired with an LCM facilitator. ART initiation (Day 0): focused on the importance of early ART initiation, accessing and resolving enrolment barriers; counselling on disclosure and testing partners, family members and associates (PFAs).
- LCM nurse: conduct index contact solicitation; offer community ART; refer to facility for enrolment.
- Clients initiated on ART: the LCM officer escorts the client to an outside mobile unit to receive clinical services from the nurse; same-day transport/escort when and where possible.
- Follow-up phone call: Day 3-5.
- Enrolment at the ART/VCT unit as soon as the client is ready: escort or meet at the facility; introduce the client to the facility LCM officer; provide treatment.
- Follow-up phone call: Day 10-12.
- 1st session (LCM facilitator): focused on encouraging early enrolment in HIV care; discuss the benefits of early ART initiation.
- 2nd clinical visit (day 30-45): focused on disclosure and ART adherence counselling, HTS for PFAs, and assessing and resolving barriers to care; assess barriers to ART adherence; address concerns raised by the client.""")
replace('unaids-linkages-sop', '0172', """Flowchart: Linkages for client testing HIV positive in the community (Annexure 4)

1. Tested HIV positive -> verify previous HIV positive/ART registration in any system (CMIS, APMR).
   - Found in the system: see Annexure 2, Linkages for Clients Returning to Care.
   - Not found in the system: retest for verification as per the HTS algorithm.
2. Retest result:
   - Test -ve: re-appoint to HIV testing according to HTS guidance.
   - Test +ve: readiness assessment.
3. Readiness assessment:
   - Ready, option A: same-day community ART initiation -> enroll into LCM -> offer prevention package (i.e., TPT, CaCx) -> refer and link to facility for ART refill -> follow-up as per LCM guidance to be done by the facility.
   - Ready, option B: refer and link to facility for ART initiation within 7 days -> enroll into LCM -> offer prevention package (i.e., TPT, CaCx) -> call the facility to ensure linkage -> follow-up as per LCM guidance to be done by the facility.
   - Not ready: enroll into LCM; escalation counselling (doctor, nurse, social worker, HTS provider, expert client, psychologist) -> follow clients as per LCM guidance until initiation.""")
replace('unaids-linkages-sop', '0093', """## 12.23 Responsibility Of Referring Facility

The health facility referring client must understand the needs of the client and ascertain if services are available at the facility where the client is being referred to. Set an appointment for the client so that the receiving facility is made aware when they should expect the client. Comprehensively document services provided for the client in the National Referral form. Explain to the client the importance of linkage.""")   # the bullet list was a column-jumbled copy of tbl-p58-0094
replace('unaids-linkages-sop', '0126', """(Process to identify clients that have disengaged from care, continued)

c) Document demographic information (name, surname, CMIS number, date reported LTFU etc.) of clients that missed scheduled visits from the appointment register

d) Verify LTFU using patient charts, CMIS /APMR, pharmacy records

e) Contact confirmed LTFU using phone contacts

f) If unable to contact the client on 3 different phone attempts on different days (or times) refer clients to community ECs

g) If unable to track the client through home visits or Community partners for follow up home visits""")   # list was repeated twice by the parser
drop('unaids-linkages-sop', '0142', '0143-rest')   # p91: intro + stray lines, all inside tbl-p91-0143 (intro paragraph included)
drop('mental-health-deskguide', '0035', '0063')   # caption-only / table body copy; both inside tbl-p24-0036 / tbl-p34-0064
drop('mental-health-deskguide', '0229')   # caption only; tbl-p91-0230 carries it
replace('mental-health-deskguide', '0239', "## **NON PHARMACOLOGICAL MANAGEMENT**\n\n**a. COUNSELLING**\n\n- Establish rapport with the client/ patient\n- Provide non-judgmental and solution focused counselling.\n- Help the patient to explore their psychosocial problems and decide on appropriate goals to dealing with them by making their own decisions.\n- Explore the patient's thoughts and understanding about their presenting stressor(s).\n- Emphasize on maintaining a regular sleep cycle ( to patients with insomnia) such as;\n  - o going to bed at the same time every night,\n  - o avoiding sleeping too much especially during day time,\n  - o avoiding taking substances that interfere with sleep i.e. caffeinated beverages\n  - o Turning off the lights, TV and phone when sleeping\n  - o Using bed for sleeping only to signal the brain that it is time to sleep\n- Structured physical activity program\n  - o Explore with the patient kind of physical activity the client prefers\n  - o Encourage them to exercise at least three times a week\n- Reactivate healthy social network\n  - o Encourage patients to socialize and not to let worries isolate them from loved ones or enjoyable activities. Social interaction and caring relationships can lessen worries.\n  - o Identify the person's prior social activities that, if re-initiated, would have the potential for providing psychosocial support; for example family gatherings, outings with friends, sports, movies etc.\n  - o Actively encourage resuming prior social activities\n- Inform patient and family supporter:\n  - o About the diagnosis.\n  - o How to recognize thoughts of self-harm or suicide and consult immediately", page_end=98)   # lead-in 'Inform patient and family supporter:' + its 2 sub-items (split at chunk boundary)
replace('mental-health-deskguide', '0240', "## **NON PHARMACOLOGICAL MANAGEMENT** (continued)\n\n- Normalize their worries. For example, worries about loss of energy, loss of appetite and/ or insomnia. Assure them it is part of the condition.\n- Let it go; encourage the patient not to dwell on past concerns. Change what he/she can and let the rest take its course.\n- Conduct Suicide Risk Assessment as indicated.\n- Explore adherence to medications and provide adherence counselling as indicated\n- Explore and manage stigma and discrimination issues as well as Highly Expressed Emotions.\n\n**b. PSYCHO-EDUCATION**\nProvide information about depression that;\n- Depression is very common and can happen to anyone at any time.\n- Depression can be successfully treated if adherence is ensured\n- For the majority of people suffering from MDD it takes 4-6 weeks to start feeling better.\n- Antidepressants are not addictive but they have side effects like any other medicines.\n\n**c. SPECIAL CASES; CHILDREN AND ADOLESCENTS**\nExplore about;\n- mental & substance use problems in parents/caregivers and the adolescents themselves\n- school performance problems\n- parents' psychosocial stressors\n- maltreatment, abuse or bullying at school by teachers or other students\n- issues of adoption, foster care, orphanage etc. which may influence the current presentation\n- They need Doctor/Clinical Psychologist led services, ensure proper referral and linkages.\n- The need for family therapy or academic interventions")
drop('anc', '0026-rest')     # right text, wrong page (14): re-added with its real page, p23
add('anc', 'tbl-anc-essential-package', 23, '3.0 Providing ANC Services', """## 3.0 Providing ANC Services

ANC services can start as soon as the woman misses a period and suspects that she is pregnant. The ANC services that are provided must be in line with the ANC service package outlined in this guideline.""")
drop('hiv-amendment-2024', '0054-rest')   # p28-29: sentence + question both inside fig-7.1 / fig-7.2 items
drop('hiv-amendment-2024', '0066-rest')   # p33: last bullet of fig-8.2, already in the figure item
replace('hiv-amendment-2024', '0013', """## CHAPTER 3: HIV TESTING SERVICES

### INTRODUCTION

Even though Eswatini has made tremendous progress towards HIV Epidemic Control, findings from SHIMS3 (2021) indicate that critical case-finding gaps remain at the sub-population level among children 15 years and below, women 15-29 years, men 25-34 years, the military and key populations (MSM & FSW). These HTS gaps need to be addressed to ensure Eswatini fully achieves and maintains the first 95 UNAIDS HIV epidemic control target.

### **PURPOSE**

This addendum seeks to provide guidance to address current HTS gaps through strategic shifts in HTS implementation, and adoption of a status-neutral approach as the key gateway for entry into care.""")   # p8 chapter introduction was missing
strip('hiv-amendment-2024', '0061', ' icon: X mark in a circle')
strip('hiv-amendment-2024', '0104', 'image: abstract background with red, blue, and yellow graphic elements')
drop('prep-2025', '0026')   # p14-15: table footnotes (in tbl-oral-prep-start-stop) + figure placeholders (fig-ed-prep-examples has the figures)
strip('prep-2025', '0054', "image: A line chart showing CAB PrEP blood levels over 12 months, with annotations for dosing schedule and the 'tail period'.")
strip('prep-2025', '0054', "## **Figure 7. CAB-LA “tail period”**")
add('prep-2025', '0054', 25, "2 Overview of PrEP Products > 2.3 CAB-LA Injectable PrEP > Stopping CAB-LA > Tail Period (Figure 7)", """### Figure 7. CAB-LA "tail period" (line chart, read from the page)

The chart plots the CAB PrEP blood level over 12 months against a horizontal line marking the blood level needed to prevent HIV. Dose #1 is given at month 1, dose #2 at month 2 and dose #3 at month 4; each injection raises the level well above the line. At month 6 the client is due for dose #4 but decides to stop CAB PrEP. From then on the level falls slowly below the line through month 12: this is the "tail period" – after injections are stopped, CAB PrEP is still present in the body, but not enough to prevent HIV. When the level drops below the line it is possible to acquire a kind of HIV that could be resistant to the best HIV treatment regimen. (Adapted from Columbia University Irving Medical Center and the Blueprint Project.)""")
strip('prep-2025', '0069', "## **Figure 8. LEN dosing schedule**", "image: LEN dosing schedule diagram")   # figure is item fig-len-initiation-schedule
drop('prep-2025', '0077')    # p33: text + placeholder, both inside fig-len-rifampicin
drop('sti-vh-draft-2026', '0086-rest-a')   # running header + an NB line that txt-p41 already carries (p41)

# ---------------- STI ----------------
replace('sti-vh-draft-2026', 'txt-p34-t0129', """## Common etiological STIs (POC testing):

### Bacterial STIs:

- Gonorrhoea
- Chlamydia
- Syphillis
- Chanchoid
- Bacterial vaginosis
- Mycoplasma genitalium
- Pelvic inflammatory desease (PID)""")    # group heading was lost
replace('sti-vh-draft-2026', 'txt-p36-t0140', """## 5.1.1 See chart 2 for syndromic treatment for genital ulcer syndrome.

The following table shows the causative organisms with their signs and symptoms, treatment and options.""")   # sentence was cut
replace('sti-vh-draft-2026', 'txt-p78-t0208', """## 7.1.2 Syphilis in pregnancy

The clinical symptoms of syphilis are not altered by pregnancy. Since asymptomatic adult syphilis infection is common, all pregnant women should be screened for syphilis. This can reduce the complications of congenital syphilis. A rapid plasma reagent (RPR) test should be routinely done on pregnant mothers at first contact with the health care provider and treatment should be instituted if the RPR result is reactive and the partner should be treated as well. If RPR test is negative repeat after 3 months.""", page_end=79)
drop('sti-vh-draft-2026', 'txt-p78-t0209')   # second half of the sentence above (page break)

# ---------------- HIV 2022 ----------------
drop('hiv-2022', '0122-rest')                 # two lead-ins of the p57 IPV tool, which box-3.3-ipv-screening-tool carries in full
drop('hiv-2022', '0360-rest-a', '0360-rest')  # p138 one-line lead-ins to boxes that follow with their own titles
drop('hiv-2022', '0503-rest')                 # p186 colour key of a timeline graphic whose content is in txt-p186-t0363 / Table 8.8
drop('hiv-2022', '0770-rest')                 # p284 marker list, inside fig-11.11-hbv-jaundice-diagnosis
drop('tb-2025', '0599-rest')                  # p231 growth-chart axis labels

# ---------------- FP ----------------
replace('fp-2021', '0033', '## **4.3 FP COMMODITY LOGISTICS AND MANAGEMENT**\n\nHigh-quality reproductive health care requires a continuous supply and management of contraceptives and other commodities. Of note, Family planning providers are the most important link in the contraceptive supply chain management system that moves commodities from the manufacturer to the client.\n\n* Accurate and timely reports and orders from providers help supply chain managers determine what products are needed, how much to buy, and where to distribute them.\n* Clinic staff members do their part when they:\n    - Properly manage contraceptive inventory\n    - Accurately record and report what is provided to clients, and\n    - Promptly order new supplies.\n\nClinic staff members need to be familiar with, and work within the system that in place to make sure that they have the supplies they need.\n\nLogistics Management Information System (LMIS) of FP commodities must include:\n* Accurate projection of supply needs and cost\n* Ordering and procurement\n* Appropriate storage facilities at all levels\n* Efficient distribution system\n* Maintaining good records of supply and utilization\n* Monitoring the quality of supplies\n* Robust LMIS\n\n**The purpose of logistics management information system** (diagram): LMIS ensures commodities are available in the right product, in the right quantity, in the right condition, in the right place, at the right time and for the right cost.', page_end=27)   # p27 LMIS diagram (six 'rights') read from the page
replace('fp-2021', '0034', '## **5.1 OVERVIEW OF NFPM**\n\nNatural family planning methods (NFPM) refers to the methods that do not include the use of chemical / hormonal substances or devices for the purpose of preventing pregnancy or achieving pregnancy.\n\n#### **Types of NFPM**\n\n1.  Abstinence\n2.  Fertility Awareness Methods (FAM)\n3.  Lactational Amenorrhea (LAM)\n4.  Coitus Interruptus (CI)', heading_path='5 Natural Family Planning Method > 5.1 Overview of NFPM')   # LMIS heading + image placeholder moved out; chunk now starts at 5.1
strip('fp-2021', '0166', 'image: header banner showing illustrations of Condom, Female condom, Oral contraception, and Vaginal ring')   # page-header artwork
replace('fp-2021', '0197', """## **14.2 APPENDIX 2: WHO MEDICAL ELIGIBILITY CRITERIA WHEEL FOR CONTRACEPTIVE USE (2015)**

The guideline reproduces the WHO Medical Eligibility Criteria Wheel for Contraceptive Use (2015) as a full-page image (pp. 94-95). The wheel gives the MEC category (1-4) for each method (combined hormonal contraceptives, progestogen-only pills, progestin-only injectables, implants, levonorgestrel IUD, copper IUD) by condition (e.g. postpartum and breastfeeding, nulliparity, adolescents, vaginal bleeding, uterine fibroids, cervical and breast cancer, liver disease, venous thromboembolism, cardiovascular disease, hypertension, obesity, diabetes, smoking, headache, medications, HIV, STIs, PID, sepsis). The same recommendations are given in text in Appendix 1 (14.1, Summary of Recommendation - Medical Eligibility Criteria).""")   # p105 placeholder text only
replace('fp-2021', '0063', '## Exclusive Breastfeeding\n\n#### *Less than 6 months after giving birth*\n\n* If her menses have not returned, she can start POPs any time between giving birth and 6 months.\n* No need for a backup method\n* If her menses have returned, she can start POPs as advised for women having menstrual cycles\n\n## Mixed feeding\n\n#### *If her menses have not returned*\n\n* She can start POPs any time if reasonably certain she is not pregnant.\n* She will need a backup method for the first 2 days of taking pills.\n* She can start POPs as advised for women having menstrual cycles (see next page)\n\n## Not breastfeeding\n\n#### *Less than 6 weeks after giving birth*\n\n* She can start POPs at any time.\n* No need for a backup method.\n\n#### *More than 6 weeks after giving birth*\n\n* If her menses have not returned, she can start POPs any time if reasonably certain she is not pregnant.\n* Offer a backup method for the first days of taking pills.\n* If her menses have returned, she can start POPs as advised for women having menstrual cycles.\n\n## <u>Switching from a hormonal method</u>\n\n* Immediately, if she has been using the hormonal method (POPs) consistently and correctly or if otherwise reasonably certain she is not pregnant.\n* No need to wait for her next monthly period.\n* No need for a backup method.')   # p42: 'Not breastfeeding' heading was lost, so its <6-week rule read as Mixed feeding
replace('fp-2021', '0090', '## Exclusive Breastfeeding (COCs)\n\n#### *Less than 6 months after giving birth*\n\n* Give her COCs and tell her to start taking them 6 months after giving birth or when breast milk is no longer the baby’s main food (whichever comes first).\n\n#### *More than 6 months post birth*\n\n* If her menses have not returned, she can start COCs any time it is reasonably certain she is not pregnant.\n\n* She will need a backup method for the first 7 days of taking pills.\n* If her menses have returned, she can start COCs as advised for women having menstrual cycles.')   # p53 group label only in metadata
replace('fp-2021', '0091', '## Mixed feeding (COCs)\n\n### *Less than 6 weeks post birth*\n\n* Give her COCs and tell her to start taking them 6 weeks after giving birth.\n* Give her a backup method to use until 6 weeks since giving birth if her monthly bleeding returns before this time.\n\n### *More than 6 weeks after giving birth*\n\n* If her menses have not returned, she can start COCs any time it is reasonably certain she is not pregnant\n* If her menses have returned, she can start COCs as advised for women having menstrual cycles')
replace('fp-2021', '0092', '## *No monthly period (not related to childbirth or breastfeeding)*\n\n* She can start COCs any time it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days of taking pills.\n\n## *After miscarriage or abortion*\n\n* Immediately. If she is starting within 7 days after first or second trimester miscarriage or abortion, no need for a backup method.\n* If it is more than 7 days after first or second trimester miscarriage or abortion, she can start COCs any time it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days of taking pills.\n\n## *Not breastfeeding*\n\n* She can start COCs at any time on days 21–28 after giving birth.\n* Give her pills any time to start during these 7 days.\n* No need for a backup method.', heading_path='6 Hormonal Contraceptives > 6.4 COMBINED ORAL CONTRACEPTIVES (COCs) > When to start')   # was labelled 'Mixed feeding'
replace('fp-2021', '0078', '## **When to start POIs?**\n\n### <u>Regular Menses</u>\n\n* Give the initial injection within the first 7 days of the menstrual bleeding or at any time, if it is reasonably certain that she is not pregnant\n* If after 7 days of menstrual bleeding she will need a backup method for the next 7 days.\n\n### <u>Amenorrheic</u>\n\n* Give anytime if it is reasonably certain that she is not pregnant.\n* Use a backup method for the first 7 days of initiating the method')
replace('fp-2021', '0079', '## **When to start POIs?** (continued)\n\n### <u>Postpartum client</u>\n\n#### *Breastfeeding:*\n\n* Any time within 6 weeks postpartum. With lactational amenorrhea give between 6 weeks and 6 months postpartum, if you can establish that she is not pregnant.\n\n#### *Non breastfeeding:*\n\n* Start immediately or at any time within the first 21 days postpartum. After 21 days postpartum and no menses, rule out pregnancy first and initiate but emphasize on the need of a backup method for the next 7 days.\n\n### <u>Post abortion</u>\n\n* Start immediately within 7 days after first or second trimester abortion, no need for a backup method.\n* If more than 7 days, she can start anytime it is reasonable certain she is not pregnant.\n* She will need a backup method for the first 7 days after the injection.\n\n## **Side effects of POIs**\n\n### **DMPA**\n\n* Irregular bleeding and prolonged periods: in the first 3 months.\n* No monthly period, infrequent bleeding and irregular bleeding: at 1 year.\n\n### **NET-EN**\n\n* Weight gain\n* Headaches\n* Dizziness\n* Abdominal bloating and discomfort\n* Mood changes\n* Low libido\n* Loss of bone density')   # p47-48: 'Side effects' heading lost; DMPA timing brackets (first 3 months / at 1 year) restored from the page
replace('fp-2021', '0105', '## <u>Exclusive breastfeeding</u> (CICs)\n\n#### *Less than 6 months after giving birth*\n\n* Delay first injection until 6 months after giving birth or when breast milk is no longer the baby’s main food, whichever comes first.\n\n#### *More than 6 months after giving birth*\n\n* If monthly bleeding has not returned, start injectables any time if it is reasonably certain woman is not pregnant.\n* She will need a backup method for the first 7 days after the injection.\n\n* If her menses have returned, she can start injectables as advised for women having menstrual cycles')   # p59 group label only in metadata
replace('fp-2021', '0108', '## <u>After taking emergency contraceptive pills (ECPs)</u> (CICs)\n\n### *After taking progestin-only or combined ECPs:*\n\n* Start or restart injectables on the same day as taking the ECPs.\n* No need to wait for her next monthly menstrual bleeding to have the injection.\n* Give a backup method for the first 7 days after the injection\n* If she does not start immediately, but returns for injectables, she can start at any time if it is reasonably certain she is not pregnant.')
replace('fp-2021', '0116', '## **Side effects** (implants)\n\n* Changes in bleeding patterns, including:\n    - Lighter bleeding and fewer days of bleeding\n    - Prolonged bleeding, irregular bleeding, infrequent bleeding, amenorrhea (first several months to a year)\n    - Lighter bleeding and fewer days of bleeding\n    - Irregular bleeding, infrequent bleeding and absent monthly bleeding may persist after a year of insertion\n* Headaches\n* Abdominal pain\n* Acne (can improve or worsen)\n* Weight change\n* Breast tenderness\n* Dizziness\n* Mood changes\n* Nausea\n* Enlarged ovarian follicles')   # p63-64: bracket 'First several months to a year' restored; list order as printed
replace('fp-2021', '0118', '## **When to start**\n\nA woman can start using implants any time she wants if it is reasonably certain she is not pregnant.\n\n### <u>Having menstrual cycles or switching from a non-hormonal method</u>\n\n*Any time of the month*\n\n* If she is starting within 7 days after the start of her monthly bleeding, no need for a backup method.\n* If it is more than 7 days after the start of her monthly bleeding, she can have implants inserted any time if it is reasonably certain she is not pregnant.\n    - She will need a backup method for the first 7 days after insertion.')   # page-break line split
replace('fp-2021', '0120', '## <u>Exclusive breastfeeding</u> (implants)\n\n### *Less than 6 months after giving birth*\n\n* If her menses have not returned, she can have implants inserted any time between giving birth and 6 months.\n* No need for a backup method.\n* If her menses have returned, she can have implants inserted as advised for women having menstrual cycles\n\n### *More than 6 months after giving birth*\n\n* If her menses have not returned, she can have implants inserted any time if it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days after insertion.\n* If her menses have returned, she can have implants inserted as advised for women having menstrual cycles.')
replace('fp-2021', '0121', '## <u>Mixed feeding</u>\n\n* If her menses have not returned she can have implants inserted any time if it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days after insertion.\n* If her menses have returned, she can have implants inserted as advised for women having menstrual cycles.')
replace('fp-2021', '0122', '## <u>Not breastfeeding</u> (implants)\n\n### *Less than 6 weeks after giving birth*\n\n* She can have implants inserted at any time.\n* No need for a backup method\n\n### *More than 6 weeks after giving birth*\n\n* If her menses have not returned, she can have implants inserted any time if it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days after insertion.\n* If her menses have returned, she can have implants inserted as advised for women having menstrual cycles\n\n## <u>Amenorrhea (not related to childbirth or breastfeeding)</u>\n\n* She can have implants inserted any time if it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days after insertion.')
replace('fp-2021', '0125', '## <u>After taking emergency contraceptive pills (ECPs)</u> (implants)\n\n### *After taking progestin-only or combined ECPs:*\n\n* Implants can be inserted on the same day as she takes the ECPs.\n    - She will need to use a backup method for the first 7 days.\n* If she does not start immediately, but returns for an implant, she can start at any time if it is reasonably certain she is not pregnant.')
replace('fp-2021', '0135', '## <u>Exclusive breastfeeding</u> (IUCD)\n\n### *Less than 6 months after giving birth*\n\n* If the IUCD is not inserted within the first 48 hours and her menses have not returned, she can have the IUCD inserted any time between 4 weeks and 6 months after giving birth.\n* If her menses have returned, she can have the IUCD inserted as advised for women having menstrual cycles.\n* No need for a backup method.\n\n### *More than 6 months after giving birth*\n\n* If her menses have not returned, she can have the IUCD inserted any time it is reasonably certain she is not pregnant.\n* If her menses have returned, she can have the IUCD inserted as advised for women having menstrual cycles\n* No need for a backup method.\n\n## <u>Mixed feeding or not breastfeeding</u> (IUCD)\n\n### *More than 4 weeks after giving birth*\n\n* If her menses have not returned, she can have the IUCD inserted if it can be determined that she is not pregnant\n* No need for a backup method.\n* If her menses have returned, she can have the IUCD inserted as advised for women having menstrual cycles.\n\n## <u>Amenorrhea (not related to childbirth or breastfeeding)</u>\n\n* Any time if it can be determined that she is not pregnant\n* No need for a backup method.', heading_path='7 Intrauterine Contraception Device > When to start IUCDs')   # p71: 'Exclusive breastfeeding' and 'Mixed feeding or not breastfeeding' labels lost
replace('fp-2021', '0067', '## <u>Having menstrual bleeding</u> (POPs)\n\n### *Any time of the month*\n\n* If she is starting within 5 days after the start of her monthly bleeding, no need for a backup method.\n* If it is more than 5 days after the start of her monthly bleeding, she can start POPs any time it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days of taking pills\n\n## <u>Amenorrhoeac (not related to childbirth or breastfeeding)</u>\n\n* She can start POPs any time it is reasonably certain she is not pregnant.\n* She will need a backup method for the first 7 days of taking pills.')
replace('fp-2021', '0070', '## <u>After taking emergency contraceptive pills (ECPs)</u> (POPs)\n\n### *After taking progestin-only or combined ECPs:*\n\n* She can start or restart POPs immediately after she takes the ECPs.\n* No need to wait for her next monthly bleeding.\n* A continuing user who needed ECPs due to pill-taking errors can continue where she left off with her current pack.\n* If she does not start immediately, but returns for POPs, she can start at any time if it is reasonably certain she is not pregnant.\n* All women will need to use a backup method for the first 7 days of taking pills.\n\n### *After taking postinor ECPs:*\n\n* She can start or restart POPs immediately after taking -ECPs.\n* No need to wait for her next monthly bleeding.')

# ---------------- TB ----------------
insert('tb-2025', '0012', '**Index Patient (index case) of TB:** refers to the initially identified person with TB disease in a specific household or other comparable setting in which others may have been exposed. An index patient is a person on whom a contact investigation is centred but who is not necessarily the source of an outbreak of TB.', 'Patient-Initiated Care: refers to a patient-initiated pathway to TB diagnosis that involves: (1) a person with TB disease experiencing symptoms that they recognize as serious; (2) the person having access to and seeking care, and presenting spontaneously at an appropriate health facility; (3) a health worker correctly assessing that the person fulfils the criteria for presumptive TB; and (4) the successful use of a diagnostic algorithm with sufficient sensitivity and specificity to diagnose TB.')   # p18 paragraph missing from every chunk
insert('tb-2025', '0014', '**TB Disease:** refers to a person with disease caused by the M. tuberculosis complex. The M. tuberculosis complex comprises nine distinct but closely related organisms. The complex includes M. africanum, M. bovis, M. canetti, M. caprae, M. microti, M. mungi, M. orygis, M. pinnipedii, and M. tuberculosis.', 'TB Case: refers to the occurrence of TB disease in a person. The term should be reserved for use in the context of registration or reporting of the clinical condition and not during the provision of care. This definition also includes the identification of TB disease through post-mortem examination. All TB cases should be notified to public health authorities, regardless of whether TB treatment was started. People with TB who died or were lost to follow-up before TB treatment started should also be notified to public health authorities; this is because they are important from the perspective of both surveillance and public health (they may have contacts that require tracing and follow-up).')   # p19 paragraph missing from every chunk
insert('tb-2025', '0058', '(c) <u>IEC Materials:</u> TB information, education and communication materials remain important in communicating TB messages. Different types of IEC materials (posters, brochures, pamphlets, job aids etc.) should be developed and distributed to various audiences according to their needs.', '(d) Traditional Media: Though communication has evolved over the years, the use of traditional media such as radio, television and newspapers remain important in the communication of TB messages. According to recent surveys, radio remains the most effective channel for communicating health messages.')   # p35 paragraph missing from every chunk
insert('tb-2025', '0078', "- Additional sessions can be planned according to patients' needs e.g. poor adherence, depression, mental health etc.", '## 2.7 Risk Communication\n\nRisk communication refers to the real-time exchange of information, advice and opinions between experts or officials and people who face a threat to their survival, health, economic or social well-being3. The main purpose is that everyone at risk can make informed decisions to mitigate the effects of the health threat.')   # p41 paragraph missing from every chunk
insert('tb-2025', '0092', 'Community Education and Awareness Campaigns to prompt earlier care-seeking for TB symptoms at healthcare facilities.', 'These active case-finding models may be implemented through community outreach activity by community health volunteers in collaboration with other community partners or a team including the provision of integrated mobile clinic services.')   # p47 paragraph missing from every chunk
insert('tb-2025', '0213', 'During the on-site visit, the NTRL supervisor should select five smear-positive and five smear-negative slides randomly and review them as per QA protocol.', 'Ensure that the microscopy laboratories and health facilities collect and transport. TB samples are visited at least once every month. Other health facilities which collect specimens and transport them to an off-site laboratory should assign Specimen Identification Numbers and write them on the side of the containers.')   # p91 paragraph missing from every chunk
insert('tb-2025', '0223', '**Note:** The LMIS reports should be submitted to the regional health offices (Regional Pharmacist and Regional Lab Coordinator) every month for review before submission to CMS.', '## 5.4.3 Expired/ damaged laboratory and drug commodities\n\nAll health facilities should have a demarcated area for storage of products that have expired or have been damaged. It is recommended that this should not be in the same area where there is usable stock. Approval of disposal of pharmaceuticals and laboratory chemicals must be sought from the Government Stores department by completing and submitting TF 108/TF106 forms before destruction occurs (see Health Facility Pharmaceutical & Laboratory Supply Chain SOPs).')   # p94 paragraph missing from every chunk
insert('tb-2025', '0251', '- ✓ ART stopped can be re-introduced or re-initiated after at least 2 weeks on the full TB drug regimen to prevent IRIS.', 'Since some of the drugs recommended in the options above may not be available in all TB BMUs, this guideline recommends that patients with severe hepatopathy be referred for management by a doctor at a health center or hospital where these medications are available. It is encouraged that the management of these cases be discussed by the managing clinician with a team of peers and TB specialists.')   # p104 paragraph missing from every chunk
insert('tb-2025', '0299', 'No regimen modification is allowed except for Lzd dose reduction to 300 mg if a 9-week consecutive treatment is completed. If culture remains positive or reversion occurs from month 4 to the end of the BPaLM regimen and month 6 to the end of the BPaL regimen, assign the treatment outcome "failure".', '(c) Switch to ITR shall be considered earlier in patients with a clear lack of response (clinically, smear grading, culture).')   # p121 paragraph missing from every chunk
replace('tb-2025', '0107', '## 3.3.6 Syndromic referral approach to cough and other signs of TB/CLC\n\nThe entry point for the integration of TB with CLC is chronic cough as a key symptom of underlying problems. For standardisation, cough of any duration needs to be investigated. If tests for TB are negative but the cough persists, further tests for CLC need to be undertaken.\n\nChronic cough may be present due to several factors including:\n- Asthma\n- Bronchiectasis\n- COPD\n- Left Heart Failure\n- Lung Cancer\n- Tuberculosis\n- Other Conditions\n\nCHWs should normally screen and refer those with signs and symptoms to the Primary Health Care (PHC) clinic as the first step. The PHC should determine whether patients need further diagnosis for conditions that cannot be managed at the PHC and, if so, refer them further to the nearest hospital or specialist facility. Referral and feedback tools should be used at each stage of referral (i.e. CHW to PHC, PHC to hospital/specialist facility).\n\nCHWs are closely linked to PHCs with a formal system of referral that feeds into the national monitoring and reporting system. At PHC level CHWs are provided with information about the diagnostic outcome of each presumptive case referred through a feedback loop. In addition, CHWs need to maintain close follow-up of all those receiving treatment to ensure that those whose symptoms persist despite treatment completion are re-referred to the PHC or more specialized facilities or hospitals. Similarly, PHCs must use referral tools to hospitals or specialized TB/CLC facilities and ensure a feedback loop is also provided to them for onward relay to the CHW in whose area the patient resides for follow-up and support.\n\nSome potentially life-threatening conditions should be treated as “red flag symptoms” (e.g. Chest pain). CHWs are capacitated to recognise such signs and utilize a tool (see Table 7 below) to assist them ask the right questions to ensure such “emergency” cases are rushed to the nearest health facility.')   # p52-53: 'Tuberculosis' list item and the CHW referral paragraph were missing
replace('tb-2025', '0063', '## 2.4 Social Mobilization\n\nSocial mobilization entails engaging communities and other stakeholders to participate and take ownership of activities and strategies aimed at ending TB in Eswatini. Such activities may include community dialogues, community outreaches, road shows, meetings, door-to-door outreaches, health fairs, debates, sports, drama performances and many more. Community mobilization helps generate a wider participation and involvement of everyone including community leaders and opinion leaders to be at the forefront of activities that will contribute to ending TB in Eswatini.\n\nTable 5 below briefly describes ACSM interventions, desired behaviours and outcomes that will contribute to ending TB in Eswatini.')   # p37 section text was missing
insert('tb-2025', '0324', 'Adverse drug reaction (ADR) is a major cause of fatality and loss of follow-up. Patients should be carefully monitored to detect and manage ADRs at their onset. DR-TB Clinicians and counsellors should educate the patients on potential adverse reactions, their signs and symptoms, necessity of timely reporting. The ADR should be recorded in the section provided in the treatment supporter book.', 'The community treatment supporters responsible for the supervision of the patient at home should actively search for signs and symptoms of ADR on every visit. Additionally, they need to keep in touch with the patient over the phone to actively enquire about ADRs. Patients should be encouraged to report even the mildest symptoms and record them in the ADR diary. On self-reporting by the patient or on elicitation by a health worker, the treating physician should clinically examine and investigate for the cause. Some of the ADRs like a drug induced gastritis or itching might be mild and managed at the decentralized DR-TB unit level.')   # p131 paragraph missing from every chunk
insert('tb-2025', '0467', 'In addition to the identification of signals and causality assessment, indicators will be useful to assess the coverage of aDSM activities and to summarize the overall AE experience of monitored patients. The ultimate purpose of systematic data collection within aDSM is to enable causality assessment for SAEs, determine their frequency (rates) and detect signals. Even though clinicians skilled in MDR-TB management already attempt to assess relationships between drugs and ADRs and take appropriate clinical action. Nevertheless, formal causality assessment is a separate process that requires the involvement of other experts and is not within the scope of these guidelines.', '## 9.8 Structure and coordination of active pharmacovigilance in Eswatini\n\nThe responsibility for the coordination of pharmacovigilance at the national level in Eswatini has been assigned to the National Pharmacovigilance Unit (NPVU) with the guidance of the National Patient Safety Monitoring Committee (NPSMC) and support from public health programs. The NPSMC is responsible for promoting the optimum safety of medicines used in the country.')   # p185 paragraph missing from every chunk
insert('tb-2025', '0502', '<mark>TB treatment is the same for HIV co-infected patients and HIV negative patients for both drug susceptible and drug-resistant TB (see Chapter 6 &7)</mark>', 'Health workers (skilled, lay and support staff), offenders and correctional facility staff should periodically be screened for TB to identify and treat active disease and provide TPT after active TB is ruled out, regardless of HIV status. HIV testing should, however, be encouraged. Note: Tests of TB infection could be done, if possible, to learn about the risk of transmission to healthcare workers - in those who test negative at baseline.')   # p207 paragraph missing from every chunk
insert('tb-2025', '0717', 'Information gathered on these aspects during the monitoring process provides the basis for the evaluative analysis.', 'Surveillance is the systematic collection, analysis, and reporting of data related to TB infection and disease. The goal of TB surveillance is to help public health agencies prevent the spread of disease, control and treat it, and identify priority needs. The World Health Organization (WHO) has guided TB surveillance since the mid-1990s, including standardized definitions, forms, registers, and reports.')   # p276 paragraph missing from every chunk
insert('tb-2025', '0725', "Once the treatment card is issued, the Patient's identity card is also issued to be kept by the patient, which has all the information from the treatment card and is updated every day.", 'DR-TB Patient File (TB 08) Information relevant to the start and continuation of second-line treatment in a TB patient is entered into the patient’s file. The Patient File is kept at the treatment center or with the health care worker providing DRTB services. A record of the administration of drugs is kept on the file. The file, or a copy of it, must always follow the patient (e.g. from a specialized hospital to an ambulatory facility). The DRTB Patient file is usually opened after a decision is taken to start the patient on treatment and s/he is registered in the (Second line) DRTB treatment register. It is the primary source of information to update this register. Information on the DR-TB Patient file is organized in several blocks: The section on patient information includes demographic and clinical details: Patient name, Address/telephone, Sex, Date of birth (or Age), Initial weight, and Site of disease. The site of disease is denoted as “pulmonary” and “extrapulmonary” in the same way as for basic TB management. This section also includes the Second-line TB treatment registration number (the unique register number assigned at the start of treatment) and the Date of registration.')   # p278 paragraph missing from every chunk
insert('tb-2025', '0733', 'Supervision will mostly be provided by one qualified and knowledgeable member of the TB program staff and/or Implementing partner staff. Additional members of the supervision team may include the medical supervisor, the laboratory supervisor, pharmacists, nurses, and trainees.', 'Supervision will be carried out at all levels of the health infrastructure, with regular visits to all implementing units. Visits should be arranged to selected institutions, organizations, and individuals, and TB patients eventually at home at the peripheral level informed by gaps identified from data. The supervisory team should prepare a draft report during the visit and provide it to the TB staff responsible for immediate action. The main recommendations should be discussed and, if possible, agreed upon during the visit. The report should be short and must include: •• Actions taken since the last visit. •• Main achievements and constraints observed during the visit. •• Recommendations and proposed next steps before the next visit to overcome problems or improve program performance.')   # p281 paragraph missing from every chunk
insert('tb-2025', '0678', '## 14.2 Leprosy', 'Leprosy is a chronic infectious disease caused by the mycobacterial species Mycobacterium leprae (M. leprae). It affects the skin, mucosa of the upper respiratory tract, and the eyes and peripheral nerves (sensory, motor and autonomic nerves). Left untreated, the disease may cause progressive and permanent disabilities. Although Eswatini has eliminated leprosy as a public health threat, health workers should notify the regional TB coordinator of any presumed cases for further assistance with evaluation and linkage to care.')   # p259 leprosy definition paragraph was missing
insert('tb-2025', '0319', '- Maximize transparency in operations', 'The need for support should be assessed and the process of providing support should be initiated by the health system as patients may not request it. However, the health system may not be equipped to provide all forms of support with its resources. In such situations, health system personnel should be able to link the patient to appropriate sources of support. All staff in the DR-TB service delivery institutions and field should be considerate and behave humanely to patients suffering from DR-TB.')   # p129 paragraph was missing
replace('tb-2025', '0126', """Figure 10: TB screening algorithm – HIV-negative individuals 15 years old and above in health facilities installed with X-ray and CAD/AI

1. Adolescents >15 years and adults, HIV negative, attending a health facility -> symptom screen (multi-entry): current cough OR fever OR weight loss OR night sweats.
2. Symptom screen positive -> collect two sputum samples and perform microbiological assessment of active TB.
3. Symptom screen negative -> assess the risk at the respective OPD (high-risk and key vulnerable population groups+; if PLHIV, refer to algorithm 1B).
   - Not high risk -> exit.
   - High risk -> check if CXR screening was done in the past 12 months.
     - Yes (CXR done) -> evaluate for TPT eligibility; provide TPT if eligible.
     - No -> X-ray screen with CAD:
       - CAD negative -> evaluate for TPT eligibility; provide TPT if eligible.
       - CAD positive* -> collect two sputum samples and perform microbiological assessment of active TB.
       - Non-TB abnormal# -> further clinical evaluation; provide TPT if eligible.
4. Microbiological assessment: positive -> initiate TB treatment; negative -> further clinical evaluation; provide TPT if eligible.

Footnotes printed with the figure:
+ Key vulnerable population groups include: TB contacts, PLHIV, miners/ex-miners*, COPD, diabetes mellitus, immunosuppressive conditions (including cancer), undernourished, inmates, smokers, alcohol/substance misuse.
* If CAD reports silicosis positive, refer for further assessment and treatment for silicosis and provision of TPT if eligible.
# Abnormal (not TB): e.g. cardiomegaly, possible cancer, silicosis, etc. (if smoking history is present and possible cancer is identified on the CXR, highly suspicious of cancer).""")   # p59: rewritten from the page; footnotes were missing
drop('tb-2025', '0128-rest')   # p60 footnotes, inside fig-screen-plhiv-cxr
replace('tb-2025', '0135', """Figure 13: TB screening algorithm for miners/ex-miners and their families using CXR and CAD/AI in the occupational health centre

Population: miners and ex-miners undergoing TB and occupational lung disease screening at an Occupational Health Centre with a BME-accredited practitioner. Two parallel checks:
A. Symptom screen (current cough OR fever OR weight loss OR night sweats):
   - Positive -> perform microbiological assessment (if either CXR or symptom screen is positive).
   - Negative -> further clinical evaluation; provide TPT if eligible.
B. Check if CXR screening was done in the past 12 months:
   - Yes -> further clinical evaluation; provide TPT if eligible.
   - No -> X-ray screen with CAD and human reader:
     - Negative -> further clinical evaluation; provide TPT if eligible.
     - TB positive -> perform microbiological assessment; AND ask: had (current or prior) active TB occurred within a year of mining?+ If yes: if silicosis-negative and TB-positive, refer to a 2-person MBOD panel -> submit results to CCMS (Compensation Claims Management System) for adjudication by MBOD/CCOD.
     - Abnormal other than TB (e.g. silicosis) -> refer to a 4-person MBOD panel for clinical assessment including silicosis diagnosis -> submit results to CCMS for adjudication by MBOD/CCOD.
Microbiological assessment: positive -> initiate active TB treatment; negative -> perform clinical assessment including LTBI; provide TPT if eligible.

Note: CAD reading for silicosis is only a preliminary reading; confirmation is by a human expert reader.
+ Active and (inactive) 'post-TB' are both eligible for compensation if active TB occurred as a miner or within one year of leaving the mines, OR with silicosis.""")   # p62 rewritten from the page
replace('tb-2025', '0138', """Figure 14: TB screening algorithm for health care workers using CXR and CAD/AI in the wellness centre

Population: healthcare workers (annual screening with TB symptoms and CXR) at wellness clinics. Two parallel checks:
A. Symptom screen (current cough OR fever OR weight loss OR night sweats): positive -> see "if either or both are positive" below; negative -> evaluate and provide TPT if eligible.
B. Check if CXR screening was done in the past 12 months: yes -> evaluate and provide TPT if eligible; no -> X-ray screen with CAD:
   - CAD negative -> evaluate and provide TPT if eligible.
   - CAD positive* -> see below.
   - Non-TB abnormal* -> further clinical evaluation; provide TPT if eligible.
If either or both (symptom screen, CAD) are positive -> collect two sputum samples and perform microbiological assessment of active TB: positive -> initiate active TB treatment; negative -> further clinical evaluation; provide TPT if eligible.

Also assess risk factors like smoking and HIV infection; if PLHIV, refer to the screening algorithm for HIV.
* Abnormal (not TB): e.g. cardiomegaly, possible cancer, silicosis, etc. (if smoking history is present and possible cancer is identified on the CXR, highly suspicious of cancer).""")   # p63 rewritten from the page; footnotes were missing
replace('tb-2025', '0141', """Figure 15: TB screening algorithm (3) for community member children and adults attending the Integrated Mobile Clinic (IMC)

Population: community members (children and adults) residing in communities identified through hotspot mapping+. Two parallel checks:
A. Symptom screen (current cough OR fever OR weight loss (poor weight gain or history of contact in children <10 years) OR night sweats): positive -> see "if either or both are positive" below; negative -> evaluate and provide TPT if eligible.
B. Check if CXR screening was done in the past 12 months: yes -> no CXR; provide TPT if eligible. No -> chest X-ray read by CAD for >15 years and by a human reader for <15 years:
   - Negative -> evaluate and provide TPT if eligible.
   - Positive* -> see below.
   - Non-TB abnormal# -> refer for re-read by a human reader and further clinical evaluation.
If either or both are positive -> collect two sputum samples (if <5 years or cannot produce sputum, collect one stool sample) and perform microbiological assessment of active TB: positive -> initiate active TB treatment; negative -> further clinical evaluation; provide TPT if eligible.

+ Criteria to identify hotspots include: miners/ex-miners, factory workers and their respective communities, correctional inmates (annual screening), populations with structural risk factors for TB and limited access to healthcare, TB contacts, PLHIV, COPD, reported outbreaks.
* If CAD reports silicosis positive, refer for further assessment and treatment for silicosis and provision of TPT if eligible.
# Abnormal (not TB): e.g. cardiomegaly, possible cancer, silicosis, etc. (if smoking history is present and possible cancer is identified on the CXR, highly suspicious of cancer).""")   # p64 rewritten from the page; footnotes were missing
replace('tb-2025', '0164', """Figure 16: TB and DR-TB diagnostic and treatment decision algorithm

Presumptive TB (symptoms and/or CXR suggestive of TB) -> collect 2 specimens -> Xpert MTB/RIF Ultra (and urine LAM for PLHIV with CD4 <200 regardless of TB signs/symptoms, presumptive TB regardless of CD4, or seriously ill@ regardless of CD4 count). For PLHIV, start treatment if urine LAM is positive even when the Xpert test is negative; when the Xpert result is received, follow the algorithm.
Xpert result:
- MTB detected, RR detected*: start DR-TB treatment with the short all-oral regimen according to national guidelines -> test with SLPA/Xpert XDR, C&DST and NGS -> adapt the regimen if required according to the DST result.
- MTB detected**, RR not detected: start first-line drugs (FLD) -> test the 2nd sample with Xpert XDR/FLPA and pDST -> perform NGS for Hr/PDR-TB and adapt the regimen according to the DST result.
- Error / invalid / no result / RIF indeterminate: repeat the Xpert test*** and follow the same algorithm.
- MTB not detected: re-evaluate the clinical condition# -> clinically diagnosed TB: start treatment and send for C&DST, adapt the regimen if required according to the DST result; not diagnosed as TB: manage for other diseases, start TPT if eligible.
(Footnotes for **, ***, @ and # follow in the next chunk: trace results, indeterminate RR, seriously ill adult/child, clinical evaluation.)""")   # p72 rewritten from the page
replace('tb-2025', '0169', """Figure 17: Interpretation of trace result from the Xpert MTB/RIF (Ultra) test

MTB trace detected:
- Previous history of TB, HIV negative, adolescents and adults ≥15 years, pulmonary TB -> repeat (with an early morning sample):
  - MTB+ or trace -> treat.
  - MTB- -> clinical assessment: suggestive of TB -> treat; not TB -> evaluate for other morbidity.
- No previous history of TB (HIV negative), PLHIV, children <15 years, EPTB -> treat.
After treatment starts: culture and DST (Xpert XDR, pDST, tNGS) -> clinical assessment / adjust treatment based on the DST results.
(Acronyms: PTB pulmonary TB; EPTB extra-pulmonary TB; MTB+ TB positive; MTB- TB negative; DST drug susceptibility test.)""")   # p74 rewritten from the page
replace('tb-2025', '0291', """Figure 20: Algorithm for treatment selection and modification (DR-TB)

Patient diagnosed as MDR/RR-TB or PDR-TB or failed Hr-TB treatment -> collect 2 sputum specimens for LPA, SM, TBC and DST and perform other clinical and lab tests.
1. Check exclusion criteria to BPaLM: NO to all -> start BPaLM. YES to any -> step 2.
2. Check exclusion for 6 Bdq-Dlm-Lfx-Lzd-Cfz: NO to all -> start 6 Bdq-Dlm-Lfx-Lzd-Cfz. YES to any -> step 3.
3. Check exclusion for the 9-month regimens*: NO to all -> start one of the 9-month regimens. YES to any -> start a longer regimen/ITR.
4. For every regimen: check second-line LPA / Xpert MTB XDR, NGS, pDST:
   - FQ-S only# -> continue the same treatment regimen.
   - FQ-R only# -> omit the FQ (Mfx/Lfx) for those on BPaLM and 6-Bdq-Dlm-Lzd-Lfx-Cfz; for those on 9-month regimens, change to a longer regimen/ITR.
   - FQ-S or FQ-R with additional drug resistance## -> discuss with the CAC and adjust the treatment regimen if required.
# = no other second-line drug resistance (e.g. Bdq, Cfz, Lzd, Cs); ## = other second-line drug resistance (i.e. Bdq, Cfz, Lzd, Cs).""")   # p118 rewritten from the page; footnote was missing
_paed = """1. Danger signs requiring urgent medical care? Yes -> stabilize and/or transfer as needed (if transferred: exit; if retained: continue to step 2). No -> step 2.
2. Child <2 years old, living with HIV, and/or with severe acute malnutrition?
   - Yes -> step 3.
   - No -> treat the most likely non-TB condition(s) and follow up in 1-2 weeks; if symptoms persist/worsen -> step 3; if not -> exit.
3. Collect respiratory/stool specimens for mWRD testing (e.g. Xpert MTB/RIF or Ultra), including, in children living with HIV, urine LF-LAM if available.
4. If performed, did mWRD or LF-LAM detect Mycobacterium tuberculosis? Yes -> initiate appropriate TB treatment. No / not performed / result not yet available -> step 5.
5. Close or household TB contact in the previous 12 months? Yes -> initiate appropriate TB treatment. No -> step 6.
"""
replace('tb-2025', '0362', "Figure 21: Decision tree for TB treatment in children <10 years old – Algorithm A (settings where CXR is available)\n\nChild <10 years with symptoms suggestive of pulmonary TB:\n" + _paed + """6. Score signs and symptoms and CXR features:
   - Signs and symptoms (Sum A): cough longer than 2 weeks +2; fever longer than 2 weeks +5; lethargy +3; weight loss +3; haemoptysis (coughing up blood) +4; night sweats +2; swollen lymph nodes +4; tachycardia +2; tachypnoea -1.
   - Chest X-ray (Sum B): cavity/cavities +6; enlarged lymph nodes +17; opacities +5; miliary pattern +15; effusion +8.
7. Is Sum A + Sum B > 10? Yes -> initiate appropriate TB treatment. No -> do not treat with TB treatment; follow up in 1-2 weeks and score again.
(Source: WHO Operational Handbook on Tuberculosis, Module 5: Management of Tuberculosis in Children and Adolescents, 2022)""")   # p145 checked against the page
replace('tb-2025', '0364', "Figure 22: Decision tree for TB treatment in children <10 years old – Algorithm B (settings where CXR is not available)\n\nChild <10 years with symptoms suggestive of pulmonary TB:\n" + _paed + """6. Score signs and symptoms: cough longer than 2 weeks +5; fever longer than 2 weeks +10; lethargy +4; weight loss +5; haemoptysis +9; night sweats +6; swollen lymph nodes +7; tachycardia +4; tachypnoea +2.
7. Is the sum > 10? Yes -> initiate appropriate TB treatment. No -> do not treat with TB treatment; follow up in 1-2 weeks and score again.
(Source: WHO Operational Handbook on Tuberculosis, Module 5: Management of Tuberculosis in Children and Adolescents, 2022)""")   # p146 checked against the page
replace('tb-2025', '0473', """Figure 29: Management of Peripheral Neuropathy

- Causative medications: INH, LZD.
- Signs and symptoms: burning and tingling in the hands and feet, loss of reflexes.
- Prevent peripheral neuropathy by giving all patients on INH pyridoxine at a dose of 50 mg/day. Monitor for peripheral neuropathy with monthly clinical screening.
- Assess and correct other causes, including alcohol use, other medication such as D4T, diabetes, vitamin deficiency. Then assess severity and manage:
  - Mild / Grade 1 (little to no discomfort): analgesia required; correct other causes; monitor every 2 weeks; could lower the dose of LZD if the patient has received 2 months of treatment.
  - Moderate / Grade 2 (some discomfort; non-narcotic analgesia required and improves symptoms): correct other causes; monitor every 2 weeks; hold LZD and CS; if symptoms improve, reintroduce LZD at 300 mg daily and consider discontinuation of CS.
  - Severe / Grade 3 (severe discomfort; narcotic analgesia required and improves symptoms): correct other causes; monitor every 2 weeks; discontinue LZD and CS and give DLM.
  - Life-threatening / Grade 4 (incapacitating; narcotic analgesia required and does not improve symptoms): correct other causes; monitor every 2 weeks; discontinue LZD and CS and give DLM.
- Ancillary medication for treatment includes gabapentin, amitriptyline (used with caution with other QTcF-prolonging drugs). Physical therapy should be initiated.""")   # p187 checked against the page
replace('tb-2025', '0476', """Figure 30: Management of Optic Neuropathy

- Causative medications: EMB, LZD.
- Signs and symptoms of optic neuritis/neuropathy: loss of visual acuity, loss of red/green colour vision, development of blind spots.
- (A box printed beside this figure reads: monitor for anaemia/thrombocytopenia by checking baseline and monthly FBC and any time there are symptoms.)
- Assess by an ophthalmologist if possible. Other causes are rare but could include presbyopia, trauma, temporal arteritis. Then assess severity and manage:
  - Mild / Grade 1 (asymptomatic; clinical observations or findings only), Moderate / Grade 2 (limiting vision of the affected eye), Severe / Grade 3 (severely limiting vision of the affected eye) and Life-threatening / Grade 4 (blindness in the affected eye): at every grade, stop LZD and EMB immediately if optic neuritis is suspected; only restart if an ophthalmologic exam is done and is normal; substitute LZD with DLM.""")   # p188 checked against the page

# ---------------- NCDIMH ----------------
drop('ncdimh', '0187-rest')                  # p68 vertigo test text placed under osteoporosis p66; tbl-osteoporosis-assessment-checklist has it
drop('ncdimh', '0377-rest', '0377-rest-a')   # p138 column headers + numbered items, inside tbl-stroke-acute-contraindications-secondary
drop('ncdimh', '0043-rest', '0850-rest-a')   # one-line lead-ins to items that carry their own titles (5 A's table, diabetic foot algorithm)
insert('ncdimh', '0984-rest', '', """**For Patients with Predominant Asthma Characteristics:**
* **Corticosteroids:** Prescribe inhaled corticosteroids (ICS) to manage inflammation. It is important to note that long-acting bronchodilators should not be used as monotherapy in these cases.""")   # p344 paragraph was missing
replace('ncdimh', '0408-rest', '### **Atopic Dermatitis AD (Eczema)**\nChronic, pruritic inflammatory skin condition that occurs most frequently in children but may also affect adults. It follows a relapsing course. AD is often associated with elevated serum immunoglobulin levels and a family history of Type 1 allergies such as Allergic Rhinitis and Asthma.', heading_path='Chapter 4: Dermatology > Atopic Dermatitis (Eczema)')   # eczema intro was labelled with the CHD flowchart section
replace('ncdimh', '0462-rest', '## Gastritis\n\nThis is an inflammatory mucosal response to injury from variety of agents and mechanisms including infections, drugs, alcohol, acute stress, radiation, allergy, acid and bile, ischemia or direct trauma. The inflammation may involve the entire stomach (pangastritis) or a region of the stomach (antral gastritis) while the severity of inflammation may be erosive or non-erosive.', heading_path='Chapter 5: Gastroenterology and Hepatology > Gastritis')   # p168 'Gastritis' heading was lost
drop('hiv-amendment-2024', '0056-rest-a')        # p29 question, inside fig-7.2 (resurfaced after 0054-rest was dropped)
drop('unaids-linkages-sop', '0143-rest-a')       # p91 stray line, inside tbl-p91-0143 (resurfaced after 0142 was dropped)
drop('ncdimh', '0002')                       # p2 title-page text only
strip('ncdimh', '0508', ' Primary Brain Injury')   # p183 trailing heading of the next item (tbl-tbi-primary-secondary)
