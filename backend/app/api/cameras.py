from fastapi import APIRouter

router = APIRouter(
    prefix="/cameras",
    tags=["cameras"],
)


@router.get("/")
async def get_cameras():
    return [
        {
            "id": 1,
            "name": "Front Door",
            "brand": "Reolink",
            "enabled": True,
        },
        {
            "id": 2,
            "name": "Back Yard",
            "brand": "Reolink",
            "enabled": True,
        },
    ]