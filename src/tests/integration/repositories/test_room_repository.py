import pytest

from room_booking.domain.entities import RoomEntityFilter
from tests.factories import room_entity_factory


def test_get_rooms__get_empty_list__pass(room_repository):
    rooms = room_repository.get_rooms()
    assert rooms == []

def test_get_by_filter__empty_db_get_empty__pass():
    assert False

def test_get_by_filter__same_flat__pass():
    assert False

def test_get_raise():
    assert False

def test_create_room__get_same_entity(room_repository, room_entity):
    room_ids = room_repository.create([room_entity])
    room_entity.room_id = room_ids[0]

    assert room_entity == room_repository.get_room(RoomEntityFilter(room_id=room_entity.room_id))

    rooms = room_repository.get_rooms()
    assert len(rooms) == 1
    assert room_entity in rooms

def test_create_multiple_room__get_same_entitis__pass(room_repository,):
    room_repository
    assert False


def test_detele_room__pass(room_repository):
    assert False

def test_detele_room__raise(room_repository):
    assert False
