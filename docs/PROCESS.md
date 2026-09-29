# Development and Execution Process

## Lifecycle
1. Prepare Python environment.
2. Configure secrets.
3. Add Agentic AI PDF.
4. Implement ingestion.
5. Create/configure Pinecone index.
6. Generate and upsert embeddings.
7. Implement LangGraph.
8. Add grounded generation.
9. Add relevance/refusal logic.
10. Expose FastAPI and/or Streamlit.
11. Run benchmark queries.
12. Review retrieval and grounding.
13. Perform security/repository checks.
14. Submit GitHub URL.

## Environment
python -m venv venv

macOS/Linux:
source venv/bin/activate

Windows:
venv\\Scripts\\activate

Install:
pip install -r requirements.txt

## Configuration
OPENAI_API_KEY
PINECONE_API_KEY
PINECONE_INDEX_NAME
GROQ_API_KEY (optional fallback)
GOOGLE_API_KEY (optional fallback)

Never commit .env.

## Ingestion
Place the PDF at data/Ebook-Agentic-AI.pdf, extract pages, chunk text, create embeddings, upsert to Pinecone and verify the index.

## Query
Receive question → retrieve → evaluate relevance → refuse or generate from context → return answer, evidence and score.

## Clean Validation
Clone → environment → install → configure → PDF → ingestion → verify Pinecone → start app → benchmark → grounding/refusal check → secret check → submit.

Do not describe planned or untested functionality as completed.