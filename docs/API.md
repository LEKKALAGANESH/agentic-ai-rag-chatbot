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
  "confidence_score": 0.91
}

## Unsupported Response
{
  "final_answer": "I cannot answer based on the provided document.",
  "retrieved_context": [],
  "confidence_score": 0.0
}

The exact score/refusal policy depends on the implemented relevance threshold.

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
- 503 dependency unavailable