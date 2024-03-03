from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

async def connect_to_mongodb():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    return db

async def close_mongodb_connection(db):
    db.client.close()
# mongo_client = AsyncIOMotorClient(MONGO_URI)
# database = mongo_client[DATABASE_NAME]