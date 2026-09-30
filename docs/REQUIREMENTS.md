# Technical Requirements

## Runtime
| Requirement | Guidance |
|---|---|
| Python | 3.10–3.13 (3.14 unsupported: no langchain-pinecone build) |
| OS | macOS, Linux or Windows |
| Windows | WSL2 recommended |
| RAM | Minimum 8 GB |
| Internet | Required for OpenAI, Pinecone and any configured fallback LLM |
| Git | Recommended |

## Services
- OpenAI for embeddings and primary LLM.
- Optional Groq and Google Gemini as automatic LLM fallbacks.
- Google Gemini embeddings (`gemini-embedding-001`) when no OpenAI key is set; separate `-google` Pinecone index.
- Pinecone for vector storage/retrieval.
- Agentic AI eBook as knowledge source.

## Recommended Models
- text-embedding-3-small
- gpt-4o-mini
- llama-3.3-70b-versatile (Groq fallback)
- gemini-2.5-flash (Gemini fallback)

Verify current provider model dimensions and SDK configuration before creating the index because APIs can change.

## Core Dependencies
langchain
langgraph
langchain-openai
langchain-groq
langchain-google-genai
langchain-pinecone
langchain-text-splitters
pinecone (the current name of pinecone-client)
pypdf (used directly; langchain-community is deprecated and not needed)
fonttools (lets pypdf decode the eBook's heading font)
fastapi
uvicorn
streamlit
python-dotenv

## Environment
OPENAI_API_KEY=
PINECONE_API_KEY=
PINECONE_INDEX_NAME=agentic-ai-index
GROQ_API_KEY=            # optional answer fallback
GOOGLE_API_KEY=          # embeddings when no OpenAI key; answer fallback
EMBEDDING_PROVIDER=auto  # auto | openai | google

## Recommended Structure
agentic-ai-rag-chatbot/
├── data/
│   └── Ebook-Agentic-AI.pdf
├── src/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── graph.py
│   └── config.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── tests_sample_queries.py
└── docs/