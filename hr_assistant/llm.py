from langchain_groq import ChatGroq
from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    llm = ChatGroq(
        api_key=config.GROQ_API_KEY,
        model_name=config.LLM_MODEL_NAME
    )
    logger.info("Initialized LLM model %s",llm.model_name)
    return llm