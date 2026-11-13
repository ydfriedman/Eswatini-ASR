# Suggested app.py / .env changes (not applied)

Line numbers refer to the app.py version reviewed. Each change is independent; 1-3 matter most.

## 1. Replace the appended "Application response contract" with a short one
In `guideline_rag_system_prompt()`, the ~600-word contract appended after the prompt repeats and partly contradicts
the prompt. With prompt v2, keep only the format and calculation rules:

```python
    return prompt + '''

## Response format (required)
Return JSON with "kind", "blocks" and "calculations".
- kind: "answer" (blocks of type guideline_claim, optionally ending with one clarification block),
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

And reject looping answers so the existing retry loop handles them (add to `validate_answer()`):

```python
    sentences = [s.strip().lower() for b in blocks for s in re.split(r'(?<=[.;!?])\s+', b['text']) if len(s.split()) >= 6]
    if len(sentences) != len(set(sentences)):
        raise ValueError('The answer repeats a sentence. Write each point once.')
```

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
