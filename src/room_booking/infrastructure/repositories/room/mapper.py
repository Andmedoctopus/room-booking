from room_booking.domain.entities import RoomEntity


def build_room_entity(room_obj) -> RoomEntity:
    print(type(room_obj))
    return RoomEntity(
        id=room_obj.id, name=room_obj.name, floor=room_obj.floor, number=room_obj.number
    )
