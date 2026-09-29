from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv
from pydantic import BaseModel

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

class Settings(BaseModel):
    openai_api_key: str
    pinecone_api_key: str
    pinecone_index_name: str = "agentic-ai-index"
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o-mini"
    groq_model: str = "llama-3.3-70b-versatile"
    google_model: str = "gemini-2.5-flash"
    top_k: int = 3
    retrieval_threshold: float = 0.30
    chunk_size: int = 1000
    chunk_overlap: int = 200
    source_name: str = "Agentic AI eBook"

    @property
    def pinecone_index_host(self) -> str | None:
        return os.getenv("PINECONE_INDEX_HOST") or None

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    values = {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "pinecone_api_key": os.getenv("PINECONE_API_KEY"),
        "pinecone_index_name": os.getenv("PINECONE_INDEX_NAME", "agentic-ai-index"),
        "embedding_model": os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
        "llm_model": os.getenv("OPENAI_LLM_MODEL", "gpt-4o-mini"),
        "groq_model": os.getenv("GROQ_LLM_MODEL", "llama-3.3-70b-versatile"),
        "google_model": os.getenv("GOOGLE_LLM_MODEL", "gemini-2.5-flash"),
        "top_k": int(os.getenv("RAG_TOP_K", "3")),
        "retrieval_threshold": float(os.getenv("RAG_RETRIEVAL_THRESHOLD", "0.30")),
        "chunk_size": int(os.getenv("RAG_CHUNK_SIZE", "1000")),
        "chunk_overlap": int(os.getenv("RAG_CHUNK_OVERLAP", "200")),
    }
    missing = [k for k in ("openai_api_key", "pinecone_api_key") if not values[k]]
    if missing:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
    return Settings(**values)
