from phi.agent import Agent
from phi.model.groq import Groq
from .finance import FinanceAgent
from .search import WebSearchAgent

class MultiAgentSystem:
    def __init__(self):
        self.model = Groq(id="llama-3.3-70b-versatile")
        self.team = [
            WebSearchAgent().create(),
            FinanceAgent().create(),
        ]
        self.agent = Agent(
            team=self.team,
            model=self.model,
            instructions=[
                "Use markdown formatting for output.",
                "Always include sources for any data.",
                "Use tables to present structured information.",
            ],
            show_tools_calls=True,
            markdown=True,
        )

    def query(self, prompt: str) -> str:
        return self.agent.run(prompt).content
