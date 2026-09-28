# Product Requirements Document

## Product
Agentic AI RAG Chatbot

## Objective
Build a Retrieval-Augmented Generation chatbot that answers questions strictly from the supplied Agentic AI eBook.

## Goals
1. Load and parse the PDF.
2. Split it into meaningful chunks.
3. Generate OpenAI embeddings.
4. Store vectors in Pinecone.
5. Retrieve relevant chunks for a question.
6. Orchestrate retrieval and generation with LangGraph.
7. Generate only document-grounded answers.
8. Refuse unsupported questions.
9. Return answer, retrieved context and a meaningful relevance/confidence score.
10. Provide reproducible setup and testing documentation.

## Functional Requirements
- FR-01: PDF ingestion.
- FR-02: Recursive text chunking.
- FR-03: OpenAI embeddings.
- FR-04: Pinecone vector storage using cosine similarity.
- FR-05: Semantic top-k retrieval; initial recommendation is k=3.
- FR-06: LangGraph workflow orchestration.
- FR-07: Context-only answer generation.
- FR-08: Explicit refusal when evidence is insufficient.
- FR-09: Expose retrieved context.
- FR-10: Calculate confidence/relevance from a measurable signal.

## Non-Goals
- General web search.
- General-purpose LLM answers outside the eBook.
- Unrelated autonomous actions.
- Multi-document retrieval unless added later.

## Acceptance Criteria
The project is submission-ready when ingestion, indexing, retrieval, LangGraph orchestration, grounded generation, refusal behavior, context visibility, confidence scoring, benchmark testing and secure repository configuration all work and are documented.