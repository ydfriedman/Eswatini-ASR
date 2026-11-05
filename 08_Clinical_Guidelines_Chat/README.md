# Clinical Guidelines Chat: Sample Questions

152 sample questions (108 standard + 44 edge cases, all phrased as from a clinician) with reference answers for testing a chat over 11 Eswatini clinical guideline documents (source folder in Google Drive). Every question is in English.

- `sample_questions.xlsx`: formatted spreadsheet. Edge cases are highlighted, and a `Categories` sheet explains each category
- `sample_questions.csv`: one row per question (`id, document, topic, question_type, edge_case_category, expected_behavior, question, reference_answer, source_section, safety_critical, source_chunks, reviewer_note`)
- `sample_questions.jsonl`: the same data, one JSON object per line, for eval scripts

## Coverage

| Document | Questions |
|---|---|
| PrEP Implementation Guidelines (Nov 2025) | 12 |
| National Integrated TB Guidelines (2025) | 12 |
| Amendment to 2022 Integrated HIV Guidelines (2024) | 11 |
| Integrated HIV Management Guidelines (2022) | 11 |
| National STI & Viral Hepatitis Guidelines (draft V2, 2026) | 11 |
| National FP Services Guidelines (3rd ed., 2021) | 11 |
| Consolidated NCD, Injuries & Mental Health Guidelines | 11 |
| Mental Health Desk Guide (2022) | 9 |
| ANC Guidelines | 7 |
| Enhanced Linkages Case Management SOP (2021) | 4 |
| Cross-document (version conflicts, multi-source) | 6 |
| Out of scope (chat should decline) | 3 |

Question types: `factual`, `scenario`, `eligibility`, `dosing`, `numeric`, `conflict`, `cross-document`, `out-of-scope`.

The `conflict` and `cross-document` questions check whether the chat notices when documents disagree. Examples: the HIV self-test consent age (16 in 2022, 12 in 2024), the CrAg CD4 threshold (<100 in 2022, ≤200 in 2024), the 6-month PrEP refill window (3 days or 7 days), and the syphilis retest interval in pregnancy (every 8 weeks or every 3 months). A good answer cites the newer source and flags the difference.

## Known gaps in the source text

The questions use only text that could be extracted. Some parts of the documents were not available:

- **HIV Guidelines 2022**: text available only up to Chapter 4 (around p. 63). Chapters 5–10 (ART, PMTCT, paediatrics, NCDs) are covered only through the guideline's "Summary of Major Changes" section and the 2024 Amendment. (Since the November 2026 update, Q132 also covers infant prophylaxis from Chapter 8, taken from the full chunk set.)
- **NCD/Injuries/Mental Health Guidelines**: the original questions came from Chapters 1–3 only. The November 2026 update added questions from Chapters 6 (injuries/poisoning), 7 (nephrology), 11 (palliation) and 14 (pulmonology), using the full chunk set. Dermatology, GI, neurology, oncology, ophthalmology, podiatry, psychiatry and urology still have no questions.
- **ANC Guidelines**: most tables and charts are images (contact schedule, complication management), so their content is not covered.

Before using this set as an eval, have someone with clinical expertise review the reference answers. A few of them reflect inconsistencies inside the source documents themselves.

## Edge cases (Q109–Q152)

For edge cases, `reference_answer` describes the ideal behaviour rather than a single fact, and `expected_behavior` names it (e.g. `ask-clarifying`, `decline-redirect`, `correct-premise`, `escalate-urgently`, `resist-injection`).

Categories: irrelevant, greeting/meta, ambiguous (needs clarification), typos/shorthand, false premise, boundary values, dose calculations, unsafe orders, time-critical actions, multi-part, cross-corpus aggregation, citation requests, outdated versions, emergencies, harmful requests, prompt injection, opinion questions, other jurisdictions, multi-turn follow-ups, missing content, privacy/PII, and one-word queries. Every question is written as if from a clinician; the chat is for clinicians only.

## November 2026 update: clinician-only, safety-weighted

12 questions were rewritten; the other 140 are unchanged.

| Change | Questions |
|---|---|
| Patient-facing questions removed (the chat is for clinicians only) | Q140 reframed as a clinician question (missed oral PrEP + exposure last night → PEP); Q141 replaced by an unsafe-order check (salmeterol alone for asthma) |
| Boundary-value questions cut from 5 to 2 (kept Q129 viral load = 1000 and Q130 LEN at 28 weeks, where the threshold changes management) | Q128, Q131, Q132 replaced by dose calculations: burns fluids (Parkland), paracetamol overdose (N-acetylcysteine), newborn ARV prophylaxis by birth weight |
| Low-risk questions swapped for safety-critical dosing and emergencies | Q017 (caffeine) → severe pre-eclampsia pre-referral management; Q021, Q022, Q025 (Linkages SOP admin) → hyperkalaemia in AKI, acute severe asthma, palliative morphine conversion; Q035 (vasectomy) → rifampicin and hormonal contraception; Q057 (psychosis durations) → rapid tranquillisation doses |
| Missing-content question fixed | Q150 asked about asthma, which *is* in the guidelines; it now asks about acute gout, which is not (checked across all chunks) |

New columns:

- `safety_critical` (yes/no): a wrong answer could directly harm a patient (wrong drug or dose, missed contraindication, missed or delayed emergency care, fabricated treatment). 98 of 152 are flagged (72 of the 108 standard/out-of-scope questions, 26 of the 44 edge cases). This was a broad first pass; clinicians should confirm it.
- `source_chunks`: the `chunks_v2` chunk ids each new reference answer was written from. Every number in these answers was checked by script against those chunks, apart from values the question asks the model to calculate (e.g. 8,400 mL).
- `reviewer_note`: the points a clinician must check. Q017 (magnesium sulphate dose as printed) and Q131 (the N-acetylcysteine schedule has no stated route).
