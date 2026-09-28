# Technical Requirements

## Runtime
| Requirement | Guidance |
|---|---|
| Python | 3.10+ recommended |
| OS | macOS, Linux or Windows |
| Windows | WSL2 recommended |
| RAM | Minimum 8 GB |
| Internet | Required for OpenAI and Pinecone |
| Git | Recommended |

## Services
- OpenAI for embeddings and LLM.
- Pinecone for vector storage/retrieval.
- Agentic AI eBook as knowledge source.

## Recommended Models
- text-embedding-3-small
- gpt-4o-mini

Verify current provider model dimensions and SDK configuration before creating the index because APIs can change.

## Core Dependencies
langchain
langgraph
langchain-openai
langchain-community
langchain-pinecone
langchain-text-splitters
pinecone-client
pypdf
fastapi
uvicorn
streamlit
python-dotenv

## Environment
OPENAI_API_KEY=
PINECONE_API_KEY=
PINECONE_INDEX_NAME=agentic-ai-index

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