import pytest
from dataclasses import replace, fields

from room_booking.domain.entities import RoomEntityFilter, RoomUpdateEntity
from room_booking.domain.exceptions import RoomNotFound
from tests.utils import sync_ids_with_enitities


def test_get_rooms__get_empty_list__pass(room_repository):
    rooms = room_repository.get_rooms()
    assert rooms == []

def test_get_by_filter__empty_db_get_empty__raise_error(room_repository):
    with pytest.raises(RoomNotFound):
        room_repository.get_room(RoomEntityFilter(room_id=999999))


def test_get_by_filter__fill_random_field__raise_error(room_repository, created_room, room_entity_factory):
    new_generated_room = room_entity_factory()
    for field in fields(new_generated_room):
        room_filter = RoomEntityFilter(**{field.name: getattr(new_generated_room, field.name)})
        with pytest.raises(RoomNotFound):
            room = room_repository.get_room(room_filter)
            breakpoint()
            pytest.fail(f'Got {room} by filter {room_filter}')

def test_get_by_filter__all_params__pass(room_repository, created_room):
    for field in fields(created_room):
        room_filter = RoomEntityFilter(**{field.name: getattr(created_room, field.name)})
        assert created_room == room_repository.get_room(room_filter)

def test_get_by_same_name__get_few_room__pass(room_repository, rooms_with_same_name_field, room_entity):
    to_create = rooms_with_same_name_field + [room_entity]
    created_ids = room_repository.create(to_create)
    created_rooms = sync_ids_with_enitities(created_ids, to_create)

    name_for_search = rooms_with_same_name_field[0].name
    assert created_rooms[:-1] == room_repository.get_rooms(RoomEntityFilter(name=name_for_search))


def test_create_room__get_same_entity(room_repository, room_entity):
    room_ids = room_repository.create([room_entity])
    room_entity = replace(room_entity, room_id=room_ids[0])

    assert room_entity == room_repository.get_room(RoomEntityFilter(room_id=room_entity.room_id))
    assert [room_entity] == room_repository.get_rooms()

def test_create_multiple_room__get_same_entitis__pass(room_repository, room_entities):
    created_ids = room_repository.create(room_entities)
    created_room_entity = sync_ids_with_enitities(created_ids, room_entities)

    assert created_room_entity == room_repository.get_rooms()


def test_update_name__pass(room_repository, created_room, room_entity):
    search_id = created_room.room_id
    assert created_room == room_repository.get_room(RoomEntityFilter(room_id=search_id))

    new_name = room_entity.name
    room_repository.update_room(RoomEntityFilter(room_id=search_id), set_room=RoomUpdateEntity(name=new_name))
    after_update_entity = replace(created_room, name=new_name)
    assert after_update_entity == room_repository.get_room(RoomEntityFilter(room_id=search_id))


def test_update_room_cordinate__pass(room_repository, created_room, room_entity):
    search_id = created_room.room_id
    assert created_room == room_repository.get_room(RoomEntityFilter(room_id=search_id))

    new_cordinate = room_entity.cordinate
    room_repository.update_room(RoomEntityFilter(room_id=search_id), set_room=RoomUpdateEntity(cordinate=new_cordinate))
    after_update_entity = replace(created_room, cordinate=new_cordinate)
    assert after_update_entity == room_repository.get_room(RoomEntityFilter(room_id=search_id))

def test_update_room__raise(room_repository):
    room_repository.update_room(RoomEntityFilter(room_id=9999999999), set_room=RoomUpdateEntity(name='foo'))

def test_delete_room__pass(room_repository, created_room):
    search_id = created_room.room_id

    assert created_room == room_repository.get_room(RoomEntityFilter(room_id=search_id))
    room_repository.delete_room(search_id)

    with pytest.raises(RoomNotFound):
        assert created_room == room_repository.get_room(RoomEntityFilter(room_id=search_id))

def test_delete_room__raise(room_repository, faker):
    room_repository.delete_room(faker.pyint(100_000, 1_000_000))
