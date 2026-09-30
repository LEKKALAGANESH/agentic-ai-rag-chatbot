# Agentic AI RAG Chatbot

A document-grounded RAG chatbot for the Appening AI assignment.

## Stack
Python 3.10–3.13 · LangGraph · Pinecone · OpenAI (optional Groq / Google Gemini fallbacks) · FastAPI

## Architecture
Agentic AI PDF → PyPDF → RecursiveCharacterTextSplitter → OpenAI embeddings → Pinecone → LangGraph retrieval/relevance gate → grounded LLM (OpenAI → Groq → Gemini fallback) → FastAPI.

## Setup
Use Python 3.10–3.13; `langchain-pinecone` has no Python 3.14 build.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

On Windows use `venv\\Scripts\\activate`.

Place the supplied eBook at `data/Ebook-Agentic-AI.pdf`.

## Ingest
```bash
python -m src.ingestion
```

To explicitly replace the single-source index contents:
```bash
python -m src.ingestion --reset
```

## Run
```bash
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Query
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"query":"What is Agentic AI according to the eBook?"}'
```

## Benchmark
```bash
python tests_sample_queries.py
```

The benchmark requires a configured OpenAI API key and populated Pinecone index.

## Providers
Set `PINECONE_API_KEY` plus any of `OPENAI_API_KEY`, `GROQ_API_KEY`, `GOOGLE_API_KEY`.

| Role | Providers | Rule |
|---|---|---|
| Embeddings | OpenAI or Google Gemini | OpenAI if its key is set, otherwise Gemini. Override with `EMBEDDING_PROVIDER=openai\|google`. Groq has no embeddings API. |
| Answer generation | OpenAI → Groq → Gemini | Automatic fallback across every provider whose key is set. |

At least one embedding key (OpenAI or Google) is required.

Each embedding provider uses its own Pinecone index because vector dimensions differ: OpenAI uses `PINECONE_INDEX_NAME` (default `agentic-ai-index`), Gemini uses `<PINECONE_INDEX_NAME>-google`. Ingestion measures the embedding dimension and creates the index automatically. After changing the embedding provider, run ingestion again. Embeddings never fall back at query time, since query and index vectors must come from the same model.

```
OPENAI_API_KEY=
GROQ_API_KEY=
GOOGLE_API_KEY=
EMBEDDING_PROVIDER=auto
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
GOOGLE_EMBEDDING_MODEL=gemini-embedding-001
OPENAI_LLM_MODEL=gpt-4o-mini
GROQ_LLM_MODEL=llama-3.3-70b-versatile
GOOGLE_LLM_MODEL=gemini-2.5-flash
```

## Grounding
The application retrieves the top-k chunks (`RAG_TOP_K`, default 3) and computes:

```
confidence_score = clamp(mean(cosine_similarity of the top-k chunks), 0, 1)
```

If `confidence_score` is below the threshold, or nothing is retrieved, the LLM is not called: the API returns `I cannot answer based on the provided document.` with empty context and a score of 0.0. Otherwise the LLM receives only the retrieved chunks with a strict system prompt that forbids outside knowledge and requires the same refusal sentence when the context is insufficient.

Thresholds differ per embedding provider because the models score similarity on different scales:

| Embeddings | Variable | Default | Measured on this eBook |
|---|---|---|---|
| OpenAI | `RAG_RETRIEVAL_THRESHOLD` | 0.30 | not yet measured |
| Gemini | `RAG_RETRIEVAL_THRESHOLD_GOOGLE` | 0.62 | on-topic 0.745–0.80, off-topic (FIFA) 0.534 |

Related-but-unsupported questions can score above the threshold; the strict prompt then makes the LLM refuse.

Each response also includes `sources` (page and chunk ID per retrieved chunk).

## Observability
Every `/chat` request logs the question, chunk count, raw retrieval scores, confidence, whether it was refused, and latency. API keys are never logged.

## Documentation
See the `docs/` directory for PRD, design, architecture, RAG pipeline, API, testing, security, deployment, requirements, roadmap and submission checklist.

## Important
The PDF is intentionally ignored by Git via `data/*.pdf`. Add the assignment eBook locally before running ingestion.