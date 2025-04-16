from fastapi import FastAPI

from app.api.fortune.endpoint.fortune_router import router as fortune_router
from app.api.sample.endpoint.sample_router import router as sample_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(
    fortune_router,
    prefix="/api/v1/fortunes",
    tags=["Fortune"],
    responses={404: {"description": "Not found"}})

app.include_router(
    sample_router,
    prefix="/api/v1/samples",
    tags=["Sample"],
    responses={404: {"description": "Not found"}})
