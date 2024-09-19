# services/chroma_service.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

class ChromaService:
    def __init__(self, collection_name='conversation_data', persist_directory='vector_store_data'):
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = self._load_or_create_vector_store()

    def _load_or_create_vector_store(self):
        if os.path.exists(self.persist_directory):
            return Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )
        else:
            return Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory=self.persist_directory
            )

    def add_texts(self, texts):
        self.vector_store.add_texts(texts)
        self.vector_store.persist()

    def query(self, query_text):
        similar_docs = self.vector_store.similarity_search(query_text)
        if similar_docs:
            return similar_docs[0].page_content
        else:
            return "No se encontraron resultados."
