import os
import dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from fastapi import HTTPException

dotenv.load_dotenv()

class MongoDBClient:
    _client: Optional[AsyncIOMotorClient] = None

    @classmethod
    async def get_client(cls) -> AsyncIOMotorClient:
        if cls._client is None:
            try:
                mongo_uri = os.getenv("MONGODB_URI")
                cls._client = AsyncIOMotorClient(mongo_uri)
                print("Connected to MongoDB")
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}")
                raise HTTPException(status_code=500, detail="Database connection error")
        return cls._client

    @classmethod
    async def close_client(cls):
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            print("MongoDB connection closed")

async def get_subjects_collection():
    client = await MongoDBClient.get_client()
    db = client.subjects
    return db.get_collection("subjects collection")

async def get_users_collection():
    client = await MongoDBClient.get_client()
    db = client.users
    return db.get_collection("users_collection")

async def get_notices_collection():
    client = await MongoDBClient.get_client()
    db = client.notices_db
    return db.get_collection("notices_collection")
