from decimal import Decimal
from room_booking.domain.entities import RoomEntity, Cordinate


def build_room_entity(room_obj) -> RoomEntity:
    return RoomEntity(
        room_id=room_obj.room_id, name=room_obj.name, floor=room_obj.floor, number=room_obj.number,
        cordinate=Cordinate(
            longitude=Decimal(room_obj.longitude),
            latitude=Decimal(room_obj.latitude),
            )
    )
