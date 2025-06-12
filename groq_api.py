from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client = Groq(api_key="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")


# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend origin in production
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
        stream=False,
    )
    return {"response": completion.choices[0].message.content}
