from pydantic import BaseModel

class Notice(BaseModel):
    date: str
    title: str
    link: str