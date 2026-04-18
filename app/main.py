from retrieval import chunk_text, build_store, search
from llm import ask_llm

document = """
    Apache Airflow is an open-source platform used to programmatically author,
    schedule, and monitor workflows. It is widely used in data engineering pipelines.
    Airflow uses DAGs to define task dependencies. Docker is used for containerization.
    Faraz is my name and i am admin.
"""

chunks = chunk_text(document)

store = build_store(chunks)

query = "give me the name of admin?"

results = search(query, store, top_k=3)

print("\n--- RETRIEVED CHUNKS WITH SCORES ---")
for i, (text, score) in enumerate(results, 1):
    print(f"\n[Chunk {i}] (Score: {score:.4f})")
    print(f"{text}")

context = "\n".join([text for text, _ in results])

print(f"\n--- FINAL CONTEXT SENT TO LLM ---\n{context}")

prompt = f"""Use ONLY the context below to answer the question. 
Respond ONLY with valid JSON in this exact format, no other text:
{{
  "answer": "your exact answer here"
}}

Context:
{context}

Question: {query}

JSON Response:"""

print(prompt)
response = ask_llm(prompt)

print(f"Final Answer\n {response}")
