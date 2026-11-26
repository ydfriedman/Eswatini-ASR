# Facility Copilot — local guideline chat

## Terminal testing

Set the ML server settings in `guideline_chat/.env` if they differ from the defaults (Ollama at `http://localhost:11434`, model `llama3.1:8b`), then run from the workspace root:

```powershell
python guideline_chat/chat.py
```

No web server is required. Use `/new` and `/quit` in the chat. Evidence shows document titles, years/versions, and PDF pages. Context is kept in memory only. Optional: `--program HIV`, `--question "What are the PrEP follow-up requirements?"` for a single turn, or `--excerpts` to test retrieval without calling the model.

Retrieves from the 3,281 v3 chunks in `../chunks_v3/chunks.jsonl` (see `../chunks_v3/README.md`); parts of one re-extracted table share a `table_id` and are de-duplicated at retrieval. Tables over 6,000 characters are indexed per part (the model receives only the retrieved part), so one huge table cannot fill the model's context. On first launch, the app embeds each chunk's `embed_text` using Ollama and saves normalized vectors plus section-link and citation metadata in `guideline_chat/chunk_embeddings.sqlite`. This initial build sends chunks in batches and may take several minutes. Later starts reuse the index; a changed chunk file or embedding model triggers a complete rebuild, replacing the previous vectors.

From the workspace root:

```powershell
python -m pip install -r guideline_chat/requirements.txt
python guideline_chat/app.py
```

Open http://127.0.0.1:8000. Change the port with `--port 8001`. Rebuild without serving with `--index-only`.

The server console logs Ollama's reported input and output token counts for each chat call; embedding calls show input tokens and `output_tokens=n/a`.
It also logs wall-clock latency in seconds for each Ollama request and each turn, including failures. Turn time covers the shared answer pipeline, not browser or HTTP transport time; Ollama request time includes network overhead.

Features: program filters, cross-program search, source excerpts, PDF page links, Word download, new conversations, and draft inclusion control. No patient files are read. Questions and conversations are not persisted. The app binds only to this computer.

With the ML server model configured (the default), this release is a conversational RAG tool. It rewrites each question using recent conversation context, retrieves local passages, and generates evidence-constrained answers with clickable citations. A routing step runs first: greetings and out-of-scope requests get a fixed reply, and only questions with no searchable clinical subject (a bare "What's the dose?", a single topic word) get one clarifying question without retrieval. A question that names a medicine, condition or programme is always searched: if the guidelines answer differently by group (weight, age, pregnancy, product, population) the answer covers each group and ends with one short question to narrow it, and if the guidelines do not cover it the answer says so instead of asking or inventing a dose. Questions that need arithmetic are not left to the model: it writes `{c1}`-style placeholders that the app computes with a restricted calculator, any written "a x b = N" with a wrong product is rejected and retried, and Parkland burns-fluid questions get a verified schedule (including the time already elapsed) computed by the app and passed to the model. Questions that try to read or override the assistant's instructions are refused without calling the model. Answers are capped at about 120 words and cite sources by id; the reference list (title, section, page) is built by the app from the cited ids. If evidence is insufficient, it states the limitation. `LLM_NUM_PREDICT` (default 1200) caps the answer length; a cut-off answer is retried once with a shorter-answer instruction. Conversations remain in browser memory and reset on refresh, New conversation, or a program/draft-filter change.

Optionally put settings in `guideline_chat/.env`:

```dotenv
LLM_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b
EMBEDDING_MODEL=bge-m3:latest
```

The app loads this file automatically. It is excluded from Git; `.env.example` is the shareable template. Existing process environment settings take precedence. Restart after changing settings. Optional: `LLM_NUM_CTX` (default 16384), `LLM_TIMEOUT` seconds (default 300), and `EMBEDDING_TIMEOUT` seconds (default 300). Retrieval options: `RETRIEVAL_MODE` (`hybrid` default: BM25 keyword + embedding rank fusion; `semantic` for embeddings only), `RETRIEVAL_TOP_K` (initial hits passed to the model, default 6), `AMENDMENT_SCORE_MARGIN` (default 0.08), and `RETRIEVAL_EXPANSION=true` to expand the top hits to section context. Expansion uses up to five hits (configurable from three to five with `RETRIEVAL_EXPANSION_HITS`); sections under 250 estimated tokens expand to their parent section, while groups over 1,200 tokens fall back to the hit and its linked neighbors. Expansion is on by default in the example configuration. The embedding model must be installed on the configured Ollama server, even when generation is disabled for excerpt-only testing.

Start AI mode from the workspace root:

```powershell
powershell -ExecutionPolicy Bypass -File guideline_chat/start.ps1
```

On Linux, run `python guideline_chat/app.py`. Stop any previous server with Ctrl+C before restarting. Generation runs through [Ollama](https://ollama.com)'s `/api/chat` with a JSON schema; `LLM_MODEL` must exist there (`ollama list`) and support structured outputs. Semantic retrieval uses `EMBEDDING_MODEL` through Ollama's `/api/embed`; the default is `bge-m3:latest`. Set `LLM_MODEL=` (empty) to return retrieved excerpts without answer generation; embeddings are still required.

Questions, up to six recent conversation messages, and retrieved passages are sent only to the configured ML server. CMIS files are not read. This phase is for guideline questions, not patient-identifying information. If the model is not configured the app falls back to source excerpts. Network/model errors are shown and are not presented as generated answers. A smaller model is less reliable than a hosted frontier model at following the answer constraints; the citation checks reject malformed answers, so expect occasional retries.

Retrieval uses cosine similarity over locally cached embeddings of `embed_text`, optionally fused with BM25 keyword ranks. Query planning produces concise natural-language variants; each is embedded against the same `bge-m3` model. Results retain document, section heading, chunk type, and page range, with program and draft filters applied before ranking. Every answer block must reference a retrieved source; invalid references and uncited answer blocks are rejected. Citation validation checks source IDs, not medical entailment. Clinical review and representative evaluation are still needed. A full chat turn normally uses two model calls (query planning and answer generation) plus one embedding request per search query; those query vectors are not cached.

API implementation follows [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs).

The catalog and chunk-document mapping are in `app.py`. Publication years do not establish approval or supersession. The STI file is excluded from search by default. HIV and mental-health overlap warnings are shown where relevant; automatic amendment precedence is not implemented. Program leads must confirm authority and review extraction quality before clinical rollout. PDF page positions may differ from printed page numbers. Tables and image algorithms need visual review in the originals.

Next production steps: approved source registry, structured table/algorithm review, retrieval evaluation on the 100-question set, authenticated hosting, and controlled deployment. This local Python backend is not a Sites Worker deployment.
