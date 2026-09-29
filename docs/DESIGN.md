# System Design

## Design Principles
1. Document-first knowledge boundary.
2. Retrieval before generation.
3. Explicit refusal for insufficient evidence.
4. Transparent retrieved context.
5. Configuration separated from application logic.

## User Flow
User question → API/UI → LangGraph → retrieve → prepare context → generate/refuse → score → answer + context + score.

## Response
Successful response contains:
- final answer
- retrieved context chunks
- confidence/relevance score

Unsupported response should clearly state that the question cannot be answered from the provided document.

## Streamlit UI
If Streamlit is selected, show:
- question input
- answer
- expandable retrieved context
- confidence/relevance score

## Error States
- Blank query: validation error.
- Vector store unavailable: service error.
- LLM unavailable: fall back OpenAI → Groq → Gemini (configured providers only); service error if all fail.
- Insufficient context: refusal.
- Invalid configuration: clear startup/configuration error.

The key product behavior is the visible and enforceable boundary between information supported by the eBook and information outside it.