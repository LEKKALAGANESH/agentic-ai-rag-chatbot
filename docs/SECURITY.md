# Security

## Secrets
Required credentials:
- OPENAI_API_KEY
- PINECONE_API_KEY

Optional fallback credentials:
- GROQ_API_KEY
- GOOGLE_API_KEY

Store them in .env locally or in deployment secret storage.

## Git Protection
Minimum .gitignore entries:
.env
venv/
__pycache__/
*.pyc

## Logging
Useful:
- question
- retrieved chunk count
- retrieval scores
- latency
- final relevance score

Never log API keys, authorization headers or unnecessary sensitive data.

## Prompt Security
The generation prompt must enforce:
- retrieved context is the source of truth;
- outside model knowledge is not allowed;
- insufficient evidence causes refusal.

## Data
The Agentic AI eBook is the assignment knowledge source. Do not introduce unrelated confidential information.

## Deployment Hardening
For public deployment consider authentication, rate limiting, request limits, secret rotation, HTTPS, dependency scanning, structured audit logging and access controls.