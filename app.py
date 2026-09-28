"""FastAPI application for the Agentic AI RAG chatbot."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.graph import answer_question

app = FastAPI(title="Agentic AI RAG API", version="1.0.0")

class QueryRequest(BaseModel):
    query: str = Field(min_length=1, max_length=4000)

class QueryResponse(BaseModel):
    final_answer: str
    retrieved_context: list[str]
    confidence_score: float

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest) -> QueryResponse:
    try:
        result = answer_question(request.query)
        return QueryResponse(**result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="RAG service failed") from exc
