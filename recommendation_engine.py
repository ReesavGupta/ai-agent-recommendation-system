import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def load_agents(path: str = "knowledge_base.json"):
    with open(path) as f:
        return json.load(f)

def recommend_agents(task_desc : str, top_k=3) ->str:
    agents = load_agents()

    system_prompt = "You are a helpful assistant that matches coding tasks with the most suitable coding AI agents."

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""Given the task: "{task_desc}", recommend the best coding AI agents.
        Consider their capabilities and strengths.
        Return the top {top_k} agents and explain why."""
    
    responses = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return responses.choices[0].message.content if responses.choices[0].message.content else "" 
