from dataclasses import asdict, fields
from decimal import Decimal
from typing import Union
from room_booking.domain.entities import RoomEntity, Cordinate, RoomEntityFilter, RoomUpdateEntity
from room_booking.infrastructure.repositories.room.constants import RoomFields
from room_booking.domain.constants import DomainFields


def build_cordinate(room_obj):
    if room_obj.longitude is None and room_obj.latitude is None:
        return None
    return Cordinate(
        longitude=Decimal(room_obj.longitude),
        latitude=Decimal(room_obj.latitude),
    )
def build_room_entity(room_obj) -> RoomEntity:
    return RoomEntity(
        room_id=room_obj.room_id, name=room_obj.name, floor=room_obj.floor, number=room_obj.number,
        cordinate=build_cordinate(room_obj)
    )


def build_dict_from_entity(room: Union[RoomEntity, RoomEntityFilter, RoomUpdateEntity], remove_id=True) -> dict:
    room_as_dict = asdict(room)

    room_as_dict.pop(RoomFields.CORDINATE.value)
    room_as_dict[RoomFields.LATITUDE.value] = str(room.get_latitude())
    room_as_dict[RoomFields.LONGITUDE.value] = str(room.get_longitude())

    if remove_id:
        room_as_dict.pop(RoomFields.ROOM_ID_FIELD_NAME.value)

    return room_as_dict

def build_update_dict_from_entity(update_entity: RoomUpdateEntity, remove_id=True):
    room_as_dict = build_dict_from_entity(update_entity, remove_id=False)

    room_as_dict = {key: value for key, value in room_as_dict.items() if value is not DomainFields.EMPTY}

    if remove_id:
        room_as_dict.pop(RoomFields.ROOM_ID_FIELD_NAME.value, None)

    return room_as_dict
