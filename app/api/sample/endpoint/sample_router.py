from fastapi import APIRouter

from app.api.sample.service.sample_service import get_message

router = APIRouter()


@router.get("/{name}")
async def say_hello(name: str):
    return get_message(name)
