exec(open('batches/lk_common.py').read())
A = "14 Annex"
ITEMS = [
 D("fig-annex1-positive-facility", 99, A + " > 14.1 Annexure 1 Linkages for Client Testing Positive in the Facility", "Annexure 1. Linkages for a client testing HIV positive in the facility: true new positive verification (CMIS/APMR), RTT package, readiness assessment, retesting, ART initiation, LCM enrolment", ["0165", "0166"],
   "1. Tested HIV positive → true new positive verification (CMIS, APMR).\n"
   "2a. Found in any of the information systems → provide the RTT (return to treatment) package: welcome the client, support, do not be judgmental, review last treatment, refer client for counselling → readiness assessment.\n"
   "2b. Not found in any information system → readiness assessment.\n"
   "3. Ready → retesting for verification as per the HTS algorithm → initiate ART as per ART initiation guidelines → enrol into LCM → offer prevention package (e.g. TPT, CaCx) → follow the client as per LCM guidance to ensure retention.\n"
   "4. Not ready → enrol into LCM; escalation counselling (doctor, nurse, social worker, HTS provider, expert client, psychologist) → follow the client as per LCM guidance until initiation → offer prevention package (TPT, CaCx) → follow as per LCM guidance to ensure retention.",
   ["The flowchart prints 'CMIS.APMAR'; elsewhere the system is 'APMR'."]),
 D("fig-annex2-returning-to-care", 100, A + " > 14.2 Annexure 2 Linkages for Client Returning to Care", "Annexure 2. Linkages for a client returning to care by interruption type: missed appointment (<28 days), early interrupters (28 days-6 months), late interrupters (>6 months) – RTT package, enhanced adherence counselling, escalation", ["0167", "0168"],
   "HIV positive → verify previous HIV-positive / ART registration in any system (CMIS, APMR) – found in system:\n"
   "- Missed appointment and defaulter (immediate interrupters, <28 days post initiation) → offer relevant prevention services according to client's preferences → enrol client into LCM.\n"
   "- Interruption in treatment (LTFU), early interrupters (>28 days up to 6 months post initiation) → provide RTT package → enhanced adherence counselling.\n"
   "- Interruption in treatment (LTFU), late interrupters (>6 months on ART) → provide RTT package → counsel client based on EAC for late interrupters guidelines to ascertain barriers → escalate client based on needs after ascertaining barriers.",
   ["For clients on ART who missed an appointment (<28 days), the chart says 'offer relevant prevention services according to client's preferences' rather than resuming ART/adherence support; probably copied from the HIV-negative pathway.", "Early interrupters are defined by time 'post initiation' and late interrupters by time 'on ART'; the categories overlap for someone who interrupted more than 6 months after starting ART."]),
]
