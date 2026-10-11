from hr_assistant import config
from hr_assistant.agent import create_hr_assistant_agent
from hr_assistant.document_loader import load_document
from hr_assistant.llm import get_llm
from hr_assistant.tools import create_search_tool
from hr_assistant.spitter import split_text
from hr_assistant.vector_store import (
    build_vector_store,
    load_vector_store,
    vector_store_exists,
    get_retriever
)
from hr_assistant.guardrails import REFUSAL_MESSAGE, check_input, check_output


def build_vector_store_from_document(path):
    if(vector_store_exists()):
        print("Vector store found. Loading...")
        return load_vector_store()
    print("Vector store not found. Building vector store from document...")
    document = load_document(path)
    chunks = split_text(document)
    vector_store = build_vector_store(chunks)
    return vector_store

def build_hr_assistant(path=config.DATA_FILE_PATH):
    vector_store = build_vector_store_from_document(path)
    retriver = get_retriever(vector_store)
    search_tool = create_search_tool(retriver)
    llm = get_llm()
    tools = [search_tool]
    agent = create_hr_assistant_agent(llm, tools)
    return agent


def ask(agent, question):
    input_is_sage,_ = check_input(question)
    if not input_is_sage:
        return REFUSAL_MESSAGE

    response = agent.invoke({"messages": [{"role": "user", "content": question}]})

    output_is_safe,_ = check_output(response["messages"][-1].content)
    if not output_is_safe:
        return REFUSAL_MESSAGE
    
    return response["messages"][-1].content