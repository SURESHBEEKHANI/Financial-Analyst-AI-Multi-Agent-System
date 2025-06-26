import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.system import MultiAgentSystem

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("openai_api_key", "")

# Initialize FastAPI
app = FastAPI(
    title="Multi-Agent Financial & Web Search API",
    version="1.0.0"
)

# Allow cross-origin requests (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body model
class QueryRequest(BaseModel):
    prompt: str

# Instantiate the multi-agent system
agent_system = MultiAgentSystem()

@app.post("/query")
async def handle_query(request: QueryRequest):
    try:
        response = agent_system.query(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
