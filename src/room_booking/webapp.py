from fastapi import FastAPI
import uvicorn

from room_booking.config import Settings
from room_booking.containers import Core
from room_booking.domain.routers import room


app = FastAPI()
app.include_router(room.router)
