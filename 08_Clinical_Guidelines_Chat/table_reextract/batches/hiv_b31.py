exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.229-239 (Chapter 9: adolescent SRH, transition to adult care, DSD, programme elements, monitoring
# timelines). From the page images.
C9 = "Chapter 9: ART for Children and Adolescents"
TR = C9 + " > 9.14 Transitioning to Adolescents to Adult Care"
ITEMS = [
 D("fig-9.8-contraceptive-options", 229, C9 + " > Pregnancy Prevention in Adolescents Living with HIV > Figure 9.8", "Figure 9.8 Contraceptive Options available to all Adolescents in Eswatini", [],
   "Key message (box above the figure): WHO recommends Long-Acting Reversible Contraception (IUD, Implants) as first choice for adolescent girls and young women wishing to prevent unwanted pregnancies. They are the most effective, safe and allow a swift return to fertility when a pregnancy is desired. ALWAYS counsel on the importance of dual protection for ALL methods of contraception.\n\n"
   "Contraceptive options available to all adolescents in Eswatini (figure of hexagons with photographs):\n"
   "- Male/female condoms (adolescent friendly colors/flavors)\n- IUD (copper or hormonal)\n- Progestin only injectable contraception (Depo, NST)\n"
   "- Implants (Jadelle or Implanon)\n- Emergency contraception (ECP)\n- Oral contraceptive pills (COCs/POP)"),
 D("fig-9.9-stages-of-transition", 232, TR + " > Figure 9.9", "Figure 9.9 Major components of different stages of transition", ["0635"],
   "Three stages of transition (three columns):\n"
   "Paediatric (2-14 yrs):\n- Dependent on caregiver for care and ART adherence\n- Start and completion of disclosure to the child\n- Psychosocial support via art and games therapy\n- Self-care with a focus on hygiene, basic nutrition, and puberty\n\n"
   "10-24 yrs:\n- Shift in responsibility, with client more accountable for adherence\n- Disclosure of HIV status\n- Participation in support/peer groups and clubs\n- Knowledge about HIV in relation to life and relationships\n- Establishment of own treatment goals and plans\n- Preparation for adult care and transition\n\n"
   "15+ yrs:\n- Completion of transition to independent clinical and self-care\n- Service options: young adult clubs, male adherence clubs, prevention of perinatal HIV transmission, mother-baby care, family clinics, and community antiretroviral therapy groups\n- Client-led psychosocial support: maintaining supportive networks via online groups and discussions sharing personal successes, job opportunities, HIV events, and more",
   flags=["The age bands of the three stages overlap as printed (2-14, 10-24 and 15+ years)."]),
 D("fig-9.10-transition-steps", 232, TR + " > Transition steps > Figure 9.10", "Figure 9.10 Transition Steps", ["0638"],
   "Transition steps (left to right):\n1. Assess child/adolescent and caregiver's readiness and skills\n→ 2. Prepare child/adolescent and caregiver for transition process\n"
   "→ 3. Review progress and engage transition team (MDT)\n→ 4. Transfer care for child/adolescent\n"
   "→ 5. Follow-up with child/adolescent and caregiver to ensure maintenance of good clinical outcomes",
   pages=[232, 233],
   flags=["The text before the figure refers to the readiness criteria with a broken cross-reference ('see Error! Reference source not found.'); the criteria are in Table 9.17."]),
 T("tbl-9.17-transition-checklist", 233, TR + " > Table 9.17", "Table 9.17 Checklist for Successful Transitions to Adult Care", ["0640", "0641"],
   [r("Skills an Adolescent Should Have Before Transitioning to Adult Care", "Checklist for Successful Transition")],
   [[L("Know when to seek medical care for symptoms or emergencies.", "Identify symptoms and describe them.", "Make, cancel and reschedule appointments.",
       "Arrive at appointments on time.", "Call ahead for urgent visits.", "Can name/describe his/her medications and the doses",
       "Request prescription refills correctly and allow enough time for refills to be processed before medications run out.",
       "Knows when his/her last viral load test was done", "Knows results of his/her last viral load test",
       "Understands what the viral load test results mean for his/her treatment",
       "Establish a good working relationship with healthcare workers at the paediatric/adolescent site, which will enable the adolescent to work effectively with the healthcare worker at the adult site.",
       "Negotiate multiple providers and subspecialty visits (for other services).", "Condom use skills", "Contraception access and usage",
       "Readiness to join adult support groups"),
     L("The client has accepted their chronic illness and is oriented toward future goals and hopes, including long-term survival.",
       "The client has learned the skills needed to negotiate appointments and multiple providers in an adult practice setting.",
       "The client has achieved personal and medical independence and can assume responsibility for his/her treatment and participate in decision-making.",
       "The referring provider is familiar with the new provider and practice setting, and direct communication about an individualized plan for the client has taken place.",
       "The client is receiving psychosocial support (peer, family, facility) and entitlements are in place (housing, home care, transportation).",
       "Life skills have been addressed (e.g., educational goals, job training, parenting).",
       "The client receives uninterrupted comprehensive medical care.", "Sexual reproductive health and family planning.", "Consistent and correct condom use.")]],
   pages=[233, 234],
   footnotes=["The two columns are independent lists (items in the same row are not paired). Header as printed: 'Skills and Adolescent Should Have…'."]),
 B("box-teen-clubs", 235, C9 + " > 9.16 Differentiated Service Delivery for children and adolescents > Differentiated care models", "Teen Clubs (key message)", ["0647", "0648"],
   "Key message: All facilities must have Teen Clubs. Facilities should have dedicated days for children especially those that are failing treatment with a multidisciplinary team to review these failing clients whenever possible.\n\n"
   "(Multi-month dispensing, same section: after the age of two years, ART refills and clinical consultations for stable CALHIV can be extended to 3-monthly for younger children (ages 2-5 years) and 6 months for ≥5 years and adolescents.)"),
 D("fig-9.11-retention-framework", 236, C9 + " > 9.16 Differentiated Service Delivery for children and adolescents > Figure 9.11", "Figure 9.11 Improving CALHIV continuity in care requires a mix of preventive and responsive strategies", ["0650"],
   "Paediatric and adolescent Retention Framework (centre), with four linked components:\n"
   "- Trained HCWs: high quality comprehensive paediatric care; ART optimization; child/adolescent friendly services\n"
   "- Active patient tracking: prompt identification of missed appointments and rescheduling; active community tracing efforts; back to care initiatives; paediatric AHD\n"
   "- Supportive services: increase enrollment of CALHIV in OVC/DREAMS programs; referrals for additional support; virtual support\n"
   "- DSD models: MMD; peer-peer support (adolescents, caregivers); family centered care; facility fast track; child/teen clubs; community based models (DDD, outreach)\n\n"
   "Source: adapted from \"Leveraging decentralized drug distribution models to meet the HIV treatment needs of children and adolescents living with HIV\", Decentralized Drug Distribution (DDD) Learning Collaborative, May 2021."),
 T("tbl-9.18-paediatric-programme-elements", 237, C9 + " > 9.17 Elements of a Well-Functioning Paediatric HIV Program > Table 9.18", "Table 9.18 Elements of a Well-Functioning Paediatric HIV Program", ["0652", "0654"],
   [r("Program Area", "Specific Elements")],
   [[C("Paediatric testing"), L("Dried blood spot kits, HTS kits", "Disclosure materials")],
    [C("Care and treatment"), L("Paediatric ARV formulations", "NVP clips and syringes", "Pill cutters/pill boxes", "Dosing charts", "Adolescent services—family planning, cervical cancer screening", "Access to clinical psychologist")],
    [C("Client education"), L("Paediatric ARV formulations", "Information, education and communication materials on paediatric ART", "Disclosure counselling materials", "U-report", "Income generating skills development")],
    [C("Job aids"), L("WHO clinical stages posters", "Neurological developmental stages", "Dried blood spot posters", "ART and ARV dosing guidelines", "Stepped-up adherence counselling")],
    [C("Phlebotomy"), L("Blood collection tubes and Butterfly needles for phlebotomy", "VL required materials (For plasma and DBS VL)")],
    [C("Differentiated Service Delivery"), L("Teen Clubs, paediatric-specific days, fast track, peer support, mother-baby clubs, family-centred models")],
    [C("Materials for teen clubs and other differentiated models of paediatric care"), L("HIV and sexual and reproductive health curriculum for teen clubs", "Community-Centred Models of ART Delivery (CommART) Guidelines and SOPs", "Tools and job aids", "Condom demonstrations and distribution")],
    [C("Post-exposure prophylaxis paediatric materials"), L("Counselling tools", "Post-exposure prophylaxis drugs package for partners", "PrEP as per the need for partners")],
    [C("Marketing materials on our telemedicine options"), L("DBS hotline, Baylor HIV/TB Hotline (7848-5571), U-Report, Paediatric specific days")]],
   pages=[237, 238]),
 T("tbl-9.19-monitoring-timelines-children", 239, C9 + " > 9.18 Summary of Monitoring and Clinical Service Timelines for Paediatrics and Adolescents > Table 9.19", "Table 9.19 Summary of Monitoring and Clinical Service Timelines for Children and Adolescents", ["0657"],
   [r("Test", "Baseline", "2 weeks", "1 month", "3 months", "6 months", "9 months", "12 months", "Thereafter")],
   [r("CD4 count or %", "X", "", "", "", "X", "", "", "Every 6 months if detectable VL or when clinically recommended"),
    r("Viral load", "None", "", "", "", "X", "", "X", "Every 6 months for ages 0–19 years"),
    [C("Haemoglobin"), C("X"), C("If clinically indicated (e.g., If on AZT, regimen, do Hb every 6 months)", cs=7)],
    r("AST/ALT", "As clinically indicated", "", "", "", "", "", "", "As clinically indicated"),
    r("Creatinine", "TDF only", "", "", "", "TDF only", "", "TDF only", "Every 6 months if on TDF"),
    r("TB-LAM (TB symptoms present)", "For children and adolescents with a CD4 count ≤ 100 cells/mm³ or less than 25%.", "", "", "", "", "", "", "For children and adolescents with a CD4 count ≤ 100 cells/mm³ or less than 25%."),
    r("CrAg screening", "For children (older than 10 years) and adolescents with a CD4 count ≤100cells/mm³ or less than 25%.", "", "", "", "", "", "", "Rescreen every child older than 10 years with CD4 count ≤100cells/mm³ or less than 25% regardless of frequency")],
   context_before="Caption printed on p.238 above the table (section heading 9.18); the grid is on p.239. The first header cell is blank in the source.",
   pages=[238, 239],
   source_flags=["Table 9.19 schedules VL at 6 and 12 months then every 6 months for ages 0–19 years; check against the 2024 Amendment VL monitoring schedule."]),
]
