import time
from unittest.mock import MagicMock
import pytest
import pytest_factoryboy

from tests.factories import __all_facotories__
from room_booking.webapp import init_dependency
from dataclasses import replace

for factory_implementation in __all_facotories__:
    pytest_factoryboy.register(factory_implementation)

@pytest.fixture(scope='session')
def di():
    with init_dependency() as di:
        yield di

@pytest.fixture
async def datasource(di):
    return await di.resources.datasource()

@pytest.fixture
def datasource_container(di):
    return di.resources.datasource


@pytest.fixture(scope="function", autouse=True)
async def transaction_rollback(datasource_container, mocker):
    datasource = await datasource_container()
    async with datasource.open_connection() as connection:
        print(f'>>> OPEN CONNECTION {connection}')

        mock = mocker.Mock(datasource)
        class DatasourceMockConnection:
            async def __aenter__(self):
                async with connection.begin_nested() as nested:
                    self.nested = nested
                    return nested

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                await self.nested.rollback()

        mock.open_connection = DatasourceMockConnection
        with datasource_container.override(mock):
            yield

@pytest.fixture
async def room_repository(di):
    return await di.repositories.room()

@pytest.fixture
def room_entity(room_entity_factory):
    return room_entity_factory()

@pytest.fixture
def room_entities(room_entity_factory):
    return [room_entity_factory() for _ in range(5)]

@pytest.fixture
async def created_room(room_repository, room_entity):
    room = await room_repository.create([room_entity])
    return replace(room_entity, room_id=room[0])

@pytest.fixture
def rooms_with_same_name_field(room_entities):
    name = room_entities[0].name
    return [replace(room, name=name)for room in room_entities]
