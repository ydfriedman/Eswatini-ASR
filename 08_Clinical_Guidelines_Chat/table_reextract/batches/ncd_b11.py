exec(open('batches/ncd_common.py').read())
N = C("No interaction")
UP_SU = C("↑ potential interaction: may need sulfonylurea dose adjustment")
DN_SU = C("↓ potential interaction: may need sulfonylurea dose adjustment")
ITEMS = [
 T("tbl-antidiabetic-arv-interactions", 62, CH2 + " > Diabetes in Special Populations > Diabetes in HIV > Drug interactions between antidiabetic agents and ARVs",
   "Drug interactions between antidiabetic agents and antiretrovirals (ARVs) (source: University of Liverpool hiv-druginteractions.org)", ["0175", "0176", "0177"],
   [[C("Antidiabetic agent"), C("TDF/TAF"), C("AZT"), C("3TC"), C("FTC"), C("EFV"), C("NVP"), C("DTG"), C("LPV/r"), C("ATV/r"), C("DRV/r")]],
   [[C("Metformin"), N, N, N, N, N, N, C("↑ CAUTION: metformin levels increased (limit metformin to 1,000 mg/day; monitor renal function)"), N, N, N],
    [C("Glibenclamide"), N, N, N, N, DN_SU, DN_SU, N, DN_SU, DN_SU, DN_SU],
    [C("Glipizide"), N, N, N, N, UP_SU, N, N, DN_SU, DN_SU, DN_SU],
    [C("Gliquidone"), N, N, N, N, UP_SU, N, N, DN_SU, DN_SU, DN_SU],
    [C("Gliclazide"), N, N, N, N, UP_SU, N, N, DN_SU, DN_SU, DN_SU],
    [C("Glimepiride"), N, N, N, N, UP_SU, N, N, DN_SU, DN_SU, DN_SU]],
   context_before="Diabetes in HIV: a dose adjustment of metformin should be considered when co-administering DTG with metformin to maintain glycaemic control. Monitor renal function and blood glucose when metformin and DTG are co-administered; patients with moderate renal impairment may be at increased risk of lactic acidosis due to increased metformin concentrations.",
   footnotes=["Key: no interaction. Potential interaction with increased (↑) or decreased (↓) levels of the sulfonylurea, which may require dose adjustment: monitor blood glucose and adjust the sulfonylurea dosage as needed. CAUTION when co-administering metformin with DTG: metformin levels are increased and dose reduction of metformin should be considered. The US prescribing information recommends limiting the total daily dose of metformin to 1,000 mg when co-administered with DTG. Renal monitoring is recommended, as PLHIV with renal impairment are at increased risk of lactic acidosis due to increased metformin levels in the presence of DTG.",
              "*Essential medicines list included atenolol, metoprolol, carvedilol as alternatives (as printed under the table). Refer to National HIV Management Guidelines."],
   source_flags=["Interaction category is shown only by cell colour in the PDF (green = none, purple = potential sulfonylurea interaction, red = caution); written out in each cell.",
                 "'Glibencamide' printed; written Glibenclamide.",
                 "The footnote about atenolol/metoprolol/carvedilol does not relate to antidiabetic drugs; possibly misplaced in the source."]),
]
