from fastapi import FastAPI

app = FastAPI(
    title="Surveillance Clips API",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "name": "Surveillance Clips API",
        "status": "running"
    }