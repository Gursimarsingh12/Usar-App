from motor.motor_asyncio import AsyncIOMotorClient
import os
import dotenv

dotenv.load_dotenv()

class MongoDB:
    client: AsyncIOMotorClient = None
    subjects_collection = None
    users_collection = None
    notices_collection = None

    @classmethod
    async def connect(cls):
        if cls.client is None:
            mongo = os.getenv("MONGO")
            cls.client = AsyncIOMotorClient(mongo)
            cls.subjects_db = cls.client.subjects
            cls.subjects_collection = cls.subjects_db.get_collection("subjects collection")
            cls.users_db = cls.client.users
            cls.users_collection = cls.users_db.get_collection("users_collection")
            cls.notices_db = cls.client.notices_db
            cls.notices_collection = cls.notices_db.get_collection("notices_collection")

    @classmethod
    async def close(cls):
        if cls.client:
            cls.client.close()

    @classmethod
    async def get_subjects_collection(cls):
        await cls.connect()
        if cls.subjects_collection is None:
            raise RuntimeError("MongoDB connection nhi chl raha")
        return cls.subjects_collection