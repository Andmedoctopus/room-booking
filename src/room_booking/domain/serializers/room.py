from typing import List, Optional

from pydantic import BaseModel


class RoomSerializer(BaseModel):
    id: int
    name: str
    floor: Optional[int] = None
    number: Optional[int] = None


class RoomRequest(BaseModel):
    name: str
    floor: Optional[int] = None
    number: Optional[int] = None


class PostRoomRequest(BaseModel):
    rooms: List[RoomRequest]
