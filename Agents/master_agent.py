from web_search import web_agent
from finance_agent import finance_agent

def run_agent(query):
    # Routing based on keywords
    finance_keywords = ["finance", "stock", "analyst", "revenue", "share", "price", "market", "eps", "dividend"]
    if any(word in query.lower() for word in finance_keywords):
        finance_agent.print_response(query, stream=True)  # Execute & stream output
    else:
        web_agent.print_response(query, stream=True)  # Execute & stream output

if __name__ == "__main__":
    user_query = input("Please write your query: ")
    run_agent(user_query)  # No need to return or print again
