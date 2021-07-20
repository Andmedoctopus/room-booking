from fastapi import APIRouter
from room_booking.src


router = APIRouter(
    prefix='/rooms',
    tags=["rooms"]
)


@router.get("/")
async def read_items():
    return 
