from typing import List, Optional

from room_booking.domain.entities import RoomEntity, RoomEntityFilter
from room_booking.domain.interfaces import IRoomRepository, IRoomService


class RoomService(IRoomService):
    def __init__(self, room_repository: IRoomRepository):
        self._room_repository = room_repository

    async def create(self, rooms: List[RoomEntity]) -> List[int]:
        return await self._room_repository.create(rooms)

    async def get_room(self, room_filter: Optional[RoomEntityFilter] = None) -> RoomEntity:
        return await self._room_repository.get_room(room_filter)

    async def get_rooms(self, room_filter: Optional[RoomEntityFilter] = None) -> List[RoomEntity]:
        return await self._room_repository.get_rooms(room_filter)

    async def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomEntityFilter
    ) -> None:
        return await self._room_repository.update_room(room_filter, set_room)

    async def delete_room(self, room_id: int) -> bool:
        return await self._room_repository.delete_room(room_id)
