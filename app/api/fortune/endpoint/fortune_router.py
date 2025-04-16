from fastapi import APIRouter

from app.api.fortune.service.fortune_service import get_fortune

router = APIRouter()


@router.get("/{name}")
async def fortune(name: str):
    return await get_fortune(name)
