from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "CineAI backend is working!"}

@app.post("/generate-scene/")
def generate_scene(data: PromptInput):
    return {
        "status": "success",
        "prompt_received": data.prompt,
        "note": "ML model output will go here soon!"
    }
