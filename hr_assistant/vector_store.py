import os
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from hr_assistant import config
from hr_assistant.embeddings import get_embedding_model
from hr_assistant.logger import get_logger

logger = get_logger(__name__)
client = QdrantClient(url=config.QDRANT_CLUSTER_URL, api_key=config.QDRANT_API_KEY)

def build_vector_store(chunks,path=config.VECTOR_STORE_PATH):
    if(vector_store_exists(path)):
        logger.info("Vector store found. Loading...")
        return load_vector_store(path)
    embeddings_model = get_embedding_model()
    logger.info("Vector store not found. Building vector store from chunks...")
    return QdrantVectorStore.from_documents(
        chunks, 
        embedding=embeddings_model,
        url=config.QDRANT_CLUSTER_URL,
        api_key=config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME
    )

def load_vector_store():
    logger.info("Loading vector store from %s", config.VECTOR_STORE_PATH)
    embeddings_model = get_embedding_model()
    return QdrantVectorStore(
        client=client,
        embedding=embeddings_model,
        collection_name=config.QDRANT_COLLECTION_NAME
    )

def vector_store_exists(path=config.VECTOR_STORE_PATH):
    return client.collection_exists(collection_name=config.QDRANT_COLLECTION_NAME)

def get_retriever(vector_store,k=config.TOP_K_RESULTS):
    return vector_store.as_retriever(search_kwargs={"k": k})
