from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=10, overlap=4):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)

    return chunks


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def build_store(chunks):
    store = []

    embeddings = model.encode(chunks)

    for i, chunk in enumerate(chunks):
        store.append(
            {
                "text": chunk,
                "embedding": embeddings[i],
            }
        )
    return store


def search(query, store, top_k=3):
    query_embedding = model.encode(query)

    results = []

    for item in store:
        score = cosine_similarity(query_embedding, item["embedding"])
        results.append((item["text"], score))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    return results[:top_k]


if __name__ == "__main__":
    document = """
    Apache Airflow is an open-source platform used to programmatically author,
    schedule, and monitor workflows. It is widely used in data engineering pipelines.
    Airflow uses DAGs to define task dependencies. Docker is used for containerization.
    Faraz is my name and i am admin.
    """

    chunks = chunk_text(document)

    store = build_store(chunks)

    query = "Who is admin?"

    results = search(query, store)
    print("\n--- CHUNKS ---")
    for c in chunks:
        print(f"chunks: [{c}]")

    print(f"Query: {query}")
    for text, score in results:
        print(f"\nScore: {score:.4f}")
        print(f"chunk: {text}")
