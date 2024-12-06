from fastapi import FastAPI
from app.routers import suggest

app = FastAPI(title="Mood Playlist Generator")

# 라우터 포함
app.include_router(suggest.router, prefix="/api/v1", tags=["playlist"])

@app.get("/")
async def root():
    return {"message": "Mood Playlist Generator API"}