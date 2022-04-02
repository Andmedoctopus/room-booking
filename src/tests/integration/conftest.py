import pytest
from dataclasses import replace

@pytest.fixture
def room_entity(room_entity_factory):
    return room_entity_factory()

@pytest.fixture
def room_entities(room_entity_factory):
    return [room_entity_factory() for _ in range(5)]

@pytest.fixture
def created_room(room_repository, room_entity):
    return replace(room_entity, room_id=room_repository.create([room_entity])[0])

@pytest.fixture
def rooms_with_same_name_field(room_entities):
    name = room_entities[0].name
    return [replace(room, name=name)for room in room_entities]
