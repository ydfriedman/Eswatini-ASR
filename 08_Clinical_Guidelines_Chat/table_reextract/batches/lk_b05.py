exec(open('batches/lk_common.py').read())
# Fixes from the user's review of the 50-item validation sample (Nov 2026). Load after lk_b04.
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-lcm-timeline", 21, "5 Linkage to Treatment and Care > 5.4 Summary of Linkage case management services",
   "5.4 Summary of Linkage case management services: timeline of clinic visits and telephone calls (Day 0 to Day 180)", ["0023"],
   [r("Day", "Contact", "Purpose")],
   [r("Day Zero", "Clinic visit", "Diagnosis & ART Initiation; LCM Enrolment"),
    r("Day 3-5", "1st Call", "Explore challenges in regard to treatment"),
    r("Day 10-12", "2nd Call", "Remind about next appointment date"),
    r("Day 14", "First Clinic/ART Refill", "Follow up on index testing and assess barriers"),
    r("Day 21-29", "3rd Call", "Explore challenges in regard to treatment & remind about next appointment"),
    r("Day 30-45", "Second Clinic/ART refill", "Follow up on Index testing and assess barriers"),
    r("Day 44-60", "4th Call", "Remind about next appointment date"),
    r("Day 60-90", "Third Clinic/ART Refill", "Follow up on index testing and assess barriers"),
    r("Day 120-125", "5th Call", "Explore challenges in regard to treatment"),
    r("Day 150", "Fourth Clinic/ART refill", "Continue index testing. Prepare Client for recharge, inform about ART available DSD options"),
    r("Day 170-175", "6th Call", "Remind about next appointment date"),
    r("Day 180", "Fifth Clinic/ART refill", "Refill outstanding/pending issues. Discharge client. Refer to preferred DSD model")],
   footnotes=["Printed as a timeline with clinic visits above the arrow and telephone calls below; listed here in day order. 'Follow upon' is printed for 'follow up on'."],
   source_flags=["The timeline calls Day 150 the 'Fourth' and Day 180 the 'Fifth' clinic visit, but sections 12.18 and 12.20 call them the fifth (5th ARV refill) and sixth (6th ARV refill) visits."]),
]
