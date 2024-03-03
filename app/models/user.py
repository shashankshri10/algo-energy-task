from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    full_name: str
