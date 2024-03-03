from pydantic import BaseModel, validator
from datetime import datetime

class Asset(BaseModel):
    name: str
    type: str
    location: str
    purchase_date: str
    initial_cost: float
    operational_status: str

    @validator('purchase_date')
    def validate_purchase_date(cls, value):
        try:
            datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            raise ValueError('Purchase date must be in the dd/mm/yyyy format')
        return value

    @validator('operational_status')
    def validate_operational_status(cls, value):
        if value not in {"Under maintenance", "Operational"}:
            raise ValueError('Operational status must be "Under maintenance" or "Operational"')
        return value
