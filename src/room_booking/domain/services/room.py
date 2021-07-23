from typing import List

from room_booking.domain.entities import RoomEntity, RoomEntityFilter
from room_booking.domain.interfaces import IRoomRepository, IRoomService


class RoomService(IRoomService):
    def __init__(self, room_repository: IRoomRepository):
        self._room_repository = room_repository

    def create(self, rooms: List[RoomEntity]) -> List[int]:
        return self._room_repository.create(rooms)

    def get_room(self, room_filter: RoomEntityFilter) -> RoomEntity:
        return self._room_repository.get_room(room_filter)

    def get_room_list(self, room_filter: RoomEntityFilter) -> List[RoomEntity]:
        return self._room_repository.get_room_list(room_filter)

    def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomEntityFilter
    ) -> None:
        return self._room_repository.update_room(room_filter, set_room)

    def delete_room(self, room_id: int) -> bool:
        return self._room_repository.delete_room(room_id)
