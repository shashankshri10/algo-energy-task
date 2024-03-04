from pydantic import BaseModel, Field, validator
from datetime import datetime

class StartEnd(BaseModel):
    start_date: str
    end_date: str
    
    @validator('start_date')
    def validate_purchase_date(cls, value):
        try:
            datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            raise ValueError('Start date must be in the dd/mm/yyyy format')
        return value
    @validator('end_date')
    def validate_purchase_date(cls, value):
        try:
            datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            raise ValueError('End date must be in the dd/mm/yyyy format')
        return value