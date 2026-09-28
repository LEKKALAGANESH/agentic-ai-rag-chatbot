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
→ grounded generation
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