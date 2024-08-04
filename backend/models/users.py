from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    profile_url: str
    phone_number: str
    name: str
    semester: str
    branch: str