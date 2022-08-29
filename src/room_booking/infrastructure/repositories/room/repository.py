from dataclasses import asdict
from typing import List, Optional

from sqlalchemy import delete, insert, select, update, and_

from room_booking.domain.entities import RoomEntity, RoomEntityFilter, RoomUpdateEntity
from room_booking.domain.exceptions import RoomNotFound
from room_booking.domain.interfaces import IRoomRepository
from room_booking.infrastructure.datasource import DataSource
from room_booking.infrastructure.models import room_table
from room_booking.infrastructure.repositories.room.constants import RoomFields
from room_booking.infrastructure.repositories.room.mapper import build_room_entity, build_dict_from_entity, build_update_dict_from_entity


class RoomRepository(IRoomRepository):
    def __init__(self, datasource: DataSource):
        self._datasource = datasource

    @staticmethod
    def _patch_query_by_filter(query, room_filter: RoomEntityFilter):
        if room_filter.room_id is not None:
            query = query.where(room_table.c.room_id == room_filter.room_id)

        if room_filter.name is not None:
            query = query.where(room_table.c.name == room_filter.name)

        if room_filter.floor is not None:
            query = query.where(room_table.c.floor == room_filter.floor)

        if room_filter.number is not None:
            query = query.where(room_table.c.number == room_filter.number)

        if room_filter.cordinate is not None:
            query = query.where(
                and_(
                    (room_table.c.latitude == str(room_filter.cordinate.latitude)),
                    (room_table.c.longitude == str(room_filter.cordinate.longitude)),
                )
            )

        return query

    async def create(self, rooms: List[RoomEntity]) -> List[int]:
        insert_values = []
        for room in rooms:
            room_as_dict = build_dict_from_entity(room)

            insert_values.append(room_as_dict)

        insert_query = insert(room_table).returning(room_table.c.room_id)

        async with self._datasource.open_connection() as conn:
            print(f'>>> IN REPOSITORY CONNECTION {conn}')
            rooms_obj = await conn.execute(insert_query, insert_values)
            await conn.commit()

        return [room.room_id for room in rooms_obj]

    async def get_room(self, room_filter: RoomEntityFilter) -> RoomEntity:
        room_list = await self.get_rooms(room_filter)
        if len(room_list) == 0:
            raise RoomNotFound(room_filter)

        return room_list[0]


    async def get_rooms(self, room_filter: Optional[RoomEntityFilter] = None) -> List[RoomEntity]:
        if room_filter is None:
            room_filter = RoomEntityFilter()

        select_query = self._patch_query_by_filter(select([room_table]), room_filter)

        async with self._datasource.open_connection() as conn:
            print(f'>>> IN REPOSITORY CONNECTION {conn}')
            rooms_obj = await conn.execute(select_query)
            await conn.commit()

        return [build_room_entity(room_obj) for room_obj in rooms_obj]

    async def update_room(
        self, room_filter: RoomEntityFilter, set_room: RoomUpdateEntity
    ) -> None:
        values = build_update_dict_from_entity(set_room)

        update_query = self._patch_query_by_filter(update(room_table), room_filter)
        update_query = update_query.values(values)

        async with self._datasource.open_connection() as conn:
            print(f'>>> IN REPOSITORY CONNECTION {conn}')
            await conn.execute(update_query)
            await conn.commit()

    async def delete_room(self, room_id: int) -> bool:
        delete_query = self._patch_query_by_filter(
            delete(room_table), RoomEntityFilter(room_id=room_id)
        )

        async with self._datasource.open_connection() as conn:
            print(f'>>> IN REPOSITORY CONNECTION {conn}')
            await conn.execute(delete_query)
            await conn.commit()

        return True
