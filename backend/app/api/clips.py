from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse

from app.config import get_clips_path
from app.services.storage_service import StorageService

router = APIRouter(
    prefix="/clips",
    tags=["clips"]
)


storage = StorageService(get_clips_path())


@router.get("/")
async def get_clips(request: Request):
    clips = storage.list_clips()
    for clip in clips:
        clip["stream_url"] = str(
            request.url_for("stream_clip", clip_path=clip["relative_path"])
        )

    return clips


@router.get("/{clip_path:path}/stream", name="stream_clip")
async def stream_clip(clip_path: str):
    clip = storage.get_clip(clip_path)
    if clip is None:
        raise HTTPException(status_code=404, detail="Clip not found")

    return FileResponse(
        clip,
        media_type="video/mp4",
        filename=clip.name,
        content_disposition_type="inline",
    )
