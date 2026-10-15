# Clinical Guidelines Chat: Sample Questions

152 sample questions (108 standard + 44 edge cases) with reference answers for testing a chat over 11 Eswatini clinical guideline documents (source folder in Google Drive). Every question is in English.

- `sample_questions.xlsx`: formatted spreadsheet. Edge cases are highlighted, and a `Categories` sheet explains each category
- `sample_questions.csv`: one row per question (`id, document, topic, question_type, edge_case_category, expected_behavior, question, reference_answer, source_section`)
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
| Mental Health Desk Guide (2022) | 9 |
| Consolidated NCD, Injuries & Mental Health Guidelines | 8 |
| ANC Guidelines | 7 |
| Enhanced Linkages Case Management SOP (2021) | 7 |
| Cross-document (version conflicts, multi-source) | 6 |
| Out of scope (chat should decline) | 3 |

Question types: `factual`, `scenario`, `eligibility`, `dosing`, `numeric`, `conflict`, `cross-document`, `out-of-scope`.

The `conflict` and `cross-document` questions check whether the chat notices when documents disagree. Examples: the HIV self-test consent age (16 in 2022, 12 in 2024), the CrAg CD4 threshold (<100 in 2022, ≤200 in 2024), the 6-month PrEP refill window (3 days or 7 days), and the syphilis retest interval in pregnancy (every 8 weeks or every 3 months). A good answer cites the newer source and flags the difference.

## Known gaps in the source text

The questions use only text that could be extracted. Some parts of the documents were not available:

- **HIV Guidelines 2022**: text available only up to Chapter 4 (around p. 63). Chapters 5–10 (ART, PMTCT, paediatrics, NCDs) are covered only through the guideline's "Summary of Major Changes" section and the 2024 Amendment.
- **NCD/Injuries/Mental Health Guidelines**: Chapters 1–2 and the start of Chapter 3 only. Chapters 4–15 (dermatology, GI, injuries, nephrology, neurology, oncology, ophthalmology, palliation, podiatry, psychiatry, pulmonology, urology) have no questions.
- **ANC Guidelines**: most tables and charts are images (contact schedule, complication management), so their content is not covered.

Before using this set as an eval, have someone with clinical expertise review the reference answers. A few of them reflect inconsistencies inside the source documents themselves.

## Edge cases (Q109–Q152)

For edge cases, `reference_answer` describes the ideal behaviour rather than a single fact, and `expected_behavior` names it (e.g. `ask-clarifying`, `decline-redirect`, `correct-premise`, `escalate-urgently`, `resist-injection`).

Categories: irrelevant, greeting/meta, ambiguous (needs clarification), typos/lay language, false premise, boundary values, multi-part, cross-corpus aggregation, citation requests, outdated versions, emergencies, patient-facing questions, harmful requests, prompt injection, opinion questions, other jurisdictions, multi-turn follow-ups, missing content, privacy/PII, and one-word queries.
