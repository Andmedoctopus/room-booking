import asyncio
import time
from fastapi import FastAPI

from contextlib import asynccontextmanager, contextmanager
from room_booking.containers import Application
from room_booking.domain.routers import room
from room_booking.config import Settings

@contextmanager
def init_dependency(init_resources=True):
    di_application = Application()
    di_application.resources.config.from_pydantic(Settings())

    di_application.services.wire(
        [
            room,
        ]
    )
    if init_resources:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(di_application.init_resources())

    yield di_application

    if init_resources:
        loop.run_until_complete(di_application.shutdown_resources())


def create_app() -> FastAPI:
    with init_dependency(init_resources=False) as di:
        app = FastAPI()
        app.include_router(room.router)

        @app.on_event("startup")
        async def startup():
            await di.init_resources()

        @app.on_event("shutdown")
        async def shutdown():
            await di.shutdown_resources()


        return app

