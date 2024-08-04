from fastapi import APIRouter
from cruds.notices import get_notices, get_latest_notices
from models.notices import Notice

router = APIRouter(
    tags=["notices"],
    responses={404: {"description": "Not found"}}
)

@router.get("/notices", response_model=list[Notice])
async def fetch_notices():
    notices = await get_notices()
    return notices

@router.get("/latest-notices", response_model=list[Notice])
async def fetch_latest_notices():
    latest_notices = await get_latest_notices()
    return latest_notices