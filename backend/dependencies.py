import os
import dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from fastapi import HTTPException

dotenv.load_dotenv()

client: Optional[AsyncIOMotorClient] = None

async def connect_to_database():
    global client
    if client is None:
        try:
            mongo_uri = os.getenv("MONGODB_URI")
            client = AsyncIOMotorClient(mongo_uri)
            print("Connected to MongoDB")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise HTTPException(status_code=500, detail="Database connection error")

async def close_database_connection():
    global client
    if client is not None:
        client.close()
        print("MongoDB connection closed")

async def get_subjects_collection():
    global client
    if client is None:
        await connect_to_database()
    db = client.subjects
    return db.get_collection("subjects collection")

async def get_users_collection():
    global client
    if client is None:
        await connect_to_database()
    db = client.users
    return db.get_collection("users_collection")

async def get_notices_collection():
    global client
    if client is None:
        await connect_to_database()
    db = client.notices_db
    return db.get_collection("notices_collection")
