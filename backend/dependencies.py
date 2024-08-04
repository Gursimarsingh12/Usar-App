from motor import motor_asyncio
import os
import dotenv

dotenv.load_dotenv()

class MongoDB:
    client = None
    
    @classmethod
    async def get_client(cls):
        if cls.client is None:
            mongo_uri = os.getenv("MONGO")
            cls.client = motor_asyncio.AsyncIOMotorClient(mongo_uri)
        return cls.client
    
client = MongoDB.get_client()
subjects_db = client.subjects
subjects_collection = subjects_db.get_collection("subjects collection")
users_db = client.users
user_collection = users_db.get_collection("users_collection")
notices_db = client.notices_db
notices_collection = notices_db.get_collection("notices_collection")