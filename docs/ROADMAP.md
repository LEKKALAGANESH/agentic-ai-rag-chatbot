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
- [ ] Source PDF available for local ingestion

## Phase 2 — Ingestion
- [x] PDF loader
- [x] chunking
- [x] embeddings
- [x] Pinecone index creation
- [x] metadata
- [ ] Live Pinecone ingestion verification (requires credentials)

## Phase 3 — RAG
- [x] LangGraph state
- [x] retrieval node
- [x] context preparation
- [x] grounded generation
- [x] relevance/refusal gate
- [x] meaningful score

## Phase 4 — Interface
- [x] FastAPI /chat
- [x] answer output
- [x] context output
- [x] score output

## Phase 5 — Evaluation
- [x] 6 benchmark queries defined
- [ ] Live benchmark execution
- [ ] Out-of-domain refusal verified against live index
- [ ] Retrieval quality reviewed against live index

## Phase 6 — Submission
- [x] Source code committed
- [x] Documentation committed
- [x] Repository configuration committed
- [ ] Clean-environment runtime validation
- [ ] Pinecone index populated
- [ ] Benchmark evidence captured
- [ ] Final submission review

## Current Status
The implementation is committed. Live end-to-end validation remains dependent on installing the dependencies, providing OpenAI/Pinecone credentials, and supplying the Agentic AI PDF.