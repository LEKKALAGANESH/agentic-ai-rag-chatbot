"""Benchmark queries from the assignment reference material."""
import sys

BENCHMARK_QUERIES = [
    "What is Agentic AI according to the eBook?",
    "How do AI agents differ from traditional automation systems?",
    "What are the core components of an Agentic Architecture?",
    "What role does memory play in Agentic AI workflows?",
    "Who won the 2022 FIFA World Cup?",
    "What specific fact about Agentic AI is not present in the eBook?",
]

if __name__ == "__main__":
    # Windows consoles default to cp1252, which cannot print some PDF characters.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    from src.graph import answer_question
    for i, query in enumerate(BENCHMARK_QUERIES, 1):
        print(f"\n[{i}] {query}")
        try:
            r = answer_question(query)
            print(f"confidence: {r['confidence_score']:.3f} | pages: {[s['page'] for s in r['sources']]}")
            print(f"answer: {r['final_answer']}")
        except Exception as exc:
            print(f"ERROR: {exc}")
