from fastapi import FastAPI

from room_booking.containers import Application
from room_booking.domain.routers import room
from room_booking.config import Settings

def init_dependency():
    di_application = Application()
    di_application.resources.config.from_pydantic(Settings())

    di_application.init_resources()
    di_application.services.wire(
        [
            room,
        ]
    )
    return di_application

def create_app() -> FastAPI:
    init_dependency()
    app = FastAPI()
    app.include_router(room.router)
    return app

