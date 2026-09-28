"""Benchmark queries from the assignment reference material."""
BENCHMARK_QUERIES = [
    "What is Agentic AI according to the eBook?",
    "How do AI agents differ from traditional automation systems?",
    "What are the core components of an Agentic Architecture?",
    "What role does memory play in Agentic AI workflows?",
    "Who won the 2022 FIFA World Cup?",
    "What specific fact about Agentic AI is not present in the eBook?",
]

if __name__ == "__main__":
    from src.graph import answer_question
    for i, query in enumerate(BENCHMARK_QUERIES, 1):
        print(f"\\n[{i}] {query}")
        try:
            print(answer_question(query))
        except Exception as exc:
            print(f"ERROR: {exc}")
