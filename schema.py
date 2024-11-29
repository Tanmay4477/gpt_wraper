from pydantic import BaseModel

class MessageSchema(BaseModel):
    role: str
    level: str
    answer: str