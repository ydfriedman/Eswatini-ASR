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
        _cache[doc].update(text_add=[], text_replace={}, text_strip={})
    return _cache[doc]
def drop(doc, *cids):
    s = spec(doc).setdefault('text_drop', [])
    for c in cids:
        c = c if c.startswith(doc) else f'{doc}-{c}'
        if c not in s: s.append(c)
def merge(doc, src, dst):
    spec(doc).setdefault('text_merge', {})[f'{doc}-{src}'] = f'{doc}-{dst}'
def replace(doc, cid, text, page_end=None):
    spec(doc).setdefault('text_replace', {})[f'{doc}-{cid}'] = dict(text=text.strip(), page_end=page_end) if page_end else text.strip()
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
