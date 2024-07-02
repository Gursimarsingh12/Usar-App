from models.subjects import Subject
from typing import List

def subject_schema(subject: dict) -> dict:
    return {
        "semester_name": subject["semester_name"],
        "subject_name": subject["subject_name"],
        "subject_credits": subject["subject_credits"],
        "subject_code": subject["subject_code"],
        "subject_type": subject["subject_type"],
        "branch_name": subject["branch_name"]
    }


def subjects_list(subjects: List[dict]) -> List[dict]:
    sub_list: List[dict] = []
    for subject in subjects:
        sub = subject_schema(subject=subject)
        sub_list.append(sub)
    return sub_list