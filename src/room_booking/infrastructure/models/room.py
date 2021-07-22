from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()


room_table = Table(
    "room",
    metadata,
    Column("id", Integer, Sequence("room_id_seq", metadata=meta), primary_key=True),
    Column("name", String),
    Column("floor", Integer, nullable=False),
    Column("number", Integer, nullable=False),
)
