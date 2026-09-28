# Submission Checklist

## Core
- [ ] Python RAG implementation
- [ ] LangGraph workflow
- [ ] Pinecone vector store
- [ ] OpenAI embeddings
- [ ] LLM
- [ ] PDF ingestion
- [ ] chunking
- [ ] embeddings/indexing
- [ ] retrieval
- [ ] grounded generation
- [ ] unsupported-question handling

## API / UI
- [ ] FastAPI or Streamlit works
- [ ] answer returned/displayed
- [ ] retrieved context returned/displayed
- [ ] confidence/relevance returned/displayed

## Testing
- [ ] 5–6 sample queries
- [ ] grounded questions
- [ ] out-of-domain question
- [ ] refusal verified
- [ ] retrieval quality reviewed

## Repository
- [ ] clean structure
- [ ] requirements.txt
- [ ] .env.example
- [ ] .gitignore
- [ ] no API keys
- [ ] README setup
- [ ] ingestion command
- [ ] application command
- [ ] testing commands
- [ ] architecture documentation

## Final Validation
Clone → create environment → install → configure → add PDF → ingest → verify Pinecone → start app → run benchmarks → verify grounding/refusal → check README → check secrets → push → submit GitHub URL.