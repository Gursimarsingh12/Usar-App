from fastapi import APIRouter, HTTPException
from typing import List
from models.subjects import Subject
from cruds.subjects import (
    add_subject,
    get_all_subjects,
    get_subjects_by_semester_and_branch,
    get_subject_by_code,
    get_subject_by_type,
    update_subject,
    delete_subject
)

router = APIRouter()

@router.get("/")
def welcome():
    return {"message": "Welcome to USAR Subjects API!!"}

@router.post("/subjects", response_model=Subject)
async def create_subject(subject: Subject):
    return await add_subject(subject)

@router.get("/subjects", response_model=List[Subject])
async def read_all_subjects():
    return await get_all_subjects()

@router.get("/subjects/{semester_name}/{branch_name}", response_model=List[Subject])
async def read_subjects_by_semester_and_branch(semester_name: str, branch_name: str):
    return await get_subjects_by_semester_and_branch(semester_name, branch_name)

@router.get("/subjects/{semester_name}/{branch_name}/{subject_code}", response_model=Subject)
async def read_subject_by_code(semester_name: str, branch_name: str, subject_code: str):
    subject = await get_subject_by_code(semester_name, branch_name, subject_code)
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.get("/subjects/{semester_name}/{branch_name}/type/{subject_type}", response_model=List[Subject])
async def read_subjects_by_type(semester_name: str, branch_name: str, subject_type: str):
    subjects = await get_subject_by_type(semester_name, branch_name, subject_type)
    if not subjects:
        raise HTTPException(status_code=404, detail="No subjects found")
    return subjects

@router.put("/subjects/{semester_name}/{branch_name}/{subject_code}", response_model=Subject)
async def update_existing_subject(semester_name: str, branch_name: str, subject_code: str, subject: Subject):
    return await update_subject(semester_name, branch_name, subject_code, subject)

@router.delete("/subjects/{semester_name}/{branch_name}/{subject_code}", response_model=dict)
async def delete_existing_subject(semester_name: str, branch_name: str, subject_code: str):
    success = await delete_subject(semester_name, branch_name, subject_code)
    if not success:
        raise HTTPException(status_code=404, detail="Subject not found")
    return {"message": "Subject deleted successfully"}

@router.get("/semesters", response_model=List[str])
async def get_semesters() -> List[str]:
    semesters = [
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6",
        "Semester 7",
        "Semester 8"
    ]
    return semesters

@router.get("/types", response_model=List[str])
async def get_sub_type() -> List[str]:
    types = ["Theory", "Practical"]
    return types

@router.get("/branches", response_model=List[str])
async def get_branches() -> List[str]:
    branches = ["AIML", "AIDS", "AR", "IIOT"]
    return branches