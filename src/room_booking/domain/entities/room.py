from dataclasses import dataclass
from typing import Optional


@dataclass
class RoomEntity:
    room_id: int
    name: str
    floor: Optional[int] = None
    number: Optional[int] = None


@dataclass
class RoomEntityFilter:
    room_id: Optional[int] = None
    name: Optional[str] = None
    floor: Optional[int] = None
    number: Optional[int] = None
