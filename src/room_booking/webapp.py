from fastapi import FastAPI

from room_booking.domain.routers import room

app = FastAPI()
app.include_router(room.router)
