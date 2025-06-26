from phi.tools.yfinance import YFinanceTools
from .base import BaseAgent

class FinanceAgent(BaseAgent):
    def __init__(self):
        tools = [
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True,
            ),
        ]
        instructions = [
            "Display financial data in markdown tables.",
            "Include dates for stock prices and news.",
        ]
        super().__init__(
            name="Finance AI Agent",
            role="Analyze and report on financial data and market trends.",
            instructions=instructions,
            tools=tools,
        )
