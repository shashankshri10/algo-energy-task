from pydantic import BaseModel

class Asset(BaseModel):
    id: str
    user_id:str
    name: str
    type: str
    location: str
    purchase_date: str
    initial_cost: float
    operational_status: str
