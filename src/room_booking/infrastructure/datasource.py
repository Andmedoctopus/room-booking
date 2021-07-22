from sqlalchemy import MetaData, create_engine

from room_booking.config import Settings

config = Settings()

metadata = MetaData()
engine = create_engine(config.db.url)
