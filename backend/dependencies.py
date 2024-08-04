from motor.motor_asyncio import AsyncIOMotorClient
import os
import dotenv

dotenv.load_dotenv()

class MongoDB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            mongo_url = os.getenv("MONGO")
            cls._instance.client = AsyncIOMotorClient(mongo_url)
            cls._instance.subjects_db = cls._instance.client.subjects
            cls._instance.subjects_collection = cls._instance.subjects_db.get_collection("subjects_collection")
            cls._instance.users_db = cls._instance.client.users
            cls._instance.user_collection = cls._instance.users_db.get_collection("users_collection")
            cls._instance.notices_db = cls._instance.client.notices_db
            cls._instance.notices_collection = cls._instance.notices_db.get_collection("notices_collection")
        return cls._instance

# Usage
db_instance = MongoDB()
subjects_collection = db_instance.subjects_collection
user_collection = db_instance.user_collection
notices_collection = db_instance.notices_collection
