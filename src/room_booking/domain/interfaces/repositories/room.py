from abc import ABC, abstractclassmethod
from typing import List

from room_booking.domain.entities import RoomEntity, RoomEntityFilter


class IRoomRepository(ABC):
    @abstractclassmethod
    def create(self) -> int:
        pass

    @abstractclassmethod
    def get_room_list(self, room_filter: RoomEntityFilter) -> List[RoomEntity]:
        pass

    @abstractclassmethod
    def get_room(self, room_filter: RoomEntityFilter) -> RoomEntity:
        pass

    @abstractclassmethod
    def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomEntityFilter
    ) -> None:
        pass

    @abstractclassmethod
    def delete_room(self, room_id: int) -> bool:
        pass
