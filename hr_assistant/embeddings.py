from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_embedding_model(): 
    logger.info("Initializing Jina Embeddings model...")
    return JinaEmbeddings(jina_api_key=config.JINA_API_KEY, model_name=config.EMBEDDING_MODEL_NAME)
