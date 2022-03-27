from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from room_booking.containers import Services
from room_booking.domain.entities import RoomEntity, RoomEntityFilter
from room_booking.domain.interfaces.domain_services import IRoomService
from room_booking.domain.serializers import PostRoomRequest, RoomSerializer

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/")
@inject
async def get_rooms(
    room_service: IRoomService = Depends(Provide[Services.room]),
) -> List[RoomSerializer]:
    rooms = room_service.get_rooms(RoomEntityFilter())
    serialized_rooms = [
        RoomSerializer(
            id=room.room_id,
            name=room.name,
            floor=room.floor,
            number=room.number,
        )
        for room in rooms
    ]
    return serialized_rooms


@router.get("/{room_id}")
@inject
async def get_room(
    room_id: int, room_service: IRoomService = Depends(Provide[Services.room])
) -> RoomSerializer:
    room = room_service.get_room(RoomEntityFilter(id=room_id))
    return RoomSerializer(
        id=room.room_id,
        name=room.name,
        floor=room.floor,
        number=room.number,
    )


@router.post("/")
@inject
async def create_room(
    request_body: PostRoomRequest,
    room_service: IRoomService = Depends(Provide[Services.room]),
) -> List[int]:
    rooms = [
        RoomEntity(
            id=None,
            name=room.name,
            floor=room.floor,
            number=room.number,
        )
        for room in request_body.rooms
    ]
    return room_service.create(rooms)


@router.patch("/{room_id}")
@inject
async def update_room(
    room_id: int,
    update_values: RoomSerializer,
    room_service: IRoomService = Depends(Provide[Services.room]),
) -> RoomSerializer:
    room_service.update_room(
        RoomEntityFilter(id=room_id),
        RoomEntity(
            id=None,
            name=update_values.name,
            floor=update_values.floor,
            number=update_values.number,
        ),
    )
    room = room_service.get_room(RoomEntityFilter(id=room_id))
    return RoomSerializer(
        id=room.room_id,
        name=room.name,
        floor=room.floor,
        number=room.number,
    )


@router.delete("/{room_id}")
@inject
async def delete_room(
    room_id: int, room_service: IRoomService = Depends(Provide[Services.room])
) -> bool:
    return room_service.delete_room(room_id)
