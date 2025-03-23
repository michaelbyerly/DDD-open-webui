from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.openai_service import get_openai_response

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

class PromptRequest(BaseModel):
    prompt: str

@app.post("/prompt")
async def generate_prompt_response(request: PromptRequest):
    try:
        result = await get_openai_response(request.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"response": result}