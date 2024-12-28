# Import necessary modules and classes
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from the .env file
openai.api_key = os.getenv("openai_api_key")  # Set the OpenAI API key

## Create a web search agent
web_search_agent = Agent(
    name="Web Search Agent",  # Name of the agent
    role="Search the web for the information",  # Role description
    model=Groq(id="llama-3.3-70b-versatile"),  # Model used by the agent
    tools=[DuckDuckGo()],  # Tools used by the agent
    instructions=["Alway include sources"],  # Instructions for the agent
    show_tools_calls=True,  # Show tool calls in the output
    markdown=True,  # Format output in markdown
    # ...existing code...
)

## Create a financial agent
finance_agent = Agent(
    name="Finance AI Agent",  # Name of the agent
    model=Groq(id="llama-3.3-70b-versatile"),  # Model used by the agent
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),  # Tools used by the agent
    ],
    instructions=["Use tables to display the data"],  # Instructions for the agent
    show_tool_calls=True,  # Show tool calls in the output
    markdown=True,  # Format output in markdown
    # ...existing code...
)

# Create a multi-agent system combining the web search and financial agents
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],  # Team of agents
    instructions=["Always include sources", "Use table to display the data"],  # Instructions for the agents
    show_tool_calls=True,  # Show tool calls in the output
    markdown=True,  # Format output in markdown
    model=Groq(id="llama-3.3-70b-versatile"),  # Model used by the multi-agent system
    # model=Groq(id="llama3-groq-70b-8192-tool-use-preview")
)

# Use the multi-agent system to print a response to a query
multi_ai_agent.print_response("what is apple price ", stream=True)