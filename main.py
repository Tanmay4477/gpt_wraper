import uvicorn
from fastapi import FastAPI
import anthropic
from pydantic import BaseModel
from pydantic_settings import BaseSettings

class MessageSchema(BaseModel):
    message: str

class Settings(BaseSettings):
    api_key: str = "API"

settings = Settings()
app = FastAPI()

client = anthropic.Anthropic(
    api_key="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"
)

@app.get("/")
async def root():
    return {"message": "App Started"}

@app.post("/template")
def template(message: MessageSchema):
    message_to_string = str(message)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=50,
        messages=[
            {"role": "user", "content": [{
                "type": "text",
                "text": message_to_string
            }]}
        ]
    )
    print(response.content)
    return {"message": response.content[0].text}

@app.post("/chat")
def chat():
    return {"message": "New Chat"}

if __name__ == "__main__":
    uvicorn.run("main:app")