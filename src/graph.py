"""LangGraph RAG workflow with strict grounding and retrieval scoring."""
from __future__ import annotations

from typing import Any, TypedDict

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langgraph.graph import END, START, StateGraph

from .config import get_settings

REFUSAL = "I cannot answer based on the provided document."

class AgentState(TypedDict, total=False):
    question: str
    documents: list[Document]
    context: list[str]
    scores: list[float]
    score: float
    answer: str


def _services():
    settings = get_settings()
    embeddings = OpenAIEmbeddings(model=settings.embedding_model)
    store = PineconeVectorStore.from_existing_index(
        index_name=settings.pinecone_index_name,
        embedding=embeddings,
    )
    llm = ChatOpenAI(model=settings.llm_model, temperature=0)
    return settings, store, llm


def retrieve(state: AgentState) -> AgentState:
    settings, store, _ = _services()
    results = store.similarity_search_with_score(state["question"], k=settings.top_k)
    docs = [doc for doc, _ in results]
    scores = [float(score) for _, score in results]
    # Pinecone cosine similarity is normally higher-is-better. Clamp for a stable API value.
    confidence = max(0.0, min(1.0, sum(scores) / len(scores))) if scores else 0.0
    return {
        "documents": docs,
        "context": [d.page_content for d in docs],
        "scores": scores,
        "score": confidence,
    }


def route_after_retrieval(state: AgentState) -> str:
    settings = get_settings()
    return "generate" if state.get("documents") and state.get("score", 0.0) >= settings.retrieval_threshold else "refuse"


def generate(state: AgentState) -> AgentState:
    _, _, llm = _services()
    context = "\n\n--- DOCUMENT CHUNK ---\n\n".join(state.get("context", []))
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a document-grounded assistant. Answer ONLY from the provided context from the Agentic AI eBook. Do not use outside knowledge. If the context does not contain enough information, respond exactly: I cannot answer based on the provided document. Keep the answer concise and factual."""),
        ("human", "Question: {question}\n\nContext:\n{context}"),
    ])
    response = llm.invoke(prompt.format_messages(question=state["question"], context=context))
    return {"answer": str(response.content).strip()}


def refuse(state: AgentState) -> AgentState:
    return {"answer": REFUSAL, "context": [], "score": 0.0}


def build_rag_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate)
    workflow.add_node("refuse", refuse)
    workflow.add_edge(START, "retrieve")
    workflow.add_conditional_edges("retrieve", route_after_retrieval, {"generate": "generate", "refuse": "refuse"})
    workflow.add_edge("generate", END)
    workflow.add_edge("refuse", END)
    return workflow.compile()


def answer_question(question: str) -> dict[str, Any]:
    if not question or not question.strip():
        raise ValueError("Question must not be empty")
    result = build_rag_graph().invoke({"question": question.strip()})
    return {
        "final_answer": result.get("answer", REFUSAL),
        "retrieved_context": result.get("context", []),
        "confidence_score": float(result.get("score", 0.0)),
    }
