from pydantic import BaseModel, Field, validator
from datetime import datetime

class PerformanceMetric(BaseModel):
    asset_id: str
    creation_date: str
    uptime: float
    downtime: float
    maintenance_costs: float
    failure_rate: float = Field(..., ge=0.0, le=1.0, description="Failure rate should be between 0 and 1")
    efficiency: float = Field(..., ge=0.0, le=100.0, description="Efficiency should be between 0 and 100")
    
    @validator('creation_date')
    def validate_purchase_date(cls, value):
        try:
            datetime.strptime(value, '%d/%m/%Y')
        except ValueError:
            raise ValueError('Creation date must be in the dd/mm/yyyy format')
        return value
