# Import necessary modules and classes
from phi.agent import Agent  # Import the Agent class from the phi.agent module
from phi.tools.yfinance import YFinanceTools  # Import YFinanceTools from the phi.tools.yfinance module
from phi.tools.duckduckgo import DuckDuckGo  # Import DuckDuckGo from the phi.tools.duckduckgo module
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module
from phi.model.groq import Groq  # Import the Groq class from the phi.model.groq module
import os  # Import the os module for interacting with the operating system
import phi  # Import the phi module
from phi.playground import Playground, serve_playground_app  # Import Playground and serve_playground_app from the phi.playground module

# Load environment variables from the .env file
load_dotenv()  # Load environment variables from a .env file

# Set the API key for phi
phi.api = os.getenv("PHI_API_KEY")  # Set the API key for phi using an environment variable

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

# Create a playground app with the agents
app = Playground(agents=[finance_agent, web_search_agent]).get_app()  # Create a playground app with the agents

# Serve the playground app
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)  # Serve the playground app
