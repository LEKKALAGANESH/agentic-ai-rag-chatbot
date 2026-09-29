# Deployment

## Local
python -m venv venv
pip install -r requirements.txt

Configure .env and place the PDF in data/.

## Ingestion
Reference command:
python -m src.ingestion

The exact command depends on the final source implementation.

## FastAPI
uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs

## Streamlit
If selected:
streamlit run app.py

## Required Deployment Configuration
- Python 3.10–3.13 (3.14 unsupported: no langchain-pinecone build)
- OpenAI API access
- Optional Groq / Google Gemini API access for LLM fallback
- Pinecone API access
- Pinecone index
- environment variables
- indexed Agentic AI document

## Pre-Deployment Validation
1. Clean environment install.
2. Verify configuration.
3. Run ingestion.
4. Verify Pinecone.
5. Start API/UI.
6. Run benchmark queries.
7. Verify refusal behavior.
8. Verify secrets are not exposed.