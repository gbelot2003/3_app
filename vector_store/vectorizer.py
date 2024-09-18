# vector_store/vectorizer.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def vectorize_and_store(texts, collection_name):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma(collection_name=collection_name, embedding_function=embeddings)
    vector_store.add_texts(texts)
    return vector_store
