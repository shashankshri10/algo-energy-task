from datetime import datetime
from app.models.asset import Asset
from app.models.start_end import StartEnd
from app.db import connect_to_mongodb,close_mongodb_connection
import os

class AssetService:
    async def get_ISO_date_string(self,dtstr: str)->str:
        date_object = datetime.strptime(dtstr, '%d/%m/%Y')
        # iso_date_string = date_object.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        # return iso_date_string
        return date_object
    # function to create asset and store it
    async def create_asset(self,asset:Asset,user_id:str)->dict:
        db = await connect_to_mongodb()
        asset_data = asset.model_dump()
        # number of assets added byb the user
        # username = await db.users.find_one({_id:})
        asset_data['user_id'] = user_id
        # iso_date_string generation
        iso_date_string = await self.get_ISO_date_string(asset_data["purchase_date"])
        asset_data["purchase_date"] = iso_date_string
        result = await db.assets.insert_one(asset_data)
        await close_mongodb_connection(db)
        if result.acknowledged:
            return {"status":True,"message":f"Asset created with id:{result.inserted_id}"}
        return {"status": False, "message":"Could not insert asset"}
    # get assets by user_id
    async def get_assets_by_user_id(self,user_id:str)->list:
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({"user_id":user_id}).to_list(length=5)
        await close_mongodb_connection(db)
        for asset in asset_data:
            asset["_id"] = str(asset["_id"])
        return asset_data
    # get assets by name
    async def get_assets_by_name(self, name: str) -> list:
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({"name": name}).to_list(length=5)
        await close_mongodb_connection(db)
        for asset in asset_data:
            asset["_id"] = str(asset["_id"])
        return asset_data

    async def get_assets_by_type(self, type: str) -> list:
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({"type": type}).to_list(length=5)
        await close_mongodb_connection(db)
        for asset in asset_data:
            asset["_id"] = str(asset["_id"])
        return asset_data
    
    async def get_assets_by_operational_status(self, operational_status: str) -> list:
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({"operational_status": f"{operational_status}"}).to_list(length=5)
        # print(asset_data)
        
        await close_mongodb_connection(db)
        for asset in asset_data:
            asset["_id"] = str(asset["_id"])
        return asset_data
    
    async def get_assets_by_location(self, location: str) -> list:
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({"location": f"{location}"}).to_list(length=5)
        # print(asset_data)
        
        await close_mongodb_connection(db)
        for asset in asset_data:
            asset["_id"] = str(asset["_id"])
        return asset_data
    
    async def change_date(self):
        db = await connect_to_mongodb()
        asset_data = await db.assets.find({}).to_list(length=None)
        for asset in asset_data:
            asset["purchase_date"] = datetime.fromisoformat(asset["purchase_date"])
            await db.assets.update_one({"_id":asset["_id"]},{"$set":{"purchase_date":asset["purchase_date"]}})
        print("All converisons done")
        close_mongodb_connection(db)
        pass
    
    async def get_assets_by_purchase_date(self,start_end:StartEnd,user_id:str)->list:
        start_end_data = start_end.model_dump()
        start_end_data["start_date"] = await self.get_ISO_date_string(start_end_data["start_date"])
        start_end_data["end_date"] = await self.get_ISO_date_string(start_end_data["end_date"])
        db = await connect_to_mongodb()
        # await self.change_date()
        docs = await db.assets.find({"user_id":user_id,
                                     "purchase_date":{"$gte":start_end_data["start_date"],
                                                 "$lte":start_end_data["end_date"]}}).to_list(length=None)
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        await close_mongodb_connection(db)
        return docs
            