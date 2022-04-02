from urllib.parse import urljoin

import pytest
from tests.unit.views.room.conftest import ROOM_PREFIX

pytestmark = pytest.mark.anyio

@pytest.mark.skip
def test_create_room():
    pass

@pytest.mark.skip
def test_update_room():
    pass


@pytest.mark.skip
def test_get_room():
    pass


async def test_get_room_empty(client, room_service_mock):
    response = await client.get(ROOM_PREFIX)

    assert response.is_success

    assert response.json() == []

@pytest.mark.skip
def test_delete():
    pass

