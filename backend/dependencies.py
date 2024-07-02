from motor import motor_asyncio
import os
import dotenv

dotenv.load_dotenv()

mongo = os.getenv("MONGO")
client = motor_asyncio.AsyncIOMotorClient(mongo)
db = client.subjects
collection = db.get_collection("subjects collection")