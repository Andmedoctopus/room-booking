import pytest
from httpx import AsyncClient
from room_booking.webapp import create_app


@pytest.fixture()
async def client():
    async with AsyncClient(app=create_app(), base_url="http://test") as client:
        yield client

@pytest.fixture
def room_repository_mock(di, mocker):
    room_repository = di.repositories.room
    mock = mocker.Mock(room_repository())
    with room_repository.override(mock):
        yield mock
