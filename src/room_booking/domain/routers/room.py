from fastapi import APIRouter

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/")
async def read_items():
    return "Hi"
