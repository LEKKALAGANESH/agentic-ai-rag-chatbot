from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv
from pydantic import BaseModel

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

class Settings(BaseModel):
    pinecone_api_key: str
    embedding_provider: str
    pinecone_index_name: str = "agentic-ai-index"
    embedding_model: str = "text-embedding-3-small"
    google_embedding_model: str = "gemini-embedding-001"
    llm_model: str = "gpt-4o-mini"
    groq_model: str = "llama-3.3-70b-versatile"
    google_model: str = "gemini-2.5-flash"
    top_k: int = 3
    retrieval_threshold: float = 0.30
    chunk_size: int = 1000
    chunk_overlap: int = 200
    source_name: str = "Agentic AI eBook"

    @property
    def index_name(self) -> str:
        # Each embedding provider gets its own index: vector dimensions differ and are not interchangeable.
        base = self.pinecone_index_name
        return base if self.embedding_provider == "openai" else f"{base}-{self.embedding_provider}"


def _embedding_provider() -> str:
    # Groq has no embeddings API, so only OpenAI and Google can embed.
    choice = os.getenv("EMBEDDING_PROVIDER", "auto").lower()
    if choice not in ("auto", "openai", "google"):
        raise RuntimeError("EMBEDDING_PROVIDER must be auto, openai or google")
    if choice == "auto":
        choice = "openai" if os.getenv("OPENAI_API_KEY") else "google"
    key = "OPENAI_API_KEY" if choice == "openai" else "GOOGLE_API_KEY"
    if not os.getenv(key):
        raise RuntimeError(f"Missing required environment variables: {key} (needed for {choice} embeddings)")
    return choice


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    if not os.getenv("PINECONE_API_KEY"):
        raise RuntimeError("Missing required environment variables: PINECONE_API_KEY")
    return Settings(
        pinecone_api_key=os.environ["PINECONE_API_KEY"],
        embedding_provider=_embedding_provider(),
        pinecone_index_name=os.getenv("PINECONE_INDEX_NAME", "agentic-ai-index"),
        embedding_model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
        google_embedding_model=os.getenv("GOOGLE_EMBEDDING_MODEL", "gemini-embedding-001"),
        llm_model=os.getenv("OPENAI_LLM_MODEL", "gpt-4o-mini"),
        groq_model=os.getenv("GROQ_LLM_MODEL", "llama-3.3-70b-versatile"),
        google_model=os.getenv("GOOGLE_LLM_MODEL", "gemini-2.5-flash"),
        top_k=int(os.getenv("RAG_TOP_K", "3")),
        retrieval_threshold=float(os.getenv("RAG_RETRIEVAL_THRESHOLD", "0.30")),
        chunk_size=int(os.getenv("RAG_CHUNK_SIZE", "1000")),
        chunk_overlap=int(os.getenv("RAG_CHUNK_OVERLAP", "200")),
    )
