💬 Support Assistant
A powerful Streamlit-based support assistant app that integrates with LangChain and Groq's LLM to help users manage support tickets using natural language. The assistant can create, update, search, delete, and list support tickets — all through conversational input.

🚀 Features
Natural Language Support: Chat with the assistant to manage tickets using intuitive commands.

Ticket Management: Create, view, update, delete, and search support tickets.

Groq LLM Integration: Powered by the LLaMA 3.3-70B model via Groq API.

LangChain Agents: Uses langgraph with React-style agents and tool calling.

Persistent Storage: Tickets are stored in a local SQLite database.

🖥️ App Preview
(Add screenshot here if available)

🧩 Project Structure
bash
Copy
Edit
📁 src/
│   ├── agent.py        # LangChain agent setup using Groq + tools
│   ├── crud.py         # Ticket creation, deletion, update logic
│   ├── db.py           # Database engine and session config
│   └── models.py       # SQLAlchemy models
streamlit_app.py        # Streamlit UI logic
⚙️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/support-assistant.git
cd support-assistant
Create a virtual environment and install dependencies

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Add your .env file (optional)

To preload environment variables like GROQ_API_KEY, create a .env file:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
Run the app

bash
Copy
Edit
streamlit run streamlit_app.py
🔑 Usage
Launch the app.

Enter your Groq API Key in the password field.

Start chatting! Ask things like:

"Create a ticket for John about login issue"

"List tickets for Sarah"

"Update ticket 3 to closed"

"Search tickets containing 'refund'"

"What time is it?"

🧠 Powered By
Streamlit

LangChain

LangGraph

Groq LLM

SQLAlchemy

🗃️ Example Tools in Agent
Tool	Description
create_ticket	Create a support ticket
update_ticket	Update a ticket’s status
delete_ticket	Delete a ticket
check_ticket	Retrieve ticket details
list_tickets	List tickets for a user
search_tickets	Search tickets by keyword
get_current_datetime	Get current time

📌 Notes
This app uses SQLite (tickets.db) for local storage. For production, consider switching to PostgreSQL or MySQL.

The Groq API key is required for the LLM to respond — get yours at console.groq.com.

Ticket tool logic is built into the src/crud.py file and registered automatically in the agent.