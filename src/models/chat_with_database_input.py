from pydantic import BaseModel

class ChatWithDatabaseInput(BaseModel):
    client_id: str # for now it will be the client name
    question: str
    openai_model:str = "gpt-4o"
    temperature: float = 0.0

    