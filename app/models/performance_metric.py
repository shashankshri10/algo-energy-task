from pydantic import BaseModel

class PerformanceMetric(BaseModel):
    asset_id: str
    uptime: float
    downtime: float
    maintenance_costs: float
    failure_rate: float
    efficiency: float
