import os
from phi.agent import Agent
from phi.model.groq import Groq

class BaseAgent:
    def __init__(self, name: str, role: str, instructions: list, tools: list):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.tools = tools
        self.model = Groq(id="llama-3.3-70b-versatile")

    def create(self) -> Agent:
        return Agent(
            name=self.name,
            role=self.role,
            model=self.model,
            tools=self.tools,
            instructions=self.instructions,
            show_tools_calls=True,
            markdown=True,
        )
