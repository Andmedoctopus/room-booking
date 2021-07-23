from fastapi import FastAPI

from room_booking.containers import Application
from room_booking.domain.routers import room

di_application = Application()
di_application.init_resources()
di_application.services.wire(
    [
        room,
    ]
)

app = FastAPI()
app.include_router(room.router)
