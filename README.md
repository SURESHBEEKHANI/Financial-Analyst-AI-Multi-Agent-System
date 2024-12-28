# Financial AI Analyst

This project is a Financial AI Analyst that uses multiple AI agents to fetch and analyze financial data. The agents can search the web, fetch stock prices, and provide financial analysis.

## Requirements

The project requires the following Python packages:

```
phidata
python-dotenv
yfinance
packaging
duckduckgo-search
fastapi
uvicorn
groq
openai
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-ai-analyst.git
   cd financial-ai-analyst
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your API keys:
   ```
   PHI_API_KEY=your_phi_api_key
   openai_api_key=your_openai_api_key
   ```

## Usage

### Running the Financial Agent

To run the financial agent, use the following command:
```bash
python financial_agent.py
```

### Running the Playground App

To run the playground app, use the following command:
```bash
python playground.py
```

## Agents

### Web Search Agent

The Web Search Agent searches the web for information using the DuckDuckGo tool.

### Financial Agent

The Financial Agent fetches financial data such as stock prices, analyst recommendations, stock fundamentals, and company news using the YFinanceTools.

### Multi-Agent System

The Multi-Agent System combines the Web Search Agent and the Financial Agent to provide comprehensive financial analysis.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
