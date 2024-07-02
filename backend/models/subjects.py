from pydantic import BaseModel

class Subject(BaseModel):
    semester_name: str
    subject_name: str
    subject_credits: int
    subject_code: str
    subject_type: str
    branch_name: str