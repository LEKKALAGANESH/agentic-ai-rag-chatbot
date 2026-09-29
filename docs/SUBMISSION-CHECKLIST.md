# Submission Checklist

## Core Implementation
- [x] Python RAG implementation
- [x] LangGraph workflow
- [x] Pinecone vector store integration
- [x] OpenAI embeddings
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
- [ ] document-grounded queries executed
- [ ] out-of-domain question executed
- [ ] refusal verified with live dependencies
- [ ] retrieval quality reviewed
- [ ] LLM fallback verified with live Groq/Gemini keys

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
- [ ] end-to-end runtime test with live credentials
- [ ] Pinecone index populated
- [ ] benchmark evidence captured
- [ ] final secret scan
- [ ] final submission review

> Runtime-dependent boxes remain unchecked because this environment cannot execute the repository against your OpenAI/Pinecone credentials or the eBook PDF.