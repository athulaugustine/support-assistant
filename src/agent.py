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
    Your primary responsibility is to help users manage support tickets using only the available tools.

    Before calling any tool:
    - Carefully confirm that you have received all required input parameters from the user.
    - If any parameter is missing or unclear, ask the user to provide or clarify the necessary information.
    - Do not proceed to call any tool until all required details are explicitly provided and verified.

    Your workflow:
    1. Identify the user's intent (e.g., create, update, close, view, or search a support ticket).
    2. Determine which tool is appropriate for the action.
    3. Validate that all necessary parameters for the tool are available.
    4. If any parameter is missing, prompt the user to provide the exact missing details.
    5. Once all required information is gathered, call the appropriate tool with the provided parameters.

    Be concise, user-friendly, and precise in your interactions.
    """
    # Initialize Ollama model
    agent_executor = create_react_agent(model=llm, tools=tools, prompt=prompt, checkpointer=checkpointer)
    return agent_executor