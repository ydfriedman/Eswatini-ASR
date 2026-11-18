---
title: Guideline Answer Review
emoji: 🩺
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
short_description: Clinician review of guideline-chat reference answers
---

# Guideline answer review

Clinicians review the 188 benchmark questions for the Eswatini clinical guidelines chat: whether each question reads
naturally, whether the reference answer is right according to the guidelines, and what a correct answer must and must
not include. Each question is saved to a private dataset when you click Save and next (or move to another question).

Settings (Settings → Variables and secrets): `DATASET_REPO` (variable), `HF_TOKEN` (secret, write access to that
dataset), optional `REVIEW_ACCESS_CODE` (secret). See `app.py`.
