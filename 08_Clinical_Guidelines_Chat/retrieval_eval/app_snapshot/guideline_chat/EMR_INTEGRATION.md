# Native EMR chat component

`static/copilot-component.js` registers a framework-independent Web Component. It uses Shadow DOM to isolate styles and renders directly inside the EMR, without an iframe. It can live in a side panel, drawer or dedicated tab.

```html
<script src="/copilot/copilot-component.js"></script>
<facility-copilot api-base="/copilot" program="HIV" style="height:650px"></facility-copilot>
```

Configure the EMR server/reverse proxy to forward `/copilot/*` to the guideline service, stripping `/copilot` from the upstream path. Include `/api/library`, `/api/chat`, `/documents/{id}`, and `/copilot-component.js`. Keeping this route on the EMR's origin avoids CORS and shares the EMR authentication boundary. The model endpoint (`LLM_BASE_URL`) belongs in the guideline service's `.env`, never in EMR JavaScript. Load the component script once per page. Native-framework wrappers may mount this custom element; no framework dependencies are required.

The component's `program` attribute selects the initial program. Users may change the program and reset the chat. History lives only in component memory. A selected program is a retrieval filter, not patient context. The component deliberately does not read patient charts or accept EMR identifiers. Before adding patient-aware functionality, define the allowed context and implement server-side access checks.

The service provides `POST /api/chat` with `{question, program, include_drafts, history}`. History contains up to sixteen `{role: "user" | "assistant", content}` messages. AI responses include `kind`, `message`, `blocks: [{text, citations: [sourceNumber]}]`, `sources`, and `notices`. Citations are one-based positions in that response's sources array. Sources contain local relative URLs, section headings, and page metadata. Retrieval embeds the query using Ollama and compares it with vectors built from `chunks.jsonl`; the vector index is local to the guideline service. The current response flow returns an answer or evidence gap with references and does not ask clarifying or suggested follow-up questions. The service also supports excerpt-only responses when generation is disabled, but still requires the embedding service.

The current Python service is a local development server, not an authenticated production deployment. For production, the EMR gateway must authenticate and authorize all service routes, including source downloads, and keep the upstream service inaccessible to users directly. Add HTTPS, request/concurrency limits, audit metadata without raw chat content, session policy, and clinical acceptance testing before facility rollout. The service does not validate EMR session tokens itself. Do not expose this prototype directly on a public network.

Restart the local service and visit http://127.0.0.1:8000/emr-demo to try the component in a demonstration EMR shell. This demonstrates the integration contract; wiring into the actual EMR requires its frontend, gateway configuration and authentication mechanism.
