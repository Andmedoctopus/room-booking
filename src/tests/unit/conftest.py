import pytest
from httpx import AsyncClient
from room_booking.webapp import create_app

pytestmark = pytest.mark.anyio

@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope='session')
async def client(anyio_backend):
    async with AsyncClient(app=create_app(), base_url="http://test") as client:
        yield client

def room_service_mock(di, mocker):
    room_service = di.services.room
    mock = mocker.Mock(room_service)
    di.services.overide(mock)
