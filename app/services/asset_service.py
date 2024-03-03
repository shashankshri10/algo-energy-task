from app.models.asset import Asset
from app.db import connect_to_mongodb,close_mongodb_connection
import os

class AssetService:
    def create_asset(self,asset:Asset):
        # Logic to create asset in database
        pass
    def get_asset(self,asset_id:str):
        # Logic to retrieve asset from database
        pass