from dataclasses import asdict
from typing import List

from sqlalchemy import delete, insert, select, update

from room_booking.domain.entities import RoomEntity, RoomEntityFilter
from room_booking.domain.exceptions import RoomNotFound
from room_booking.domain.interfaces import IRoomRepository
from room_booking.infrastructure.datasource import get_connection
from room_booking.infrastructure.models import room_table
from room_booking.infrastructure.repositories.room.mapper import \
    build_room_entity


class RoomRepository(IRoomRepository):
    def create(self, rooms: List[RoomEntity]) -> List[int]:
        values = []
        for room in rooms:
            room_as_dict = asdict(room)
            room_as_dict.pop("id")
            values.append(room_as_dict)

        insert_query = insert(room_table).returning(room_table.c.id)

        with get_connection() as conn:
            rooms_obj = conn.execute(insert_query, values)

        return [room.id for room in rooms_obj]

    def get_room(self, room_filter: RoomEntityFilter) -> RoomEntity:
        room_list = self.get_room_list(room_filter)
        if len(room_list) == 0:
            raise RoomNotFound(room_filter)

        return room_list[0]

    @staticmethod
    def _patch_query_by_filter(query, room_filter: RoomEntityFilter):
        if room_filter.id is not None:
            query = query.where(room_table.c.id == room_filter.id)

        if room_filter.name is not None:
            query = query.where(room_table.c.name == room_filter.name)

        if room_filter.floor is not None:
            query = query.where(room_table.c.floor == room_filter.floor)

        if room_filter.number is not None:
            query = query.where(room_table.c.number == room_filter.number)
        return query

    def get_room_list(self, room_filter: RoomEntityFilter) -> List[RoomEntity]:
        select_query = self._patch_query_by_filter(select([room_table]), room_filter)

        with get_connection() as conn:
            rooms_obj = conn.execute(select_query)

        return [build_room_entity(room_obj) for room_obj in rooms_obj]

    def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomEntityFilter
    ) -> None:
        values = asdict(set_room)
        values.pop("id")

        update_query = self._patch_query_by_filter(update(room_table), room_filter)
        update_query = update_query.values(values)

        with get_connection() as conn:
            conn.execute(update_query)

    def delete_room(self, room_id: int) -> bool:
        delete_query = self._patch_query_by_filter(
            delete(room_table), RoomEntityFilter(id=room_id)
        )

        with get_connection() as conn:
            conn.execute(delete_query)

        return True
