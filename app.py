from fastapi import FastAPI 
from pydantic import BaseModel
from recommendation_engine import recommend_agents
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)


class Query(BaseModel):
    prompt: str

@app.post('/')
def recommend_ai_agent(query: Query) -> dict[str, str]:
    recommendation = recommend_agents(query.prompt)
    return {"recommendations": recommendation}
    
