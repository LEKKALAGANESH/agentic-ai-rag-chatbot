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

## LLM fallback
Answer generation tries OpenAI first, then Groq, then Google Gemini. A fallback is used only when its key is set in `.env`:

```
GROQ_API_KEY=
GROQ_LLM_MODEL=llama-3.3-70b-versatile
GOOGLE_API_KEY=
GOOGLE_LLM_MODEL=gemini-2.5-flash
```

Embeddings always use OpenAI, because the Pinecone vectors were created with the OpenAI embedding model and other providers' vectors are incompatible. `OPENAI_API_KEY` therefore stays required.

## Grounding
The application retrieves the top-k chunks, calculates a retrieval confidence from returned similarity scores, refuses below the configured threshold, and instructs the LLM to answer only from retrieved context.

## Documentation
See the `docs/` directory for PRD, design, architecture, RAG pipeline, API, testing, security, deployment, requirements, roadmap and submission checklist.

## Important
The PDF is intentionally ignored by Git via `data/*.pdf`. Add the assignment eBook locally before running ingestion.