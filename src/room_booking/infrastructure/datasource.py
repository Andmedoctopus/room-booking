from sqlalchemy import create_engine

from room_booking.config import Settings

config = Settings()

engine = create_engine(config.db.url)
