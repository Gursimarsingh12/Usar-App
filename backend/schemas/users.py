
def user_schema(user: dict) -> dict:
    return {
        "user_id": user["user_id"],
        "profile_url": user["profile_url"],
        "phone_number": user["phone_number"],
        "name": user["name"],
        "semester": user["semester"],
        "branch": user["branch"]
    }