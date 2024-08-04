from motor.motor_asyncio import AsyncIOMotorClient
import os
import dotenv
import logging

dotenv.load_dotenv()

class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()

async def get_database() -> AsyncIOMotorClient:
    return db.client

mongo = os.getenv("MONGO")
subjects_db = db.client.subjects
subjects_collection = subjects_db.get_collection("subjects collection")
users_db = db.client.users
user_collection = users_db.get_collection("users_collection")
notices_db = db.client.notices_db
notices_collection = notices_db.get_collection("notices_collection")

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(mongo, maxPoolSize=10, minPoolSize=10)
    
async def close_mongo_connection():
    db.client.close()