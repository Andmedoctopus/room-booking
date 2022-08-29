from urllib.parse import urljoin

import pytest
from tests.unit.views.room.conftest import ROOM_PREFIX


@pytest.mark.skip
def test_create_room():
    pass

@pytest.mark.skip
def test_update_room():
    pass


@pytest.mark.skip
async def test_get_room(client, room_repository_mock, room_entity):
    room_repository_mock.get_room.return_value = room_entity

    response = await client.get(ROOM_PREFIX)

    assert response.is_success
    assert response.json() == []


async def test_get_room_empty(client, room_repository_mock):
    room_repository_mock.get_rooms.return_value = []

    response = await client.get(ROOM_PREFIX)

    assert response.is_success
    assert response.json() == []

@pytest.mark.skip
def test_delete():
    pass

