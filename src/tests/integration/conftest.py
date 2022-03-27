import pytest

@pytest.fixture
def room_entity(room_entity_factory):
    return room_entity_factory()

@pytest.fixture
def room_entities(room_entity_factory):
    return [room_entity_factory() for _ in range(5)]
