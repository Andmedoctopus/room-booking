from fastapi import FastAPI

from contextlib import contextmanager
from room_booking.containers import Application
from room_booking.domain.routers import room
from room_booking.config import Settings

@contextmanager
def init_dependency():
    di_application = Application()
    di_application.resources.config.from_pydantic(Settings())

    di_application.init_resources()
    di_application.services.wire(
        [
            room,
        ]
    )

    yield di_application

    di_application.shutdown_resources()

def create_app() -> FastAPI:
    with init_dependency():
        app = FastAPI()
        app.include_router(room.router)
        return app

