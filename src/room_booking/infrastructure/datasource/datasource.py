import asyncio
from typing import Optional
from dataclasses import dataclass
from contextlib import asynccontextmanager

from dependency_injector import resources
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import Engine, Connection

from room_booking.config import Settings
from room_booking.infrastructure.datasource.constants import DB_CONNECTION_TEMPLATE


@dataclass
class DataSource:
    engine: str
    dialect: str
    username: str
    password: str
    host: str
    port: int
    database: str

    def __post_init__(self):
        self._db_engine: Optional[Engine] = None
        self._connection = None

    def get_connection_string(self) -> str:
        return DB_CONNECTION_TEMPLATE.format(
            engine=self.engine,
            dialect=self.dialect,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )

    def init_engine(self):
        self._db_engine: Engine = create_async_engine(
            self.get_connection_string(),
        )

    async def init(self):
        self.init_engine()
        await asyncio.sleep(0)

    async def shutdown(self):
        await self._db_engine.dispose()

    @asynccontextmanager
    async def open_connection(self):
        async with self._db_engine.begin() as connection:
            yield connection



async def datasource_resourcer(datasource_cls, *args, **kwargs):
    datasource = datasource_cls(*args, **kwargs)
    print('start init')
    await datasource.init()

    yield datasource

    print('shutdown')
    await datasource.shutdown()
