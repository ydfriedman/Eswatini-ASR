# Suggested app.py / .env changes (not applied)

Line numbers refer to the app.py version reviewed. Each change is independent; 1-3 matter most.

## 1. Replace the appended "Application response contract" with a short one
In `guideline_rag_system_prompt()`, the ~600-word contract appended after the prompt repeats and partly contradicts
the prompt. With prompt v2, keep only the format and calculation rules:

```python
    return prompt + '''

## Response format (required)
Return JSON with "kind", "blocks" and "calculations".
- kind: "answer" (blocks of type guideline_claim only; do not add a clarification block),
  "insufficient_evidence" (evidence_gap blocks, no clinical advice), or "clarification_needed" (one clarification block).
- Each guideline_claim block cites 1-3 source ids in "citations" (integers from valid_citation_ids). Do not write
  document names, page numbers or "see Table X" in the text; give the content itself.
- At most 5 blocks and about 160 words. Quote a table row only if it decides the answer, under 25 words.
- Never do arithmetic: write each calculated number as a placeholder like {c1} and list it in "calculations" as
  {"id": "c1", "expression": "4*30*70"}. Use an empty list when nothing is calculated.
'''
```

## 2. Generation settings in `llm_json()` (repeated lines)
Greedy decoding (temperature 0) plus forced JSON makes 8B models prone to loops. A little randomness with a fixed
seed keeps answers repeatable:

```python
'options': {'temperature': 0.2, 'seed': 42, 'top_p': 0.9,
            'repeat_penalty': 1.1, 'repeat_last_n': 128,
            'num_predict': int(os.environ.get('LLM_NUM_PREDICT', '1200')),
            'num_ctx': int(os.environ.get('LLM_NUM_CTX', '16384'))}
```

And reject answers that loop or talk about their sources, so the existing retry loop (it already passes the error
back to the model) asks again. Add both checks at the end of `validate_answer()`, after the `for block in blocks:` loop;
`re` is already imported:

```python
    # Reject answers that repeat themselves (a sign of a generation loop).
    sentences = [re.sub(r'\W+', ' ', s).strip().lower()
                 for b in blocks for s in re.split(r'(?<=[.;!?])\s+', b['text'])]
    sentences = [s for s in sentences if len(s.split()) >= 6]
    if len(sentences) != len(set(sentences)):
        raise ValueError('The answer repeated the same sentence. Write each point once.')
    # Reject answers that name their sources in the text; the app builds the reference list from the citations.
    for block in blocks:
        match = _SOURCE_TALK.search(block['text'])
        if match:
            raise ValueError(f'The answer text refers to its sources ("{match.group(0)}"). Give the content only; '
                             'sources go in "citations", and the app adds the reference list.')
```

with this pattern defined once, just above `def validate_answer(`:

```python
# Source talk the answer text must not contain ("as per Table 2 in NCDIMH", "according to", "source 1 says",
# "this source does not apply"). "the source of infection" stays allowed.
# "2024 Amendment" stays allowed: the prompt's precedence rule asks the model to say the Amendment changed something.
_SOURCE_TALK = re.compile(
    r'\baccording to\b'
    r'|\b(?:table|figure|fig\.|chart|annex|appendix|section|page|p\.)\s*\d'
    r'|\b(?:source|excerpt|passage|document)s?\s*\[?\d'
    r'|\b(?:this|that|these|those|the|first|second|third|other|one) (?:source|excerpt|passage|document)s?\b(?!\s+of\b)'
    r'|\bNCDIMH\b', re.I)
```

Optional: the retry message (`request['previous_answer_error'] = f'{exc} Fix this. Citations must be integers ...'`)
adds a citation reminder to every error; `f'{exc} Fix this in the new answer.'` fits all of them.

### Strip clarification blocks from answers
llama3.1:8b ended every answer with a clarifying question (e.g. "Is the woman living with HIV?"), even when the
question stated it, despite a prompt rule and example changes. The prompt no longer asks for one; this removes any the
model still adds. In the retry loop in `ai_answer()`, right after `apply_calculations(result, blocks)`:

```python
            if result['kind'] == 'answer':
                blocks = [b for b in blocks if b.get('type', 'guideline_claim') != 'clarification'] or blocks
```

Everything after the loop (reference list, message, returned blocks) uses `blocks`. Questions with no clinical subject
still get a clarifying question from the classify step (route "clarify"), which this does not touch.

## 3. Detect context overflow
When the prompt exceeds `num_ctx`, Ollama drops the start of it, which is the system prompt. Log the real size in
`llm_json()` after the response is read:

```python
    used = data.get('prompt_eval_count')
    if used and used > 0.9 * int(os.environ.get('LLM_NUM_CTX', '16384')):
        print(f'WARNING: prompt used {used} tokens, near the context limit', file=sys.stderr)   # needs import sys
```

If warnings appear: lower RETRIEVAL_TOP_K, send fewer history messages (e.g. the last 6 instead of 16), or cap the
total source text in `ai_answer()`.

## 4. Same settings in terminal and web
`.env` does not set RETRIEVAL_TOP_K, so the terminal (chat.py) sends 8 passages and the web app sends 5. Pin them:

```
RETRIEVAL_TOP_K=6
LLM_NUM_CTX=16384
LLM_NUM_PREDICT=1200
```

Try 5-6 first: fewer, better passages help an 8B model synthesize, and expansion adds the surrounding section anyway.

## 5. STI 2026 draft flag
`CATALOG` marks the STI/VH 2026 document `draft=False`, so the "approval status unconfirmed" notice never shows and
`--exclude-drafts` does nothing. If it is still unapproved, set the last field to `True`.

## 6. Smaller items
- History: up to 16 messages of 8,000 characters each are sent to both model calls. Sending the last 6 is usually enough.
- Search caps (3 chunks per document, 2 per page before expansion) can cut useful chunks when one guideline holds the
  whole answer. Worth testing 4-5 per document.
- Short follow-ups (12 words or fewer) also search the previous question; this can pull an old topic into a new short
  question.

## 7. Only add 2024 Amendment passages that are relevant
`ai_answer()` runs an extra Amendment search whenever any HIV 2022 passage is retrieved (around line 532) and adds the
top 2 Amendment hits per query with no relevance check. For "Who should be screened for cervical cancer?" (qwen2.5:14b)
two of the five source slots went to Amendment HIV-testing passages, and the NCDIMH summary table (stop rule, HPV
intervals) was not retrieved. Keep the Amendment search, but only add hits whose cosine similarity is close to the
best hit of the main search:

```python
    # Retrieve topic-relevant amendment passages whenever the HIV base is retrieved.
    if any(item['source']['document']['id'] == '0' for item in fused.values()):
        best = max((item['source'].get('score') or 0) for item in fused.values())
        margin = float(os.environ.get('AMENDMENT_SCORE_MARGIN', '0.08'))
        for query in queries[:3]:
            amendment_results = search(query[:300], 'HIV', drafts, doc_ids=['1'])
            # Expanded context has no score; it is only used if its own hit is kept, so it can stay.
            relevant = [s for s in amendment_results if s.get('score') is None or s['score'] >= best - margin]
            add_ranked(relevant, only_doc_id='1', limit=2)
```

The 0.08 margin is a starting guess: bge-m3 similarities depend on the corpus. To tune it, print `best` and each
Amendment hit's score for a few questions where the Amendment matters (HIV self-test consent age, CrAg threshold,
viral load thresholds) and a few where it does not (cervical screening), and pick a margin that keeps the first and
drops the second.
