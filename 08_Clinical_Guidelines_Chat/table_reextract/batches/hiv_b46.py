exec(open("batches/hiv_common.py").read())
# HIV 2022 part 5, pp.290-291 (Annex 11.17 Paediatric ARV dosing card). Read from 160 dpi renders; spans of the 'Not recommended'
# cells set from the cell borders.
AN = "Chapter 11: Annexes"
NR = "Not recommended"
def NRs(n): return C(NR, cs=n)
W = ["3 - 5.9", "6 - 9.9", "10 - 13.9", "14 - 19.9", "20 - 24.9", "25-29.9", "30-39.9", ">40"]
ITEMS = [
 T("tbl-11.17-paediatric-arv-dosing", 290, AN + " > 11.17 Paediatric ARV Dosing Card", "Annex 11.17 Paediatric ARV Dosing Card", ["0781", "0782", "0783", "0784"],
   [[C("Paediatric ARV Formulation", rs=2), C("Weight in kg", cs=8)], r(*W)],
   [r("ABC/3TC 120mg/60mg Tablet (dispersible)", "1 OD", "1.5 OD", "2 OD", "2.5 OD", "3 OD", "", "", ""),
    [C("ABC/3TC 600mg/300mg Tablet (Adult)"), NRs(5), C("1 OD"), C("1 OD"), C("1 OD")],
    r("AZT/3TC 60mg/30mg Tablet (dispersible)", "1 BD", "1.5 BD", "2 BD", "2.5 BD", "3 BD", "", "", ""),
    [C("AZT/3TC 300mg/150mg Tablet (Adult)"), NRs(5), C("1 BD"), C("1 BD"), C("1 BD")],
    [C("DTG 10mg Tablet (scored/dispersible)"), C("0.5 OD"), C("1.5 OD"), C("2 OD"), C("2.5 OD"), C("Change to Adult DTG 50mg tab OD", cs=4)],
    [C("DTG 50mg Tablet (Adult)"), NRs(4), C("1 OD"), C("1 OD"), C("1 OD"), C("1 OD")],
    [C("TDF+3TC+DTG 300mg/300mg/50mg TLD Tablet (Adult)"), NRs(6), C("1 OD"), C("1 OD")],
    [C("LPV/r 100mg/25mg Tablet"), NRs(3), C("2 BD"), C("2 BD"), C("3 BD"), C("3 BD"), C("")],
    [C("LPV/r 200mg/50mg Tablet (Adult)"), NRs(4), C("1 BD"), C("2 AM, 1 PM"), C("2 AM, 1 PM"), C("2 BD")],
    [C("ATV/r 300mg/100 mg Tablet (Adult)"), NRs(7), C("1 OD")],
    [C("TDF+3TC+EFV 300mg/300mg/400mg Tablet (Adult)"), NRs(7), C("1 OD")],
    {"section": "†Recommended DRV and ritonavir Dosing for PI Naïve Paediatric Patients ≥3 yrs & 10 kg In Need of 2nd Line"},
    [C("†DRV 75 mg Tablet (must add RTV)"), NRs(3), C("8 OD"), C("8 OD"), C("8 OD"), C("9 OD"), C("")],
    [C("†DRV 150 mg Tablet (must add RTV)"), NRs(3), C("4 OD"), C("4 OD"), C("4 OD"), C(""), C("")],
    [C("†DRV 600 mg Tablet (must add RTV)"), NRs(3), C("1 OD"), C("1 OD"), C("1 OD"), C("675 mg OD (600mg tab +75mg tab)"), C("")],
    [C("†DRV/r 400/50 mg Tablet"), NRs(7), C("2 OD")],
    {"section": "Boosting RTV for children on DRV for 2nd Line"},
    [C("Ritonavir 25mg Tablet"), NRs(3), C("4 OD"), C("4 OD"), C("4 OD"), C("4 OD"), C("4 OD")],
    [C("Ritonavir 100mg Tablet (Adult)"), NRs(3), C("1 OD"), C("1 OD"), C("1 OD"), C("1 OD"), C("1 OD")],
    {"section": "Super boosting RTV for children on Rifampicin-containing TB Treatment"},
    r("Ritonavir (RTV) 80mg/ml Suspension", "0.8ml BD", "1.2ml BD", "1.5ml BD", "2ml BD", "2.3ml BD", "", "", ""),
    [C("Ritonavir 100mg Tablet (Adult)"), NRs(2), C("1 BD"), C("1 AM, 2 PM"), C("1 AM, 2 PM"), C("2 BD"), C("2 BD"), C("3 BD")]],
   pages=[290, 291],
   context_before="Any third line client with PI Resistance clinicians must consult with the National 3rd Line Committee for updated dosing and administrative guidance for 3rd line treatment options. (Printed twice above the card.)",
   footnotes=["† DRV must be given with ritonavir (see chart above). DRV/r CANNOT be co-administered with rifampicin containing TB treatment. DRV should be used with caution in patients with known sulphonamide allergies.",
              "DRV/r can only be used in 2nd line in the following situations: children ≥3 years and ≥10 kg; PI naïve client; has INSTI resistance confirmed by genotype. (Any patient with PI exposure clinicians must consult National 3rd Line Committee prior to DRV use.)",
              "OD = once daily; BD = twice daily. Rows are colour-banded by drug class in the source (NRTIs green, DTG yellow, PIs/EFV pink, DRV blue, ritonavir purple). Blank cells are blank in the source."],
   source_flags=["Superseded by the 2024 Amendment: the updated paediatric dosing chart adds paediatric ABC/3TC/DTG 60/30/5 mg (pALD) for 6-24.9 kg (Amendment 9.2, Annex 11.17).",
                 "Annex 11.17 heads the DRV section '≥3 yrs & 10 kg' but marks DRV 'not recommended' below 14 kg; the LPV/r 100/25 mg row is blank for >40 kg."]),
]
