from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from src.crud import (
    create_ticket, update_ticket, delete_ticket,
    check_ticket, list_tickets, search_tickets, get_current_datetime
)
from langgraph.checkpoint.memory import InMemorySaver

def get_agent(api_key):
    tools = [create_ticket, update_ticket, delete_ticket,check_ticket, list_tickets, search_tickets, get_current_datetime]
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key
    )
    checkpointer = InMemorySaver()
    prompt = """You are a Support Ticket Assistant.
    Your job is to help users manage support tickets using available tools only.
    Verify all the information before calling the tools.
    """
    # Initialize Ollama model
    agent_executor = create_react_agent(model=llm, tools=tools, prompt=prompt, checkpointer=checkpointer)
    return agent_executor