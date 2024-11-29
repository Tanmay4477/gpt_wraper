import uvicorn
from fastapi import FastAPI
import anthropic
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_key: str = 'api'
    model_config = SettingsConfigDict(env_file=".env")

class MessageSchema(BaseModel):
    message: str

app = FastAPI()

settings = Settings()


client = anthropic.Anthropic(
    api_key=settings.api_key
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


if __name__ == "__main__":
    uvicorn.run("main:app")