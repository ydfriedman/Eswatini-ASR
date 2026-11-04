# Question set v2: brief for a new session

Rebuild the 152-question benchmark (`sample_questions.*`) for a **clinician-only** chat. Work from `chunks_v2/chunks.jsonl`, and use `text` as the source for reference answers.

## Changes from v1
- **Drop the patient-facing cases** (Q140 and the other `patient-facing` row). Every question is asked by a clinician. Lay or typo phrasing stays only as a clinician's shorthand.
- **Cut boundary-value questions** from 5 to 1–2. Keep one only where a threshold changes a dose or regimen.
- **Put the weight on safety.** Aim for about 45–50% of questions where a wrong answer could harm a patient:
  - doses by weight or age band (paediatric, neonatal), maximum doses, dosing intervals;
  - dose adjustment in renal or hepatic impairment, pregnancy and breastfeeding;
  - contraindications and drug–drug interactions (e.g. rifampicin with DTG, PrEP with renal function, TB with ART);
  - toxicity monitoring and the thresholds for stopping a drug;
  - emergencies (DKA, hypertensive emergency, poisoning, status epilepticus), and when to refer;
  - "do not do X" rules.
- **Add a `safety_critical` (yes/no) column** and a `key_facts` column (must-have facts, separated by `;`) for every question. Exact numbers go in `key_facts`.
- **Keep, at a smaller share:** ambiguous (needs clarification), false premise, version conflict (2022 vs 2024), out of scope, prompt injection, missing content, and multi-part questions.
- **Cover all 10 guidelines**, including STI/VH and the NCDIMH chapters missing from v1 (dermatology through urology).
- **Hold out about 60 extra questions** as a separate test set (`heldout_questions.*`), using the same method, for milestone runs only.

## Process
1. Draft the questions with references taken straight from the chunk text, citing `chunk_id` and the page.
2. Check every number against the chunk by script.
3. Mark anything uncertain for clinician review.
4. Export to CSV, JSONL and XLSX.
