from fastapi import APIRouter
from app.config import get_clips_path
from app.services.storage_service import StorageService

router = APIRouter(
    prefix="/clips",
    tags=["clips"]
)


storage = StorageService(get_clips_path())

@router.get("/")

async def get_clips():

    return storage.list_clips()
