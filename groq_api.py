import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Read API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is set
if not api_key:
    raise RuntimeError("GROQ_API_KEY environment variable not set.")

# Initialize Groq client
client = Groq(api_key=api_key)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: list

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=chat_request.messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return {"response": completion.choices[0].message.content}
