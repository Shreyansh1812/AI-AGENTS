import os
from dotenv import load_dotenv

# Load .env variables (like GROQ_API_KEY)
load_dotenv()

# Optional: sanity check
#print("Loaded GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

from phi.agent.agent import Agent
from phi.run.response import RunResponse
from phi.model.groq.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Define the agent
web_agent = Agent(
    name="Web Agent",
    provider=Groq(id="llama-3.1-8b-instant"),  # Use a more stable model
    agent_id="web_agent_1",
    session_id="session_1",
    tools=[
        DuckDuckGo()  # Use only DuckDuckGo for now to avoid tool conflicts
    ],
    instructions=[
        "Search the web for the given query using DuckDuckGo.",
        "Provide a clear summary of the search results.",
        "Always include sources and links where possible."
    ],
    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=True,
    references_format="json",
    output_model=None,
    debug_mode=False,
    show_tool_calls=True,
    markdown=True,
)

# Only run if this file is executed directly (not imported)
if __name__ == "__main__":
    # Run the agent with a simpler query
    web_agent.print_response(
        "What are the latest AI developments in 2025?",
        stream=True
    )
