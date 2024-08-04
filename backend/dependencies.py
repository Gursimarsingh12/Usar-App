from motor import motor_asyncio
import os
import dotenv
from main import get_or_create_eventloop

dotenv.load_dotenv()

mongo = os.getenv("MONGO")
loop = get_or_create_eventloop()
client = motor_asyncio.AsyncIOMotorClient(mongo, io_loop=loop)
subjects_db = client.subjects
subjects_collection = subjects_db.get_collection("subjects collection")
users_db = client.users
user_collection = users_db.get_collection("users_collection")
notices_db = client.notices_db
notices_collection = notices_db.get_collection("notices_collection")