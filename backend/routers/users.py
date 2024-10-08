from fastapi import APIRouter, HTTPException, Query
from models.users import User
from cruds.users import create_user, get_user_by_phone

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.post("/create-user", response_model=User)
async def create_new_user(user: User):
    user = await create_user(user)
    return user

@router.get("/get-user", response_model=User)
async def read_user(phone_number: str = Query()):
    user = await get_user_by_phone(phone_number)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
