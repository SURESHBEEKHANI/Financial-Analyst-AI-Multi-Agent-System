from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from .base import BaseAgent

class WebSearchAgent(BaseAgent):
    def __init__(self):
        tools = [
            GoogleSearch(fixed_language="english", fixed_max_results=5),
            DuckDuckGo(fixed_max_results=5),
        ]
        instructions = [
            "Always include sources in the response.",
            "Summarize search results clearly.",
        ]
        super().__init__(
            name="Web Search Agent",
            role="Search the web for reliable, relevant information.",
            instructions=instructions,
            tools=tools,
        )
