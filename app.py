from fastapi import FastAPI
from pydantic import BaseModel
from recommendation_engine import recommend_agents
app = FastAPI()

class Query(BaseModel):
    prompt: str

@app.post('/')
def recommend_ai_agent(query: Query) -> dict[str, str]:
    recommendation = recommend_agents(query.prompt)
    return {"recommendations": recommendation}
    
