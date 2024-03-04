from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from app.models.performance_metric import PerformanceMetric
from app.models.performance_stats import PerformanceStats
from app.services.performance_metric_service import PerformanceMetricService

from ..dependencies import verify_asset

router = APIRouter(
    prefix="/performance_metric",
    tags=["performance_metric"],
    responses={404: {"description": "Not found"}},
)
performance_metric_service = PerformanceMetricService()

@router.post("/create/")
async def create_performance_metric(performance_metric:PerformanceMetric,asset_id:Annotated[str,Depends(verify_asset)]):
    try:
        res_dict = await performance_metric_service.create_performance_metric(performance_metric)
        if res_dict["status"]:
            return {"message": res_dict["message"]}
        else:
            raise HTTPException(status_code=401, detail=res_dict["message"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/bydate/")
async def get_performance_metrics_by_date(performance_stats:PerformanceStats,asset_id:Annotated[str,Depends(verify_asset)]):
    
    stats_list = await performance_metric_service.get_performance_metrics_by_date(performance_stats)
    if not stats_list:
        raise HTTPException(status_code=404, detail="Metrics not found")
    return stats_list

@router.post("/generate_performance_stats/")
async def generate_performance_stats(performance_stats:PerformanceStats,asset_id:Annotated[str,Depends(verify_asset)]):
    stats_dict = await performance_metric_service.generate_performance_stats(performance_stats)
    if stats_dict["avg_downtime"] is None:
        raise HTTPException(status_code=404, detail="Metrics not found")
    return stats_dict