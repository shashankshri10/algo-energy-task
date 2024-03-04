from datetime import datetime
from app.models.performance_metric import PerformanceMetric
from app.models.performance_stats import PerformanceStats
from app.db import connect_to_mongodb,close_mongodb_connection
import os

class PerformanceMetricService:
    async def get_ISO_date_string(self,dtstr: str)->str:
        date_object = datetime.strptime(dtstr, '%d/%m/%Y')
        # iso_date_string = date_object.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        return date_object
    
    # function to create performance metric and store it
    async def create_performance_metric(self,performance_metric:PerformanceMetric)->dict:
        db = await connect_to_mongodb()
        performance_metric_data = performance_metric.model_dump()
        # number of assets added byb the user
        # username = await db.users.find_one({_id:})
        # performance_metric_data['asset_id'] =asset_id
        # iso_date_string generation
        iso_date_string = await self.get_ISO_date_string(performance_metric_data["creation_date"])
        performance_metric_data["creation_date"] = iso_date_string
        # check if document with same asset_id and date is there
        res2 = await db.performance_metrics.find_one({"asset_id":performance_metric_data["asset_id"],"creation_date":iso_date_string})
        if res2 is not None:
            return {"status":False,"message":"Performance metric already exists"}
        result = await db.performance_metrics.insert_one(performance_metric_data)
        await close_mongodb_connection(db)
        if result.acknowledged:
            return {"status":True,"message":f"Performance metric created with id:{result.inserted_id}"}
        return {"status": False, "message":"Could not insert Performance metric"}
    
    # function to filter performance metrics by date
    async def get_performance_metrics_by_date(self,performance_stats:PerformanceStats)->list:
        performance_stats_data = performance_stats.model_dump()
        performance_stats_data["start_date"] = await self.get_ISO_date_string(performance_stats_data["start_date"])
        performance_stats_data["end_date"] = await self.get_ISO_date_string(performance_stats_data["end_date"])
        # print(performance_stats_data["start_date"]," ",performance_stats_data["end_date"] )
        db = await connect_to_mongodb()
        docs = await db.performance_metrics.find({"asset_id":performance_stats_data["asset_id"],
                                                 "creation_date":{"$gte":performance_stats_data["start_date"],
                                                 "$lte":performance_stats_data["end_date"]}}).to_list(length=None)
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        await close_mongodb_connection(db)
        return docs
    
    # function to calculate average downntime, total maintenance costs
    async def generate_performance_stats(self,performance_stats:PerformanceStats)->dict:
        perf_data = await self.get_performance_metrics_by_date(performance_stats)
        
        if not perf_data:
            return {"avg_downtime" : None,
                    "avg_maint_cost" : None,
                    "avg_failure_rate" : None
                    }
        num = len(perf_data)
        total_downtime=0
        total_maint_cost =0
        total_failure_rate = 0
        for perf in perf_data:
            total_downtime += perf["downtime"]
            total_maint_cost +=perf["maintenance_costs"]
            total_failure_rate += perf["failure_rate"]
        tempDict={
        "avg_downtime" : total_downtime/num,
        "avg_maint_cost" : total_maint_cost/num,
        "avg_failure_rate" : total_failure_rate/num
        }
        return tempDict
