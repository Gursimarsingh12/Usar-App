from dependencies import get_subjects_collection
from models.subjects import Subject
from schemas.subjects import subject_schema, subjects_list
from typing import List
from fastapi import HTTPException

async def add_subject(subject: Subject) -> Subject:
    subjects_collection = await get_subjects_collection()
    sub = await subjects_collection.insert_one(subject.model_dump())
    if sub.inserted_id:
        return subject
    raise HTTPException(status_code=500, detail="Subject could not be added")

async def get_all_subjects() -> List[dict]:
    subjects_collection = await get_subjects_collection()
    subs = await subjects_collection.find({}).to_list(None)
    return subjects_list(subs)

async def get_subjects_by_semester_and_branch(semester_name: str, branch_name: str) -> List[dict]:
    subjects_collection = await get_subjects_collection()
    subs = await subjects_collection.find({"semester_name": semester_name, "branch_name": branch_name}).to_list(None)
    if subs:
        return subjects_list(subs)
    return []

async def get_subject_by_code(semester_name: str, branch_name: str, subject_code: str) -> dict:
    subjects_collection = await get_subjects_collection()
    sub = await subjects_collection.find_one({"semester_name": semester_name, "branch_name": branch_name, "subject_code": subject_code})
    if sub:
        return subject_schema(sub)
    return None

async def get_subject_by_type(semester_name: str, branch_name: str, subject_type: str) -> List[dict]:
    subjects_collection = await get_subjects_collection()
    subs = await subjects_collection.find({"semester_name": semester_name, "branch_name": branch_name, "subject_type": subject_type}).to_list(None)
    if subs:
        return subjects_list(subs)
    return []

async def update_subject(semester_name: str, branch_name: str, subject_code: str, subject_data: Subject) -> Subject:
    subjects_collection = await get_subjects_collection()
    sub = await subjects_collection.find_one({"semester_name": semester_name, "branch_name": branch_name, "subject_code": subject_code})
    if sub:
        await subjects_collection.update_one({"_id": sub["_id"]}, {"$set": subject_data.model_dump()})
        return subject_data
    raise HTTPException(status_code=404, detail="Subject not found")

async def delete_subject(semester_name: str, branch_name: str, subject_code: str) -> bool:
    subjects_collection = await get_subjects_collection()
    subject = await subjects_collection.find_one({"semester_name": semester_name, "branch_name": branch_name, "subject_code": subject_code})
    if subject:
        await subjects_collection.delete_one({"_id": subject["_id"]})
        return True
    return False
