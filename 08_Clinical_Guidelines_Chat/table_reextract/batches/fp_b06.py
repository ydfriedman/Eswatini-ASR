exec(open('batches/fp_common.py').read())
# Fixes from the user's review of the 50-item validation sample (Nov 2026). Load after fp_b05.
ITEMS = [
 D("fig-counselling-process", 25, "4 Selected Procedures for Providing FP Methods > 4.1 Counselling",
   "Figure 1: Structured counselling process (counselling flipchart tabs: Choosing Method, Dual Protection, Clients with Special Needs, Returning Client, Emergency Contraception, Method Tabs)", ["0030"],
   "Start: Welcome client -> Find out reason for visit. Go to correct tab.\n\n"
   "Tab 'Choosing Method' (for new clients):\n- Ask client: Do you have a method in mind?\n"
   "- If method in mind: Check if it suits needs and situation. Check dual protection needs. -> Method Tabs\n"
   "- If no method in mind: Discuss needs and situation and review method options. Check dual protection needs. -> Method Tabs\n\n"
   "Tab 'Dual Protection' (for clients who need STI protection):\n- Discuss options for dual protection. -> If needed, help client consider risk. Check if chosen option is suitable. -> Method Tabs\n\n"
   "Tab 'Clients with Special Needs':\n- Go to correct page in section: Younger client; Older client; Postpartum/pregnant client; Post-abortion client; Client living with HIV/AIDS; Client who wants to become pregnant\n\n"
   "Tab 'Returning Client':\n- Ask what method client is using: go to method page in Returning Client section.\n"
   "- No problems with method -> Check for new health conditions. Check about need for STI protection. -> Provide method\n"
   "- Problems using method -> Help manage side-effects -> Check for new health conditions. Check about need for STI protection. -> Provide method\n"
   "- Problems using method -> Switch method: go to Choosing Method tab (side) or Method tab (bottom)\n\n"
   "Tab 'Emergency Contraception' (method tab): Client had unprotected sex, needs emergency contraception. (No further steps are drawn under this tab.)\n\n"
   "Method Tabs (some method sections do not have all these pages): Overview & information for choice -> Medical eligibility criteria -> Possible side-effects -> How to use -> When to start -> What to remember -> Provide method",
   flags=("The figure is printed rotated and its bottom edge is cropped in the PDF: a line of small text below the Method Tabs strip is cut off and cannot be read.",)),
 D("fig-iud-insertion", 115, "14 Appendices > 14.5 Appendix 5: Icud Insertion Procedure",
   "14.5 Appendix 5: ICUD insertion procedure (flowchart)", ["0209"],
   "- Counseling: General; Method-specific -> Medical history -> General/ abdominal exam -> Bimanual exam -> Speculum exam\n"
   "- Speculum exam -> If positive (purulent discharge): Treat woman and partner as appropriate -> Schedule follow-up visit for reassessment and possible IUD insertion\n"
   "- Speculum exam -> If negative (no purulent discharge): Cleanse cervix -> Apply tenaculum -> Sound uterus -> Load IUD in sterile package -> Set gauge to sounded depth -> Gently insert IUD -> Post-insertion counseling"),
]
