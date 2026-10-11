from langchain.tools import tool
from hr_assistant.logger import get_logger

logger = get_logger(__name__)

def create_search_tool(retriever):
    """Creates a search tool that can be used by the HR assistant agent to retrieve relevant documents based on user queries."""
    @tool
    def search(query: str) -> str:
        """Searches for relevant documents based on the provided query using the given retriever."""
        logger.info("Searching vector DB for query: %s", query)
        results = retriever.invoke(query)
        if not results:
            logger.info("No relevant documents found for query: %s", query)
            return "No relevant documents found."
        return "\n\n".join([doc.page_content for doc in results])
    
    return search
