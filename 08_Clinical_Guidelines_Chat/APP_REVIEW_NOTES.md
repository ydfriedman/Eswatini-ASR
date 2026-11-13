# Guideline chat app: review notes (paused, nothing patched yet)

Context: `guideline_chat/app.py` + `chat.py` were shared for review (not in this repo). Server: AWS g4dn.2xlarge
(1x NVIDIA T4, 16 GB VRAM; 8 vCPU; 32 GB RAM). Ollama with llama3.1:8b (answers) and bge-m3 (embeddings).

## Current settings (from app.py and .env.example)
- llm_json(): temperature 0, num_ctx 16384 (LLM_NUM_CTX), num_predict 1200 (LLM_NUM_PREDICT), JSON schema in `format`.
- RETRIEVAL_TOP_K unset in .env: terminal chat uses 8 (chat.py), web/EMR uses 5 (app default). Expansion on.
- System prompt = guideline_rag_system_prompt.md (between START/END markers) + ~600-word "Application response contract".
- STI 2026 draft has draft=False in CATALOG, so the draft notice never shows and --exclude-drafts does nothing.

## Bugs reported by the user
1. Answers summarize source by source ("this source says..., that source says...") instead of one synthesized answer.
2. Cervical cancer screening: right source retrieved (chunks are clean: NCDIMH pp.251-253, HIV 2022 p257) but ignored.
3. The same line repeated over and over.

## Proposed changes (agreed in principle, not applied)
1. Log `prompt_eval_count` in llm_json() to detect context overflow (Ollama drops the start of the prompt, i.e. the
   system prompt, when over num_ctx).
2. Repetition: temperature 0.2 + fixed seed + top_p 0.9, repeat_penalty 1.1, repeat_last_n 128; plus a code check in
   validate_answer() that rejects answers with repeated sentences (retry loop already exists).
3. Prompt: shorten the .md + contract; add "organize by the parts of the answer, not by source; merge and cite all ids;
   never write 'source X says'"; add one short example of a merged, cited answer near the end.
4. Pin RETRIEVAL_TOP_K / LLM_NUM_CTX / LLM_NUM_PREDICT in .env so terminal and web behave the same; try top-k 4-5.
5. Cap history and total source text in code; consider loosening the per-doc 3 / per-page 2 caps; the ~160-word cap
   may drop groups in multi-population answers.
6. Set the STI draft flag if it should be treated as unconfirmed.

## Model options on a T4 (16 GB)
- Fits: Qwen2.5 7B / Qwen3 8B (drop-in, better at JSON + synthesis), Gemma 2 9B, Qwen2.5 14B / Qwen3 14B at Q4_K_M
  (~9 GB weights + KV cache at 16k + bge-m3 ~1.2 GB; tight but fits). Does not fit: 27B+ models.
- Test with `ollama pull <model>`, set LLM_MODEL, rerun the problem questions; watch `ollama ps` for GPU/CPU split.

## Waiting on from the user
- guideline_rag_system_prompt.md; the failing questions with `--sources` output.
