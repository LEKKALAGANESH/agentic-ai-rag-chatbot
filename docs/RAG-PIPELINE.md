# RAG Pipeline

## Ingestion

PDF → text extraction → document chunks → OpenAI embeddings → Pinecone vector index

## Chunking
The assignment recommends RecursiveCharacterTextSplitter with:
- chunk_size = 1000
- chunk_overlap = 200

These are starting values and should be tuned using retrieval tests.

## Retrieval
Initial recommendation:
- top-k = 3
- semantic vector similarity
- preserve page/chunk metadata where possible

## Grounding
Generation must use retrieved context only. If the context does not contain enough information, the system must not use general model knowledge and must refuse.

## Confidence
Confidence must represent a measurable signal. Possible signals:
- top retrieval similarity
- average top-k similarity
- similarity threshold
- relevance classifier
- groundedness evaluation

Do not return a fixed success value such as 0.95 for every answer without a documented meaning.

## Refusal
retrieve → relevance decision
- relevant: generate grounded answer
- insufficient: return “I cannot answer based on the provided document.”

## Evidence
Return the chunks used for generation. Page numbers and chunk IDs are recommended.

## Failure Modes
Poor chunking → tune chunk size/overlap.
Poor retrieval → tune top-k/threshold.
Hallucination → strengthen grounding prompt and refusal gate.
Missing provenance → store page/chunk metadata.
Stale index → make ingestion repeatable and index configuration explicit.