# Benchmark Results

Run on 2026-09-30 with `python tests_sample_queries.py`.

## Configuration
| Setting | Value |
|---|---|
| Embeddings | Google `gemini-embedding-001` (3072 dimensions) |
| Pinecone index | `agentic-ai-index-google`, cosine, 60 pages → 119 chunks |
| Answer LLM | Gemini `gemini-2.5-flash` (Groq key invalid at run time, so the fallback chain used Gemini) |
| top_k | 3 |
| Threshold | 0.62 (Gemini) |

## Results
| # | Query | Confidence | Pages | Outcome |
|---|---|---|---|---|
| 1 | What is Agentic AI according to the eBook? | 0.787 | 3, 7, 11 | ✅ Grounded answer |
| 2 | How do AI agents differ from traditional automation systems? | 0.750 | 9, 30, 9 | ✅ Grounded answer (RPA vs adaptive agents) |
| 3 | What are the core components of an Agentic Architecture? | 0.781 | 32, 32, 17 | ✅ Decision-making, planning, action, interaction, learning layers |
| 4 | What role does memory play in Agentic AI workflows? | 0.764 | 22, 22, 45 | ✅ Long-term and short-term memory |
| 5 | Who won the 2022 FIFA World Cup? | 0.000 | – | ✅ Refused before the LLM (raw similarity 0.534 < 0.62) |
| 6 | What specific fact about Agentic AI is not present in the eBook? | 0.772 | 3, 60, 7 | ✅ Refused by the grounded prompt |

## Answers
1. Agentic AI is an AI system that goes beyond processing data and following instructions by acting autonomously to achieve goals. It is impact-focused, proactive, and adaptive, continuously learning, focusing on goals, and acting independently.
2. AI agents differ from traditional automation systems in their ability to adapt to different situations and handle unstructured inputs. Traditional automation systems like Robotic Process Automation (RPA) excel at repetitive, rule-based tasks with structured data, following strict recipes.
3. Decision-Making Layer, Planning Layer, Action Layer, Interaction Layer, Learning Layer (with descriptions from pages 32 and 17).
4. Long-term memory stores past interactions, successful task completion methods and human demonstrations, reducing computing effort on new tasks; short-term memory is the agent's current context within its context length.
5. I cannot answer based on the provided document.
6. I cannot answer based on the provided document.

## Observations
- On-topic retrieval scores cluster at 0.745–0.80; the off-topic question scored 0.534. The 0.62 threshold separates them.
- Question 6 is topically related, so retrieval passes the threshold; the refusal comes from the strict system prompt, which is the intended second layer.
- API validation: an empty query returns 422; missing keys or a missing index return 503.
