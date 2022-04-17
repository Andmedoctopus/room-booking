from abc import ABC, abstractclassmethod
from typing import List, Optional

from room_booking.domain.entities import RoomEntity, RoomEntityFilter


class IRoomService(ABC):
    @abstractclassmethod
    async def create(self) -> List[int]:
        pass

    @abstractclassmethod
    async def get_room(self, room_filter: Optional[RoomEntityFilter] = None) -> RoomEntity:
        pass

    @abstractclassmethod
    async def get_rooms(self, room_filter: Optional[RoomEntityFilter] = None) -> List[RoomEntity]:
        pass

    @abstractclassmethod
    async def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomEntityFilter
    ) -> None:
        pass

    @abstractclassmethod
    async def delete_room(self, room_id: int) -> bool:
        pass
