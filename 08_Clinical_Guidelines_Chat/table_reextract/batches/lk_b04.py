exec(open('batches/lk_common.py').read())
# Linkages SOP tables re-transcribed from the page images (second pass over the tables first rebuilt from the
# old chunks; same table_ids). Everything not given here (replaces_chunks, heading path, context_before, flags) is carried
# over from the item as left by lk_b03, so apply this batch once, after lk_b03.
import json as _j
_prev = {t['table_id']: t for t in _j.load(open('unaids-linkages-sop_tables.json'))['tables']}
def X(tid, header, body, cap=None, flags=(), **kw):
    p = _prev['unaids-linkages-sop-' + tid]
    d = {"table_id": p['table_id'], "page": p['page'], "image_only": False, "heading_path": p['heading_path'], "caption": cap or p['caption'],
         "replaces_chunks": p['replaces_chunks'], "row_header_cols": kw.pop('rhc', p.get('row_header_cols', 1)), "header": p['header'] if header is None else header, "body": p['body'] if body is None else (body(p['body']) if callable(body) else body), "footnotes": kw.pop('footnotes', None) or (p.get('footnotes', []) if body is None or callable(body) else []),
         "source_flags": [f for f in p.get('source_flags', []) if f not in flags] + list(flags), "pages": p.get('pages', [p['page']])}
    d.update({k: v for k, v in p.items() if k not in d})
    d.update(kw); return d
def LL(*xs): return "<br/>".join("- " + x for x in xs)
BR = "<br/>".join
def STEPSEC(b):  # rows whose other cells are empty become section rows
    return [{"section": row[0]['t']} if isinstance(row, list) and all(not c['t'].strip() for c in row[1:]) else row for row in b]
def LASTSPAN(n):  # make the last body row one cell spanning n columns
    return lambda b: b[:-1] + [[C(b[-1][0]['t'], cs=n)]]
def DRUGS(*ds, sep="OR", ncol=6):
    """Drug job-aid rows: each d = (medicine, dose, frequency, duration, max dose, codes[, titration]); alternatives separated by an 'OR' row."""
    out = []
    for i, d in enumerate(ds):
        if i and sep: out.append({"section": sep})
        out.append(r(*d[:ncol]))
        if len(d) > ncol and d[ncol]: out.append([C(d[ncol], cs=ncol)])
    return out
HD = [r("Medicine", "Dose", "Frequency", "Duration", "Max dose", "Codes")]
DRUGNOTE = "Each medicine row is followed by its titration instruction where one is printed; 'OR' marks alternatives (printed in a narrow left column)."
import re as _re
def UNWRAP(b):  # join PDF line-wraps inside cells; keep breaks before bullets
    return [row if isinstance(row, dict) else [dict(c, t=_re.sub(r'<br/>(?![•\-o] )', ' ', c['t'])) for c in row] for row in b]
def REBULLET(b):  # restore line breaks lost before bullets ('... text • Next item')
    return [row if isinstance(row, dict) else [dict(c, t=_re.sub(r'(?<!<br/>)\s+• ', '<br/>• ', c['t'])) for c in row] for row in b]
def H2B(newh, cap=None, **kw):
    """Return kwargs for X(): the old header row was really the first body row; put it back and use newh as the header."""
    return dict(header=newh, body=lambda b: None, cap=cap, **kw)
def HB(tid, newh, fix=None, **kw):
    p = _prev['unaids-linkages-sop-' + tid]
    body = [list(p['header'][0])] + p['body']
    if fix: body = fix(body)
    return X(tid, newh, body, **kw)
def COLJOIN(b):  # one row per table: each column's non-empty cells joined (bullet items that had been paired across columns)
    rows = [r_ for r_ in b if isinstance(r_, list)]
    n = max(len(r_) for r_ in rows)
    return [[C("<br/>".join(r_[i]['t'] for r_ in rows if i < len(r_) and r_[i]['t'].strip())) for i in range(n)]]
ITEMS = [
 HB("tbl-p22-0025", [r("No.", "Principle")], cap="Guiding Principles for Linkage Case Management",
    footnotes=["A numbered list printed in a box; no header row in the source (headings added here)."]),
 HB("tbl-p26-0033", [r("The EC will provide the following")], cap="9.2.1 The EC will provide the following",
    footnotes=["Printed as a column of boxes; no header row in the source (heading added here)."]),
 X("tbl-p27-0038", None, None, footnotes=["The box heading 'Client on arrival at co-located ART clinic' is printed as in 9.3, although this section is about the inpatient department."]),
 X("tbl-p28-0039", [[C("Client referred after initiation", cs=2)], r("On Arrival at clinic", "The health care worker")],
   lambda b: b[1:], cap="9.5 Initiating ART at the community (Annex 1): client referred after initiation", rhc=0),
 X("tbl-p32-0046", [r("HTS Provider", "Linkage's facilitator", "Nurse/Doctor", "Client")],
   [{"section": "Clients initiating ART"},
    r(LL("Verify in CMIS client details and background.", "Assess coping with HIV diagnosis, and explain importance of linkage to ART.", "Document detailed client contact information both cell phone number and physical address in the Chronic Care Files or CMIS.", "Provide motivational counseling and information including the benefits of early ART initiation.",
         "Provide counseling on disclosure and testing of Partner, Family and Associates (PFAs).", "Ask about and list all PFAs that are available and who would benefit from testing (i.e., live within the catchment area of the facility or will visit the area before case closure)", "Offer partner notification services for testing as per HTS guidelines.", "Document the client in the linkage logbook/CMIS.",
         "Introduce clients to the ECs/ MM/ Nurse.", "Follow up with the client's outcome and document ART number in the HTS register and linkages logbook/ CMIS.", "For clients delaying initiation, the HTS provider will initiate escalated referral for higher level intervention.", "Escort client to ART clinic and facilitate registration for ART care"),
      LL("Escort clients to ART clinics and facilitate registration for ART care.", "Provide face-to-face counseling sessions on the benefits of early enrollment in care and ART, disclosure, and testing of PFAs/index testing.", "Conduct ART readiness assessment using the standardized tool and document.", "Screen for NCDs",
         "Provide motivational and informational counseling, including personal testimonials.", "Open chronic care file and document adherence session provided to client assist clients to navigate across services (e.g. triage, clinical consultation, laboratory, etc.).", "Document the assigned case in the linkage's management logbook.", "Assess and resolve real and perceived barriers to care.",
         "Provide counseling on disclosure.", "Facilitate testing of partners, family members, and associates (PFAs).", "Inform clients that there will be on going face to face sessions for the next 6 months.", "Complete appropriate sections of LCM register/ CMIS",
         "Appoint the client in the ART appointment register/ CMIS.", "For clients delaying initiation, the EC/ Mentor Mother/ adherence officer will initiate escalated referral for higher level intervention.", "Give facility contacts to clients so that clients can call if experiencing challenges.", "Document facility's contact details on client health card upon initiation",
         "For children and adolescents, educate caregiver(s) on treatment plan.", "Provide IEC materials to the patient to assist with further understanding.", "Refer to community- facility Linkage section.") + "<br/>For clients returning to care<br/>" + LL("Welcome the client back to care.", "Enhanced adherence counselling"),
      LL("Conduct HIV retesting for verification according to the national guidelines.", "Review for ART initiation barriers (psychosocial /clinical barriers)", "Emphasize the importance of maintaining a healthy lifestyle.", "Explain treatment to patient.",
         "Document client in ART register/enter client in CMIS/APMR.", "Assign and introduce Linkage facilitator for all clients.", "Inform clients that if they experience any side effects, they should report to the facility.", "Screen for NCD",
         "Screen and initiate TPT", "Inform the patient about tracing system.", "Discuss with client on the next appointment as recommended per guidelines."),
      LL("To ensure s/he understands whole process.", "Client should present their concerns, if any (maybe medical or social)", "Take the decision to start treatment.", "Elaborate an adherence plan with the HCW and to identify the best time for taking treatment, reminders, and place to store medication.",
         "Return for follow-up/ management.", "Call the facility if they will not be able to attend the scheduled appointment for rescheduling.", "Contact the health care provider right away if they experience or observe unfamiliar symptoms.", "Identifying a support System.")),
    {"section": "Client delaying ART initiation (for clients delaying ART initiation, the goal is to initiate within 14 days)"},
    r(LL("Verify in CMIS client details and background.", "Document detailed client contact information both cell phone number and detailed physical address in the Chronic Care Files/ CMIS", "Verify contact details provided by client.", "Document the client in the linkage register / CMIS.", "Refer clients delaying ART initiation using facility escalation counseling plan.", "Elicitation of PFA", "Clients refusing to be escorted should be given clear directions and complete the intra facility referral form."),
      LL("Document detailed client contact information both cell phone number and physical address in the Chronic Care Files/ CMIS/LCM register", "Provide motivational counseling and information including the benefits of early ART initiation.", "Prepare client for Pretreatment viral load.", "Document the client in the linkage register/CMIS.", "Screen for NCDs", "Refer clients delaying ART initiation using facility escalation counseling plan.",
         "Refer client to be reviewed by nurse or doctor and provide intensified counselling.", "Appoint client in the appointment register for follow up calls and further counselling sessions.", "For children and adolescents, educate caregiver(s) on treatment plan.", "Inform client of follow up contacts to be conducted by facility"),
      LL("Review and resolve identified ART initiation barriers reported by expert client.", "Emphasize on the benefits of ART and early enrolment to treatment.", "For children and adolescents, inform caregivers on disease progression.", "Discuss and agree with the client t for the next appointment date.", "Adolescent Delaying ART must be referred to peer supporters for further counselling.",
         "Children denied care by parents/guardian, refer client to social worker.", "If client is still hesitant the client must be booked for another session of further counselling", "Refer clients delaying ART initiation using facility escalation counseling plan.", "Screen for NCDs", "Screen and initiate TPT"),
      LL("To ensure s/he understands whole process.", "Client should present their concerns, if any (maybe medical or social)", "Return for follow- up/ management.", "Contact the health care provider right away if they experience or observe unfamiliar symptoms.", "Client should present their concerns, if any (maybe medical or social)", "Take the decision to start treatment."))],
   cap="12.3 Day Zero responsibilities: clients initiating ART and clients delaying ART initiation", rhc=0, pages=[32, 33, 34, 35, 36, 37, 38],
   footnotes=["Two tables printed rotated across pp.17-23 of the SOP, each one row of four role columns that continues over several pages; each column is given here as one list. The 14-day goal for clients delaying initiation is a callout above the second table."]),
 X("tbl-p40-0057", [[C("Linkages Facilitator ( EC/Adherence officer/Counselor)", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")],
   lambda b: b[1:], cap="12.5 During telephone call", rhc=0),
 X("tbl-p42-0062", None, lambda b: [[C("<br/>".join(row[0]['t'] for row in b)), C("<br/>".join(row[1]['t'] for row in b))]], rhc=0,
   cap="12.7 Day 14: first clinic visit (1st ARV refill) – clients who have and have not missed the appointment",
   footnotes=["Two independent lists (the items side by side are not paired)."]),
 X("tbl-p44-0065", None,
   [r(LL("Before the call, check ART barriers from the LCM from the LCM register and CCF.", "Call client: introduce yourself and facility, ascertain if it is the right client.", "Ascertain convenience of having call, if no, find out appropriate time", "Establish rapport.", "Tailor-make conversation based on barriers ascertained.", "Assess if the client is coping with HIV diagnosis.", "Reassure client on available support for treatment and explore readiness for initiation.", "Continue to conduct ART readiness assessment.", "Refer client to be reviewed by nurse or doctor and provide intensified counselling.", "Update contacts for patients both physical and cellphone number.", "Update documentation in the linkages case management register.", "Appoint client in the appointment register for follow up calls and further counselling sessions."),
      LL("Conduct client’s readiness assessment.", "Address client’s immediate concerns and questions", "Review and resolve previously identified barriers.", "Provide the Pre-ART service package for clients delaying ART initiation.", "Discuss and explain HIV disease progression with the client.", "Agree with the client on the next appointment date.", "Clients still refusing ART initiation, should be referred to the next level of escalation counselling according to the facility plan.", "In case of adolescents refer for peer to peer counselling where possible"))],
   cap="12.9 Clients delaying initiation on ART", rhc=0),
 X("tbl-p45-0069", [[C("Linkages Facilitator", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")],
   [r(LL("Introduce yourself and facility, ascertain if it is the right client.", "Ascertain convenience of having call, if no, find out appropriate time", "Assess how client is coping with ART treatment, check if there are any challenges.", "Remind client of the next appointment date.", "Check if clients have questions and give relevant responses.", "Record the call in the call log as needed and update in the chronic care file."),
      LL("Before the call, check ART barriers from the LCM from LCM register and CCF.", "Call client: introduce yourself and facility, ascertain if it is the right client.", "Ascertain convenience of having call, if no, find out appropriate time.", "Tailor-make conversation based on barriers ascertained.", "Assess how the client is coping with HIV diagnosis.", "Reassure client on available sup- port for treatment and explore readiness for initiation.", "Record the call in the call log as needed and update in the chronic care file."))],
   cap="12.11 During telephone call (Day 21-29: third telephonic call)", rhc=0),
 X("tbl-p49-0076", [[C("Linkage Facilitator", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")],
   [r(LL("Assess coping with ART treatment.", "Review disclosure plans and assess progress.", "Troubleshoot immediate concerns regarding disclosure.", "Review testing of plans and schedule for index partner testing", "Provide motivational and informational counseling, including personal testimonials.", "Assess coping and adherence, assess disclosure plans/outcomes, and elicit new index contacts; troubleshoot concerns and barriers to care.") + "<br/>Record the call in the call log as needed and update in the chronic care file.",
      LL("Assess coping with the HIV diagnosis.", "Reassure client on available support for coping with diagnosis and treatment.", "Check if client has been visited by a community health volunteer on behalf of the facility.", "Troubleshoot concerns and barriers to care.", "Provide motivational and informational counseling, including personal testimonials on importance of early ART initiation.") + "<br/>Record the call in the call log as needed and update the chronic care file.")],
   cap="During telephone call (before the Day 60-90 third clinic visit)", rhc=0),
 X("tbl-p53-0084", [[C("Linkage Facilitator", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")],
   [r(LL("Check any pending issues in the client chronic care file", "Check if they have managed to disclose", "Check if their contacts have been tested", "Ask client if they have any challenges with treatment and assist with treatment.", "Inform client about availability of DSD options if their viral load is undetectable", "Remind the client of the next clinical visit."),
      LL("Inform client of the available support should they change their mind", "Check if escalation counselling was done", "Inform client that there is no need to test again, should they decide that they want to be initiated on ART", "Discharge client from the LCM and document outcome"))],
   cap="12.18 Day 150: fifth clinic visit (5th ARV refill)", rhc=0,
   flags=("At the day-150 visit, clients still delaying ART are discharged from linkage case management; the table gives no further follow-up (e.g. community tracing or later re-contact) for people living with HIV who have not started treatment.",)),
 X("tbl-p58-0094", [[C("For clients referred after the first clinical visit", cs=3)], r("Linkage's facilitator (Nurse/Expect Client/ Mentor Mother)", "Doctor/Nurse", "Patient")],
   [r(LL("Conduct ART readiness assessment and highlight identified gaps that must be addressed during next visit", "Assess and troubleshoot barriers to care.", "Assess disclosure and testing of index contacts.", "Follow up on eliciting index contacts", "Provide motivational and informational counseling.", "Update contacts for patients both physical and cellphone number", "Discuss with their client their preferred facility for transfer and agree on a date the patient will visit the preferred facility.",
         "Make a follow up call to the client 3 days prior to the agreed date for visiting the preferred facility to remind client of the appointment.", "Call the preferred facility a day after the agreed date to ensure the client honored the appointment and document outcome in the linkage's logbook and update in the chronic care file.", "Give the client the contact number of the facility they are referred too", "Make follow up call to confirm linkages with the facility and call the client to get feedback"),
      LL("Collect physical history and conduct physical assessment.", "Review pending laboratory results Assess for side effects and adherence.", "Document all findings in the CCF / CMIS.", "Initiate client on ART for client", "Fill out referral form with detailed information and set up an appointment"),
      LL("To ensure s/he understand the process of referral and linkages", "Client should Facility if they will not be able to honor their appointment.", "Client must understand that it is their responsibility to ensure they are linked for treatment", "Inform client that if they are not linked, clients will be referred to community health care worker."))],
   cap="12.23 Responsibility Of Referring Facility (for clients referred after the first clinical visit)", rhc=0, pages=[58, 59],
   footnotes=["Printed rotated over two pages; each column is one list here. 'Client should Facility if...' is as printed (call the facility)."]),
 X("tbl-p64-0103", None, COLJOIN, rhc=0, cap="Responsibilities at community Linkages",
   footnotes=["Printed rotated over two pages; each column is an independent list (items side by side are not paired)."]),
 X("tbl-p67-0107", [[C("Facilitator", cs=2)], r("Clients willing to initiate ART", "Clients not willing to initiate ART")],
   [r(LL("Must be aware of available referral services (both clinical services and community resources)", "Conduct ART readiness assessment and document in the referral form", "Document a detailed referral form which include date client tested and HIV status, regimen client was initiated on or any other services the client was provided. Agree on appointment date and the client preferred facility.", "Call the facility you are referring to make an appointment for a client.", "Escort or meet clients at facilities and assist with treatment navigation services for at least the first facility visit.", "Document referral and transport pink form to the facility to ensure the client is booked.", "Conduct one follow-up face-to-face counseling session or through phone call once the client has been linked to the facility.", "For Community partners implementing Community ART, clients must be initiated before being referred out.", "Discuss with client about importance of index testing and disclosure"),
      LL("Highlight the barriers that cause the client not to initiate", "Emphasize on the benefits of ART and early enrolment to treatment.", "All clients refusing to be initiated on ART must be referred according to the counselling escalation plan.", "Assign and introduce a Linkages facilitator.", "Obtain contacts both cellphone and physical address", "Make follow up calls as per the facility LCM SOP to find out how the client is coping with the diagnosis.", "Inform client of the available support.", "Appoint client in the appointment register for follow up calls and further counselling sessions.", "Client is followed up through community health care workers and outcome must be documented in the call log systems"))],
   cap="Responsibilities for HIV testing and not initiating ART at Community level", rhc=0),
 X("tbl-p69-0110", [r("Linkage facilitator", "Nurse")],
   [{"section": "Clients initiating ART"},
    r(LL("Client is introduced by HTS Counselor to the expert client or outreach/ mobile nurse.", "Assess client readiness for ART.", "Client receives counselling and benefits of early ART.", "Open chronic care file and complete psychosocial information", "Enroll client in the LCM register/CMIS.", "Document next appointment date on appointment register.", "Call client or visit (Expert client, peer, peer navigation to find out how the client is coping with treatment as per LCM SOP", "Assist and support with disclosure.", "Discuss index testing with client"),
      LL("Conduct retesting for verification by the outreach nurse.", "Outreach nurse will assess client readiness for ART Initiation.", "Initiate client on ART", "Assign linkages facilitator", "Inform the client that it is their responsibility to ensure they are linked within the agreed upon time", "Inform client that if they experience any unfamiliar symptoms, they should contact the linkages facilitator", "Document the number for the facility where the client has been referred and the linkages facilitator")),
    {"section": "Clients not initiating ART"},
    r(LL("Assess coping with the HIV diagnosis.", "Review and resolve identified barriers for ART initiation.", "Emphasize on the benefits of early ART enrollment to treatment.", "Reassure client on available support for coping with diagnosis and treatment.", "Provide motivational and informational counseling, including personal testimonials on importance of early ART initiation.", "All clients refusing to be initiated on ART must be referred according to the escalation counselling plan.", "Client is followed up through community health care workers if client has consented, and document outcome in the call log systems.", "Appoint client in the appointment register for follow up calls and further counselling sessions"),
      LL("Review and resolve identified barriers for ART initiation and address client’s immediate concerns and questions.", "Emphasize on the benefits of ART and early enrollment to treatment.", "Discuss and explain HIV disease progression with the client.", "Provide the Pre-ART service package for package for clients delaying ART initiation.", "Assign and introduce a linkages facilitator for all clients.", "Clients still refusing ART initiation, should be referred to the next level of escalation counselling according to the facility plan.", "In case of adolescents refer for peer to peer counselling where possible"))],
   cap="12.30 Responsibilities for HIV testing and initiating ART at Community level", rhc=0,
   footnotes=["The 'Clients not initiating ART' part is printed as a second table on p.55 of the SOP (PDF p.70)."]),
 HB("tbl-p88-0140", [r("Indicator", "Description", "Calculation", "Data Collection tools")],
    cap="13.9 List of LCM Reporting Indicators (continued)", pages=[88, 89, 90],
    footnotes=["Continuation of the indicator table on p.87; printed rotated, without repeating the header row (header added here)."]),
 X("tbl-p73-0118", None, COLJOIN, rhc=0, cap="12.31 Differentiated Service Delivery for Priority Populations Linkages: children, adolescents, key populations and men",
   footnotes=["Printed rotated over pp.58-61 of the SOP; each column is one list here (the page breaks had been split into separate rows)."]),
 X("tbl-p85-0136", None, UNWRAP),
]
