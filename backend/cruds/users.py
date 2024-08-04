from schemas.users import user_schema
from models.users import User
from dependencies import MongoDB

async def create_user(user: User):
    user_dict = user.model_dump()
    await MongoDB.user_collection.insert_one(user_dict)
    return user_schema(user_dict)

async def get_user_by_phone(phone_number: str):
    user = await MongoDB.user_collection.find_one({"phone_number": phone_number})
    if user:
        return user_schema(user)
    return None