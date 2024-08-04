from motor import motor_asyncio
import os
import dotenv

dotenv.load_dotenv()

class MongoDB:
    client = None
    subjects_collection = None
    users_collection = None
    notices_collection = None

    @classmethod
    async def get_client(cls):
        if cls.client is None:
            mongo_uri = os.getenv("MONGO")
            cls.client = motor_asyncio.AsyncIOMotorClient(mongo_uri)
        return cls.client

    @classmethod
    async def get_subjects_collection(cls):
        if cls.subjects_collection is None:
            client = await cls.get_client()
            subjects_db = client.subjects
            cls.subjects_collection = subjects_db.get_collection("subjects_collection")
        return cls.subjects_collection

    @classmethod
    async def get_users_collection(cls):
        if cls.users_collection is None:
            client = await cls.get_client()
            users_db = client.users
            cls.users_collection = users_db.get_collection("users_collection")
        return cls.users_collection

    @classmethod
    async def get_notices_collection(cls):
        if cls.notices_collection is None:
            client = await cls.get_client()
            notices_db = client.notices_db
            cls.notices_collection = notices_db.get_collection("notices_collection")
        return cls.notices_collection