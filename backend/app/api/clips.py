from fastapi import APIRouter

router = APIRouter(
    prefix="/clips",
    tags=["clips"]
)


@router.get("/")
async def get_clips():
    return [
        {
            "id": 1,
            "camera": "Front Door",
            "timestamp": "2026-08-06T15:22:00",
            "filename": "front-door-test.mp4"
        }
    ]