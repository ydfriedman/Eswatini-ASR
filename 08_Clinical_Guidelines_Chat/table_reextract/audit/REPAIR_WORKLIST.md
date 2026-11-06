# Table repair worklist (from audit_cell_positions.py + classify_missing.py)

Missing = PDF words inside the ruled table that are not in the table item. "Elsewhere" = the words exist in another chunk (content split away from its table). "Lost" = not found anywhere in the document's chunks.
FP pages carry a hidden acronym-list text layer; runs from it are ignored. Tables without ruled grid lines (101 of 312) cannot be checked this way.

| Doc | Page | Item | Lost words | Words elsewhere | Example |
|---|---|---|---|---|---|
| fp-2021 | 32 | `fp-2021-tbl-p32-0044` | 70 | 11 | 36 pac post / 37 pid pelvic |
| fp-2021 | 38 | `fp-2021-tbl-p38-0058` | 6 | 16 | 46 spr / 47 srh |
| fp-2021 | 56 | `fp-2021-tbl-p56-0099` | 11 | 3 | 51 un world / advantages 52 unfpa united |
| fp-2021 | 116 | `fp-2021-tbl-p116-0210` | 17 | 0 | 38 pnc post / 39 pois |
| hiv-amendment-2024 | 12 | `hiv-amendment-2024-tbl-3-prep-initiation-hivst` | 0 | 28 | at one month then every three months / at one month then every two months |
| hiv-amendment-2024 | 12 | `hiv-amendment-2024-tbl-3-prep-followup-hivst` | 0 | 88 | daily ed or alternating / hiv test |
| hiv-amendment-2024 | 28 | `hiv-amendment-2024-tbl-7-summary-of-changes` | 0 | 18 | low level viraemia vl 50 999 / low level viraemia vl 200 999 copies ml |
| hiv-amendment-2024 | 28 | `hiv-amendment-2024-fig-7.1-vl-thresholds` | 2 | 49 | 200 / 200 |
| hiv-amendment-2024 | 40 | `hiv-amendment-2024-fig-9.4-paeds-art-follow-up` | 3 | 0 | cd 4 vl |
| mental-health-deskguide | 25 | `mental-health-deskguide-tbl-p25-0040` | 0 | 59 | if the patient has excessive / worry occurring more days for at least 6 12 difficult to control the worry plus |
| mental-health-deskguide | 28 | `mental-health-deskguide-tbl-p28-0050` | 0 | 172 | the following are diagnostic criteria a if the patient was exposed to actual or threatened death serious injur |
| mental-health-deskguide | 36 | `mental-health-deskguide-tbl-p36-0068` | 0 | 157 | intense sorrow and emotional pain in response to the death preoccupation with the deceased preoccupation with  |
| mental-health-deskguide | 40 | `mental-health-deskguide-tbl-p40-0082` | 2 | 30 | grandiosity distractibility |
| mental-health-deskguide | 45 | `mental-health-deskguide-tbl-p45-0091` | 4 | 38 | 6 / 81 occupational therapy |
| mental-health-deskguide | 49 | `mental-health-deskguide-tbl-p49-0105` | 0 | 92 | in attention and awareness a disturbance develops over a short period of time and fluctuates in severity durin |
| mental-health-deskguide | 53 | `mental-health-deskguide-tbl-p53-0114` | 0 | 25 | incoordination unsteady gait nystagmus / in attention or memory stupor or coma |
| mental-health-deskguide | 87 | `mental-health-deskguide-tbl-p87-0210` | 5 | 39 | donepezil hydrochloride po / 5 |
| mental-health-deskguide | 87 | `mental-health-deskguide-tbl-p87-0212` | 8 | 35 | 20 / 50 |
| mental-health-deskguide | 87 | `mental-health-deskguide-tbl-p87-0214` | 5 | 32 | 60 / 10 |
| mental-health-deskguide | 88 | `mental-health-deskguide-tbl-p88-0216` | 1 | 34 | 25 |
| mental-health-deskguide | 88 | `mental-health-deskguide-tbl-p88-0218` | 3 | 49 | 3 / 3 |
| prep-2025 | 19 | `prep-2025-tbl-ring-drug-interactions` | 3 | 0 | showed to be |
| prep-2025 | 39 | `prep-2025-tbl-product-eligibility` | 5 | 0 | 12 / no contra |
| prep-2025 | 41 | `prep-2025-tbl-community-initiation-referral` | 6 | 2 | the following information / scheduled appointment the |
| prep-2025 | 46 | `prep-2025-tbl-first-followup-timing` | 5 | 0 | f u visit / f u |
| prep-2025 | 48 | `prep-2025-tbl-adherence-definition` | 8 | 20 | month ago / month ago |
| prep-2025 | 50 | `prep-2025-tbl-creatinine-monitoring` | 12 | 25 | age 30 years / 30 or if |
| prep-2025 | 53 | `prep-2025-tbl-restarting-prep` | 7 | 6 | before sexual encounter / as described |
| prep-2025 | 59 | `prep-2025-tbl-data-collection-tools` | 11 | 7 | not having / the register should be used |
| prep-2025 | 64 | `prep-2025-tbl-annex2-cab-la-missed` | 6 | 105 | later as a / later as a |
| prep-2025 | 67 | `prep-2025-tbl-annex3-len-missed` | 10 | 115 | for 26 later as a / for 26 later as a |
| tb-2025 | 23 | `tb-2025-tbl-p23-0021` | 0 | 42 | using a stamp strategy / giving a stamped slip to the client and checking by attending clinicians if screening |
| tb-2025 | 77 | `tb-2025-fig-plhiv-evaluation` | 4 | 2 | both lam / xpert lam |
| tb-2025 | 80 | `tb-2025-tbl-p80-0181` | 0 | 44 | if the aspirate is dry then an ln biopsy / taken sending the material for histological examination |
| tb-2025 | 112 | `tb-2025-tbl-p112-0274` | 0 | 49 | vaccination history covid 19 influenza pneumococcal comorbidity hiv diabetes / hazardous exposure smoking biom |
| tb-2025 | 134 | `tb-2025-tbl-p134-0333` | 50 | 102 | 2 mlb / 1 mlb |
| tb-2025 | 142 | `tb-2025-tbl-p142-0356` | 0 | 80 | at any age collection of sputa after the child inhales 3 5 hypertonic saline induction improves the yield of s |
| tb-2025 | 144 | `tb-2025-tbl-p144-0360` | 1 | 18 | 90 |
| tb-2025 | 148 | `tb-2025-tbl-p148-0368` | 16 | 0 | 3 mth / 3 mth 16 yrs |
| tb-2025 | 150 | `tb-2025-tbl-p150-0376` | 3 | 0 | wt bands kg |
| tb-2025 | 151 | `tb-2025-tbl-p151-0378` | 3 | 0 | wt bands kg |
| tb-2025 | 184 | `tb-2025-tbl-p184-0463` | 12 | 22 | suggested drugs to manage the adr / nausea vomiting abdominal upset |
| tb-2025 | 201 | `tb-2025-tbl-p201-0516` | 7 | 14 | 10 kg / 10 |
| tb-2025 | 203 | `tb-2025-tbl-p203-0520` | 1 | 17 | 5 |
| tb-2025 | 216 | `tb-2025-tbl-p216-0559` | 10 | 51 | lfx 100 d t / lfx 100 dispersible tablet d t |
| tb-2025 | 217 | `tb-2025-tbl-tpt-plhiv` | 60 | 4 | population group / plus rifapentine for 3 months rifapentine 300 mg isoniazid 300 mg per tablet 12 doses 3 tab |
| tb-2025 | 224 | `tb-2025-tbl-p224-0582` | 12 | 12 | 10 / 84 |
| tb-2025 | 271 | `tb-2025-tbl-p271-0708` | 5 | 0 | sisongaid ta imb / k u |
| unaids-linkages-sop | 27 | `unaids-linkages-sop-tbl-p27-0036` | 0 | 34 | shall initiate client on art on discharge the client shall be navigated to the art department the inpatient de |
| unaids-linkages-sop | 27 | `unaids-linkages-sop-tbl-p27-0038` | 0 | 33 | is fast tracked into the consultation room for art initiation / ascertain if contacts have been elicited provi |

50 items.

## Result of the repair pass

Each item was checked against the page image or the PDF grid. **Repaired** (batches `tb_b09.py`, `mh_b04.py`, `fp_b03.py`):

| Item | Problem | Fix |
|---|---|---|
| TB Table 1 (p.23) | 3 of 4 screening-strategy bullets in a separate text chunk | Cell completed; text chunk absorbed |
| TB Table 2 (p.28) | Year/target header rows dropped: percentages had no years | Re-done from image (2020/2025 milestones, 2030 SDG, 2035 End TB) |
| TB Table 11 (p.80) | Second diagnostic bullet of the LN, pleural and TBM rows in a text chunk | Cells completed from the PDF grid |
| TB Tables 20/21/22 (pp.112-115) | Three tables fused into one item; Table 20 rows shifted and half its cells in a text chunk | Split into three items; Table 20 re-done from images |
| TB Table 32 (p.142) | Sputum-induction cell empty (content in a text chunk) | Cell filled |
| TB Table 34 (p.148) | Treatment algorithm flattened into a 9-column grid | Written out as a decision tree |
| TB 'Other toxicities' (p.184) | First two rows (nausea/vomiting, heartburn) dropped as a header | Rows restored with a proper header |
| MH Tables 8/9 (pp.36-37) | Fused; Table 8 signs and management in a text chunk | Split; both re-done from images |
| MH Tables 13/14 (pp.45-48) | Table 13 first row cut after one bullet, its other rows filed under Table 14; Table 14 step cells cut after the first line (content lost) | Both re-done from images |
| MH Table 17 cont. (pp.53-56) | Intoxication row symptoms and whole management cell in a text chunk | Re-done from images; thiamine flag confirmed (intoxication only) |
| FP Appendix 6 (p.116) | Decorative icon labels ('Condom / IUD ...') appended to the ECP cell and as extra rows | Removed |

**No change needed** (audit noise): neighbouring tables on the same page (HIV Amendment p.12 and p.28 pairs, MH classification/stepwise pairs pp.25, 28, 40, 49, Linkages p.27, TB Table 61/62), hand-transcribed tables reworded on purpose (TB Tables 31, 50, 51, 55-58, PrEP tables, MH job aids pp.85-88), FP overprinted abbreviation list, rotated pages (TB Tables 31, 78), and HIV Figure 9.4.

Second check added: `audit/lost_phrases.py` compares each rebuilt item with the old chunks it replaced (4-word phrases found nowhere in the new chunks). It caught TB Table 2 and the p.184 table, which the PDF-grid audit could not see. Root cause of both: the rebuild treated an old chunk's first markdown row as a header and dropped it when it carried content.
