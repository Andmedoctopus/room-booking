from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class Cordinate:
    longitude: Decimal
    latitude: Decimal


@dataclass
class RoomEntity:
    room_id: int
    name: str
    floor: int
    number: int
    cordinate: Optional[Cordinate] = None


@dataclass
class RoomEntityFilter:
    room_id: Optional[int] = None
    name: Optional[str] = None
    floor: Optional[int] = None
    number: Optional[int] = None
    cordinate: Optional[Cordinate] = None

