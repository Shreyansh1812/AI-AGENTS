import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from phi.agent.agent import Agent
from phi.run.response import RunResponse
from phi.model.google.gemini import Gemini

agent = Agent(
    provider=Gemini(id="gemini-1.5-flash"),
    agent_id="my_agent",
    session_id="my_session",
    add_chat_history_to_messages=True,
    knowledge_base=None,
    add_references=False,
    references_format="json",
    output_model=None,
    debug_mode=False,
    markdown=True,
)

agent.print_response("Please Provide me Detailed and latest Finanical Statements of Reliance Industries by looking at the Financial Statements uploaded on RIL's official Website", stream=True)