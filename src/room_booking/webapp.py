from fastapi import FastAPI
import uvicorn

from room_booking.config import Settings
from room_booking.containers import Core
from room_booking.domain import views 


def create_app():
    app = FastAPI()
    app.include_router(views.room)
    return app


def run_app():
    Core.config.from_pydantic(Settings())
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=5050)

app = FastAPI()
app.include_router(views.room)
