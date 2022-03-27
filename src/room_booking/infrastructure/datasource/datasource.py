from typing import Optional
from dataclasses import dataclass
from contextlib import contextmanager

from dependency_injector import resources
from sqlalchemy import create_engine
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
        if self._db_engine is None:
            self._db_engine: Engine = create_engine(self.get_connection_string())

    def init_connection(self):
        if self._connection is None:
            self._connection: Connection = self._db_engine.connect()

    def init(self):
        self.init_engine()
        self.init_connection()

    def shutdown(self):
        self._connection.close()

    @contextmanager
    def open_transaction(self):
        transaction = self._connection.begin()
        try:
            yield self._connection
            transaction.commit()
        except:
            transaction.rollback()
        finally:
            transaction.close()



def datasource_resourcer(datasource_cls, *args, **kwargs):
    datasource = datasource_cls(*args, **kwargs)
    datasource.init()

    yield datasource

    datasource.shutdown()
