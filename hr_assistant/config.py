import os 
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

DATA_FILE_PATH = os.path.join("data", "hr_policy.txt")
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

LLM_MODEL_NAME = "openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"
GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

TOP_K_RESULTS = 3

SYSTEM_PROMPT = """you are a helpful HR assistant. always use the hr_policy_search tool to answer questions about the company's HR policies. if you don't know the answer, say "I don't know" and do not make up an answer.Don't answer anything other than HR policy questions, just say 'I can't answer that, ask only HR questions''"""

LANGSMITH_TRACING=os.getenv("LANGSMITH_TRACING")
LANGSMITH_ENDPOINT=os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY=os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT=os.getenv("LANGSMITH_PROJECT")

QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")
QDRANT_CLUSTER_URL=os.getenv("QDRANT_CLUSTER_URL")
QDRANT_COLLECTION_NAME=os.getenv("QUADRANT_COLLECTION_NAME")

def check_env_variables():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")
    if not JINA_API_KEY:
        raise ValueError("JINA_API_KEY is not set in the environment variables.")