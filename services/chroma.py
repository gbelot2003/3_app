import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

class ChromaService:
    def __init__(self, collection_name='conversation_data', persist_directory='vector_store_data'):
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = self._load_or_create_vector_store()

    def _load_or_create_vector_store(self):
        # Inicializar Chroma con persistencia automática
        return Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )

    def add_texts(self, texts):
        # Agregar textos al vector store
        self.vector_store.add_texts(texts)
        # No es necesario llamar a persist(), la persistencia es automática

    def query(self, query_text):
        similar_docs = self.vector_store.similarity_search(query_text)
        if similar_docs:
            return similar_docs[0].page_content
        else:
            return "No se encontraron resultados."
