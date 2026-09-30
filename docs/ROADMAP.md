# Roadmap

## Phase 0 — Documentation
- [x] Product requirements
- [x] Design
- [x] Architecture
- [x] RAG pipeline
- [x] Process
- [x] API
- [x] Testing
- [x] Security
- [x] Deployment
- [x] Submission checklist

## Phase 1 — Foundation
- [x] Python structure
- [x] requirements.txt
- [x] .env.example
- [x] .gitignore
- [x] README
- [x] Source PDF available for local ingestion

## Phase 2 — Ingestion
- [x] PDF loader
- [x] chunking
- [x] embeddings
- [x] Pinecone index creation
- [x] metadata
- [x] Live Pinecone ingestion verification (60 pages, 119 chunks)

## Phase 3 — RAG
- [x] LangGraph state
- [x] retrieval node
- [x] context preparation
- [x] grounded generation
- [x] relevance/refusal gate
- [x] meaningful score
- [x] LLM provider fallback (OpenAI → Groq → Gemini)

## Phase 4 — Interface
- [x] FastAPI /chat
- [x] answer output
- [x] context output
- [x] score output

## Phase 5 — Evaluation
- [x] 6 benchmark queries defined
- [x] Live benchmark execution (docs/BENCHMARK-RESULTS.md)
- [x] Out-of-domain refusal verified against live index
- [x] Retrieval quality reviewed against live index
- [x] LLM fallback verified with live keys (Groq 401 → Gemini)

## Phase 6 — Submission
- [x] Source code committed
- [x] Documentation committed
- [x] Repository configuration committed
- [x] Clean-environment install and API boot (Python 3.12)
- [x] End-to-end runtime validation with live credentials
- [x] Pinecone index populated
- [x] Benchmark evidence captured
- [ ] Final submission review

## Current Status
The implementation is committed, installs on Python 3.10–3.13 and the API boots locally. Live end-to-end validation remains dependent on OpenAI/Pinecone credentials (plus optional Groq/Google keys for fallback) and the Agentic AI PDF.