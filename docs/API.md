# API Contract

## Endpoint
POST /chat

## Request
{
  "query": "What is Agentic AI?"
}

## Response
{
  "final_answer": "Grounded answer...",
  "retrieved_context": ["chunk 1", "chunk 2", "chunk 3"],
  "confidence_score": 0.79,
  "sources": [{"page": 3, "chunk_id": "<pdf-hash>-00004"}, ...]
}

## Unsupported Response
{
  "final_answer": "I cannot answer based on the provided document.",
  "retrieved_context": [],
  "confidence_score": 0.0,
  "sources": []
}

`sources` gives the eBook page and chunk ID for each entry in `retrieved_context`, in the same order.

Refusal happens before the LLM when `confidence_score` is below the provider threshold (see README "Grounding").

## Local API
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs

## Example
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"query":"What is Agentic AI according to the eBook?"}'

## Validation
Reject blank queries. Return structured errors. Apply reasonable request-size limits.

Suggested status meanings:
- 200 successful response
- 400 invalid request
- 422 validation failure
- 500 internal error
- 503 dependency unavailable (missing keys, or Pinecone index not ingested yet)