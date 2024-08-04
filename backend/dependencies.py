from motor import motor_asyncio
import os
import dotenv
import asyncio

dotenv.load_dotenv()

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

mongo = os.getenv("MONGO")
loop = get_or_create_eventloop()
client = motor_asyncio.AsyncIOMotorClient(mongo, io_loop=loop)
subjects_db = client.subjects
subjects_collection = subjects_db.get_collection("subjects collection")
users_db = client.users
user_collection = users_db.get_collection("users_collection")
notices_db = client.notices_db
notices_collection = notices_db.get_collection("notices_collection")