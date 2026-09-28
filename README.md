# Agentic AI RAG Chatbot

A document-grounded RAG chatbot for the Appening AI assignment.

## Stack
Python · LangGraph · Pinecone · OpenAI · FastAPI

## Architecture
Agentic AI PDF → PyPDF → RecursiveCharacterTextSplitter → OpenAI embeddings → Pinecone → LangGraph retrieval/relevance gate → grounded OpenAI LLM → FastAPI.

## Setup
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

## Grounding
The application retrieves the top-k chunks, calculates a retrieval confidence from returned similarity scores, refuses below the configured threshold, and instructs the LLM to answer only from retrieved context.

## Documentation
See the `docs/` directory for PRD, design, architecture, RAG pipeline, API, testing, security, deployment, requirements, roadmap and submission checklist.

## Important
The PDF is intentionally ignored by Git via `data/*.pdf`. Add the assignment eBook locally before running ingestion.