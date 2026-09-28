# Testing and Evaluation

## Objectives
Evaluate answer correctness, retrieval quality, grounding, refusal behavior, confidence scoring and API behavior.

## Required Benchmarks

### 1
What is Agentic AI according to the eBook?

### 2
How do AI agents differ from traditional automation systems?

### 3
What are the core components of an Agentic Architecture?

### 4
What role does memory play in Agentic AI workflows?

### 5 — Out of Domain
Who won the 2022 FIFA World Cup?

Expected refusal:
I cannot answer based on the provided document.

### 6 — Related but Unsupported
Ask an Agentic AI-related question whose specific answer is absent from the eBook.

Expected: refusal rather than a general-knowledge answer.

## Evaluation Matrix
| Dimension | Check |
|---|---|
| Retrieval | Are returned chunks relevant? |
| Grounding | Are answer claims supported by context? |
| Refusal | Are unsupported questions refused? |
| Confidence | Does the score reflect retrieval quality? |
| Transparency | Are context chunks visible? |
| Stability | Does behavior remain acceptable across regression runs? |

Every change to chunking, embeddings, retrieval, prompts or thresholds should rerun the benchmark set.