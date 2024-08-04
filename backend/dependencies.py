from motor import motor_asyncio
from pymongo import MongoClient
import os
import dotenv

dotenv.load_dotenv()

mongo = os.getenv("MONGO")
client = MongoClient(mongo)
subjects_db = client.subjects
subjects_collection = subjects_db.get_collection("subjects collection")
users_db = client.users
user_collection = users_db.get_collection("users_collection")
notices_db = client.notices_db
notices_collection = notices_db.get_collection("notices_collection")