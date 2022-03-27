from sqlalchemy import Column, Integer, Sequence, String, Table

from room_booking.infrastructure.models import metadata

room_id_seq = Sequence("room_id_seq")
room_table = Table(
    "room",
    metadata,
    Column("room_id", Integer, room_id_seq, primary_key=True),
    Column("name", String),
    Column("floor", Integer, nullable=False),
    Column("number", Integer, nullable=False),
    Column("longitude", String, nullable=True),
    Column("latitude", String, nullable=True),
)
