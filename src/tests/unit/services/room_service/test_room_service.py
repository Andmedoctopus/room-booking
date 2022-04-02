import pytest

@pytest.mark.skip(reason='Not implemented')
def test_get_room__empty_db__get_empty_list(mock_room_repository, room_service):
    mock_room_repository.get_rooms.return_values = []
    assert room_service.get_rooms == []

@pytest.mark.skip(reason='Not implemented')
def test_get_room__created_entities__get_created_entities(mock_room_repository, room_service):
    mock_room_repository.get_rooms.return_values = []
    assert room_service.get_rooms == []
