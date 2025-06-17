from pydantic import BaseModel

class Partner(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    love: float

