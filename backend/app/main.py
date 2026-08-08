from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.clips import router as clips_router
from app.api.cameras import router as cameras_router

app = FastAPI(
    title="Surveillance Clips API",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(clips_router)
app.include_router(cameras_router)

@app.get("/")
async def root():
    return {
        "name": "Surveillance Clips API",
        "status": "running",
    }