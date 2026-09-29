"""PDF ingestion and Pinecone indexing."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

from .config import ROOT_DIR, get_settings


def _index_dimension(embedding_model: str) -> int:
    # OpenAI text-embedding-3-small defaults to 1536 dimensions.
    # Keep this isolated so the dimension can be changed with the model configuration.
    if embedding_model == "text-embedding-3-small":
        return 1536
    if embedding_model == "text-embedding-3-large":
        return 3072
    raise ValueError(
        f"Unknown embedding model {embedding_model!r}. Set the index dimension explicitly "
        "for custom models before ingestion."
    )


def ensure_index() -> None:
    settings = get_settings()
    pc = Pinecone(api_key=settings.pinecone_api_key)
    index_list = pc.list_indexes()
    existing = set(index_list.names()) if hasattr(index_list, "names") else {item["name"] for item in index_list}
    if settings.pinecone_index_name not in existing:
        pc.create_index(
            name=settings.pinecone_index_name,
            dimension=_index_dimension(settings.embedding_model),
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )


def run_ingestion(pdf_path: str | Path, reset: bool = False) -> dict:
    settings = get_settings()
    path = Path(pdf_path)
    if not path.is_absolute():
        path = ROOT_DIR / path
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    ensure_index()
    loader = PyPDFLoader(str(path))
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        add_start_index=True,
    )
    chunks = splitter.split_documents(pages)
    source_hash = hashlib.sha256(path.read_bytes()).hexdigest()[:16]

    for i, doc in enumerate(chunks):
        page = int(doc.metadata.get("page", 0)) + 1
        doc.metadata.update({
            "source": settings.source_name,
            "source_file": path.name,
            "source_hash": source_hash,
            "page": page,
            "chunk_id": f"{source_hash}-{i:05d}",
        })

    embeddings = OpenAIEmbeddings(model=settings.embedding_model)
    vector_store = PineconeVectorStore.from_existing_index(
        index_name=settings.pinecone_index_name,
        embedding=embeddings,
    )

    if reset:
        # Resetting the whole index is intentionally explicit because this project has one source.
        pc = Pinecone(api_key=settings.pinecone_api_key)
        pc.Index(settings.pinecone_index_name).delete(delete_all=True)

    vector_store.add_documents(chunks, ids=[d.metadata["chunk_id"] for d in chunks])
    return {"pages": len(pages), "chunks": len(chunks), "index": settings.pinecone_index_name}


def main() -> None:
    parser = argparse.ArgumentParser(description="Index the Agentic AI eBook in Pinecone")
    parser.add_argument("--pdf", default="data/Ebook-Agentic-AI.pdf")
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    print(run_ingestion(args.pdf, reset=args.reset))


if __name__ == "__main__":
    main()
