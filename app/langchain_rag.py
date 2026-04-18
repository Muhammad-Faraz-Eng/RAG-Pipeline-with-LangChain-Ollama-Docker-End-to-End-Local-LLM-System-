from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA


# ------------------------
document = """
Apache Airflow is an open-source platform used to programmatically author,
schedule, and monitor workflows. It is widely used in data engineering pipelines.
Airflow uses DAGs to define task dependencies. Docker is used for containerization.
Faraz is my name and i am admin.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)

docs = splitter.create_documents([document])

embedding = HuggingFaceEmbeddings()

vectorstore = Chroma.from_documents(docs, embedding)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


llm = Ollama(model="tinyllma")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
)

query = "Who Is Admin?"

response = qa_chain.run(query)

print("\nFinal Answer")
print(response)
