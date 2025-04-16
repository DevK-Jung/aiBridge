from fastapi import FastAPI
from app.api.sample.endpoint import sample_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(sample_router.router, prefix="/api/v1/samples", tags=["Sample"])
