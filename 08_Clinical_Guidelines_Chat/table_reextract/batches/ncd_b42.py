exec(open('batches/ncd_common.py').read())
SP = CH6 + " > Spinal Injury"
ITEMS = [
 D("fig-spinal-injury-assessment", 179, SP + " > Spinal Injury Assessment",
   "Spinal injury assessment after trauma (flowchart: when spine injury is possible vs can be excluded clinically)", ["0494"],
   "1. Blunt trauma with a mechanism suspicious for spine trauma? Yes →\n"
   "2. Is the patient awake, alert and reliable?\n"
   "   - No → possible spine injury.\n"
   "   - Yes → 3. Severely injured patient? Evidence of intoxication? Neurological deficit? Thoracic or other significant distracting injury?\n"
   "     - Yes → possible spine injury.\n"
   "     - No → 4. Significant spine pain or tenderness (7/10)?\n"
   "       - Yes → possible spine injury.\n"
   "       - No → 5. Is the patient voluntarily able to flex, extend and rotate the spine in each plane regardless of pain (45° cervical spine, 30° thoracolumbar)?\n"
   "         - Yes → no spine injury.\n"
   "         - No → possible spine injury.\n"
   "Isolated penetrating trauma: Yes → no spine injury.",
   ["'WMS' is printed on the chart without explanation. 'susoicious', 'Severrly' printed.",
    "'Isolated penetrating trauma → no spine injury' is printed as is; penetrating injuries are listed as a cause of spinal injury on p.178. Clinician to confirm."]),
 T("tbl-spinal-injury-management", 180, SP + " > Management by level of care",
   "Spinal injury management by level of care: facilities without vs with an orthopaedic surgeon", ["0496", "0497", "0498"],
   [[C("Level of Care"), C("Management")]],
   [[C("Health facilities without orthopaedic surgeon"), L("Give anti-inflammatory analgesics.", "If open wound: administer tetanus toxoid (per EPI schedule) and appropriate antibiotics.", "Maintain spinal precautions: apply cervical collar or secure on a hard board; practice log rolling always; provide spinal immobilization during transport; continue resuscitation during transportation.", "Perform surgical toilet for associated injuries if facilities are available before referral.", "Refer to orthopaedic and neurosurgery department for acute treatment.", "Transfer even if clinical manifestations appear minor.")],
    [C("Health facilities with orthopaedic surgeon"), L("Manage bone injuries with appropriate orthopaedic surgeries.", "Perform spinal decompression and stabilization as indicated.", "Maintain skin, bladder, and bowel care.", "Initiate rehabilitation: physiotherapy, occupational therapy, prosthetic and orthotic fittings.")]],
   context_before="Investigations: plain spinal radiographs; CT scan or MRI where available. It is critical to maintain cervical stability during transfer and examination, hence apply a cervical collar."),
 T("tbl-snake-venom-types", 181, CH6 + " > Snakebite Envenomation > Envenomation syndromes",
   "Snakebite envenomation syndromes in Eswatini: venom type, snake species, clinical features and antivenom (cytotoxic, neurotoxic, mixed, haemotoxic)", ["0502"],
   [[C("Venom type"), C("Snake species"), C("Clinical features of envenomation"), C("Antivenom (when indicated)")]],
   [[C("Cytotoxic"), C("Puff adder, Gaboon adder, spitting cobras (Mozambique, black-necked, zebra), stiletto snake, night adders, horned adders"), C("Pain, swelling, bruising, blisters, necrosis, regional lymphadenopathy, hypotension, coagulopathy, compartment syndrome"), C("Polyvalent antivenom for puff adder, Gaboon adder and spitting cobras only")],
    [C("Neurotoxic"), C("Black and green mamba, non-spitting cobras (Cape, forest, snouted)"), C("Pins and needles, metallic taste, visual disturbances, ptosis, drowsiness, sweating, drooling, dysphagia, progressive weakness, respiratory paralysis"), C("Polyvalent antivenom for all species")],
    [C("Mixed (cytotoxic and neurotoxic)"), C("Rinkhals, Berg adder, Peringuey's adder, desert mountain adder, garter snakes, shield nose snake, coral snake"), C("Combined cytotoxic and neurotoxic features"), C("Polyvalent antivenom for rinkhals only")],
    [C("Haemotoxic"), C("Boomslang, vine snakes"), C("Spontaneous bleeding (can present late, >24 hours after bite), headaches, dizziness, fainting"), C("Boomslang monovalent antivenom for boomslang bites only")]],
   source_flags=["The PDF table is laid out with venom types as columns; transposed to one row per venom type."]),
]
SB = CH6 + " > Snakebite Envenomation"
ITEMS += [
 T("tbl-snakebite-management-by-venom", 182, SB + " > Management by Venom Type",
   "Snakebite management by venom type: supportive treatment, signs of severe envenomation, antivenom type, administration, starting and additional doses (mixed, cytotoxic, neurotoxic, haemotoxic)", ["0504", "0505"],
   [[C("Step"), C("PPS/PW syndrome: mixed cytotoxic & neurotoxic venom"), C("PPS syndrome: cytotoxic venom"), C("Neurotoxic venom (mambas, non-spitting cobras)"), C("B. syndrome: haemotoxic venom")]],
   [[C("Snakes"), C("Rinkhals, berg adder, desert mountain adder, garter snakes, shield-nose snake"), C("Puff adders, Gaboon vipers, spitting cobras (Mozambique, black-necked, black, zebra), stiletto snakes, night adders, horned adders"), C("Black and green mamba, non-spitting cobras (snouted, Cape forest)"), C("Boomslang, vine snake")],
    [C("Supportive treatment"), C("IV fluids; analgesia; protect airway"), C("IV fluids; elevate limb; analgesia"), C("IV fluids; protect airway by mask or ventilation"), C("IV fluids; blood or blood component therapy. Heparin and anti-fibrinolytics are of no value and may be dangerous")],
    [C("Analgesia (all)"), C("Paracetamol. NOT aspirin or non-steroidal anti-inflammatory medicines", cs=4)],
    [C("Severe envenomation anticipated if"), C("Drowsiness, nausea, vomiting, vertigo, mild pyrexia, dyspnoea, general weakness"), C("Severe pain; swelling > 5 cm/hour; swelling to elbow or knee by 6 hours; swelling of whole limb in 12 hours; bleeding abnormalities"), C("Metallic taste; profuse sweating; paraesthesia; excessive salivation; shortness of breath; difficult swallowing; ptosis; fasciculation"), C("Fang punctures do not stop bleeding; severe headaches; dizziness; fainting; convulsions. NB: 20 min clot test")],
    [C("Antivenom administration (all)"), C("Insert IV line (not in the bitten limb). Pretreatment: predose of adrenaline 0.25 mg (quarter ampoule) subcutaneously on either thigh, abdominal wall or forearm. A doctor administers the antivenom. No test dose required.", cs=4)],
    [C("Antivenom needed to treat (life over limb)"), C("Rinkhals"), C("Puff adder, spitting cobras, Gaboon adder"), C("All species"), C("Boomslang")],
    [C("Antivenom type and how to give"), C("Polyvalent: add antivenom vials to 200 ml saline, infuse over 30 minutes. Example: if 8 vials are used, remove 80 ml (10 ml per vial) from the saline bag and add the 8 vials of antivenom", cs=2), C("Polyvalent. Atropine + neostigmine: cobras only"), C("Monovalent: IV push 1 ampoule/min OR diluted 50/50 in isotonic fluid infused over 15-30 minutes")],
    [C("Starting dose of antivenom IV"), C("Rinkhals: 50 ml"), C("Puff adder: 50-100 ml. Mozambique spitting cobra: 100 ml+. Gaboon adder: 200 ml"), C("Black mamba, snouted cobra: 80-200 ml"), C("Boomslang, vine snake: 20 ml")],
    [C("Additional antivenom"), C("Monitor progression of swelling hourly. If swelling continues, give 2 additional ampoules of antivenom until swelling stops", cs=2), C("Monitor neurological symptoms closely. If no improvement after 30 minutes, give an additional 4 vials. Repeat as necessary"), C("If the blood remains incoagulable 6 hours after the first antivenom dose, repeat the dose until blood coagulability is restored")],
    [C("Monitoring (all)"), C("Monitor for signs of reactions and anaphylaxis: urticaria, itchiness, bronchospasm, and BP every 3 minutes for hypotension, with continuous O2 saturation monitoring", cs=4)]],
   footnotes=["Sources printed: adapted from the South African Snakebite Symposium 2022; Snake Management South African Consensus Guideline (SAA 2022); Swaziland Antivenom Foundation 2018; Netcare ISO ED 00107 V1 Nov 2019; Blaylock 2005 and Muller et al SAMJ 2012 (use of atropine and neostigmine).",
              "Administration of antivenom (highlighted box): give the first dose (10 ml) of antivenom IV at a slow rate of 1-2 ml per minute. Subsequent doses may be injected into a saline drip, no more than 20 ml per 500 ml bag, to run in 30 mins. Repeat until symptoms resolve. Monitor breathing and other vital signs continuously. Do not run the drip into the bitten limb, which should be kept elevated and well protected.",
              "Have adrenaline (1:1,000) at the bedside in case of anaphylaxis. If the patient has known allergies (asthma etc.), draw up the adrenaline (0.3-0.5 ml for adults and 0.1-0.3 ml for children) and have an antihistamine available. Antihistamine is NOT recommended as routine treatment for snakebite. DO NOT infiltrate the bite area with antivenom."],
   source_flags=["The third column is headed 'B. Syndrome Haemotoxic Veno' (same as the fourth) but lists mambas and non-spitting cobras with neurotoxic signs; labelled neurotoxic here.",
                 "Dosing instructions conflict: the chart gives starting doses of 20-200 ml diluted in 200 ml saline over 30 min, while the box below says first dose 10 ml IV at 1-2 ml/min, then no more than 20 ml per 500 ml bag. Clinician to confirm.",
                 "The mixed-venom column lists drowsiness, nausea, vertigo, pyrexia as signs of severe envenomation, unlike the usual cytotoxic/neurotoxic signs.",
                 "Flowchart-style chart in the PDF; restructured as a table. Several typos ('Booslang', 'Rinkhais', 'garder', 'Ptosisis', 'No lest dose', 'Staring dose', 'ANTIVENON')."]),
]
