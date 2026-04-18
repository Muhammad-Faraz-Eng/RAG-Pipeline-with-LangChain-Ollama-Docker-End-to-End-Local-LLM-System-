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

query = "Who Is Admin?"

results = search(query, store, top_k=3)

context = "\n".join([text for text, _ in results])

print(f"\nRetrieving Context \n {context}")

prompt = f"""
Answer the Question Using Only the context below.
    Context:
    {context}

    Question:
    {query}

    Answer:
"""

print(prompt)
response = ask_llm(prompt)

print(f"Final Answer\n {response}")
