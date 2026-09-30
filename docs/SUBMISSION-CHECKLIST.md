# Submission Checklist

## Core Implementation
- [x] Python RAG implementation
- [x] LangGraph workflow
- [x] Pinecone vector store integration
- [x] OpenAI embeddings (Gemini embeddings when no OpenAI key)
- [x] OpenAI LLM
- [x] Groq / Google Gemini LLM fallback (optional keys)
- [x] PDF ingestion
- [x] chunking
- [x] embeddings/indexing
- [x] retrieval
- [x] grounded generation
- [x] unsupported-question handling

## API / UI
- [x] FastAPI interface
- [x] final answer returned
- [x] retrieved context returned
- [x] confidence/relevance returned

## Testing
- [x] 6 benchmark queries defined
- [x] document-grounded queries executed (docs/BENCHMARK-RESULTS.md)
- [x] out-of-domain question executed (docs/BENCHMARK-RESULTS.md)
- [x] refusal verified with live dependencies (docs/BENCHMARK-RESULTS.md)
- [x] retrieval quality reviewed: on-topic 0.745–0.80 vs off-topic 0.534
- [x] LLM fallback verified live: Groq returned 401, Gemini answered

## Repository
- [x] clean structure
- [x] requirements.txt
- [x] .env.example
- [x] .gitignore
- [x] no API keys committed
- [x] README setup
- [x] ingestion command
- [x] application command
- [x] testing command
- [x] architecture documentation

## Final Validation
- [x] source code committed
- [x] documentation committed
- [x] clean-environment install (Python 3.12) and API boot: /health 200, validation 422, missing-key 503
- [x] end-to-end runtime test with live credentials (FastAPI /chat)
- [x] Pinecone index populated (60 pages, 119 chunks)
- [x] benchmark evidence captured (docs/BENCHMARK-RESULTS.md)
- [x] final secret scan of working files (also scan commit history before pushing)
- [ ] final submission review

> Live validation ran with Gemini embeddings and Pinecone; see docs/BENCHMARK-RESULTS.md.