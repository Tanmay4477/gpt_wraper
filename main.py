import uvicorn
from fastapi import FastAPI
from schema import MessageSchema
from config import client

app = FastAPI()

@app.post("/")
def interview(message: MessageSchema):
    list = [
        {"role": "user", "content": "Start"}
    ]
    list.append({"role": "user", "content": f"{message.answer}"})
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1080,
        system=f"You are a job interviewer, take {message.level} level of interview for this {message.role} role. Ask one question each time and also provide feedback for the response of the user in the same response. Be very precise. Do not ask me whether I want to process with new request or not. Just give me feedback and an another question based on it",
        messages=list
    )
    print(list, "first list")
    print(response.content)
    list.pop(0)
    print(list, "second list")
    return {"message": response.content[0].text}

if __name__ == "__main__":
    uvicorn.run("main:app")