from schemas.users import user_schema
from models.users import User
from dependencies import get_users_collection
from fastapi import HTTPException

async def create_user(user: User):
    try:
        user_collection = await get_users_collection()
        user_dict = user.model_dump()
        await user_collection.insert_one(user_dict)
        return user_schema(user_dict)
    except Exception as e:
        print(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Error creating user")

async def get_user_by_phone(phone_number: str):
    try:
        user_collection = await get_users_collection()
        user = await user_collection.find_one({"phone_number": phone_number})
        if user:
            return user_schema(user)
        return None
    except Exception as e:
        print(f"Error fetching user by phone: {e}")
        raise HTTPException(status_code=500, detail="Error fetching user by phone")
