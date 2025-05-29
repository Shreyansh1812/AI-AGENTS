import os
from dotenv import load_dotenv
load_dotenv()

from phi.agent.agent import Agent
from phi.model.groq.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Optional check
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

finance_agent = Agent(
    name="Finance Agent",
    provider=Groq(id="llama-3.3-70b-versatile"),  # Changed from xAI to Groq
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )
    ],
    instructions=["Use tables to display data", "Summarize clearly and mention data sources."],
    show_tool_calls=True,
    markdown=True,
    agent_id="finance_agent_001",
    session_id="session_001",
    add_chat_history_to_messages=False,
    knowledge_base=None,
    add_references=False,
    references_format="json",
    output_model=None,
    debug_mode=False,
)

# Only run if this file is executed directly (not imported)
if __name__ == "__main__":
    finance_agent.print_response("Summarize analyst recommendations for AMZN", stream=True)
