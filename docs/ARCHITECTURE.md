# Architecture

## Target Architecture

Agentic AI PDF
→ PDF extraction
→ Recursive chunking
→ OpenAI embeddings
→ Pinecone index

User question
→ LangGraph
→ retrieve top-k chunks
→ prepare context
→ relevance/refusal decision
→ grounded generation (OpenAI → Groq → Gemini fallback, configured providers only)
→ answer + context + score

## Components

### data/Ebook-Agentic-AI.pdf
Authoritative knowledge source.

### src/ingestion.py
PDF loading, chunking, embedding and Pinecone indexing.

### src/graph.py
LangGraph state and RAG workflow.

### src/config.py
Environment variables and runtime configuration.

### app.py
FastAPI and/or Streamlit interface.

### tests_sample_queries.py
Benchmark and grounding tests.

## Graph

START → retrieve → generate → END

A stronger implementation may use:
START → retrieve → evaluate relevance → generate/refuse → END

## State
Recommended state fields:
- question
- context
- answer
- score

The implementation may additionally preserve source page, chunk ID, retrieval scores and errors.

## Data Flow

Offline:
PDF → pages → chunks → embeddings → Pinecone vectors + metadata

Online:
question → semantic retrieval → relevant context → grounding gate → LLM → response

## Boundary
The LLM must never become an unrestricted fallback knowledge source.

Provider fallback is separate from knowledge fallback: if OpenAI fails, the same grounded prompt and retrieved context go to Groq, then Gemini. Embeddings use OpenAI or Gemini (chosen once from the configured keys), each with its own Pinecone index; they never fall back at query time because query and index vectors must come from the same model.