"""PDF ingestion and Pinecone indexing."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec

from .config import ROOT_DIR, get_settings
from .graph import embeddings as make_embeddings


def ensure_index(settings, dimension: int) -> None:
    pc = Pinecone(api_key=settings.pinecone_api_key)
    index_list = pc.list_indexes()
    existing = set(index_list.names()) if hasattr(index_list, "names") else {item["name"] for item in index_list}
    if settings.index_name not in existing:
        pc.create_index(
            name=settings.index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        return
    actual = pc.describe_index(settings.index_name).dimension
    if actual != dimension:
        raise RuntimeError(
            f"Pinecone index {settings.index_name!r} has dimension {actual}, but the "
            f"{settings.embedding_provider} embedding model produces {dimension}. "
            "Delete the index in Pinecone or set a different PINECONE_INDEX_NAME."
        )


def run_ingestion(pdf_path: str | Path, reset: bool = False) -> dict:
    settings = get_settings()
    path = Path(pdf_path)
    if not path.is_absolute():
        path = ROOT_DIR / path
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    embeddings = make_embeddings(settings)
    # Measure instead of hard-coding: dimensions differ per provider and model.
    ensure_index(settings, len(embeddings.embed_query("dimension probe")))
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

    vector_store = PineconeVectorStore.from_existing_index(
        index_name=settings.index_name,
        embedding=embeddings,
    )

    if reset:
        # Resetting the whole index is intentionally explicit because this project has one source.
        pc = Pinecone(api_key=settings.pinecone_api_key)
        pc.Index(settings.index_name).delete(delete_all=True)

    vector_store.add_documents(chunks, ids=[d.metadata["chunk_id"] for d in chunks])
    return {"pages": len(pages), "chunks": len(chunks), "index": settings.index_name, "embeddings": settings.embedding_provider}


def main() -> None:
    parser = argparse.ArgumentParser(description="Index the Agentic AI eBook in Pinecone")
    parser.add_argument("--pdf", default="data/Ebook-Agentic-AI.pdf")
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    print(run_ingestion(args.pdf, reset=args.reset))


if __name__ == "__main__":
    main()
