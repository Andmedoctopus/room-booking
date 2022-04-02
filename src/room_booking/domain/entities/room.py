from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

from room_booking.domain.constants import DomainFields


@dataclass(frozen=True)
class Cordinate:
    longitude: Decimal
    latitude: Decimal


class CordinateAccessor:
    corinate: Union[Cordinate, DomainFields, None] = None

    def get_longitude(self):
        if isinstance(self.cordinate, Cordinate):
            return self.cordinate.longitude
        return self.cordinate

    def get_latitude(self):
        if isinstance(self.cordinate, Cordinate):
            return self.cordinate.latitude
        return self.cordinate

@dataclass(frozen=True)
class RoomEntity(CordinateAccessor):
    room_id: int
    name: str
    floor: int
    number: int
    cordinate: Optional[Cordinate] = None


@dataclass(frozen=True)
class RoomEntityFilter(CordinateAccessor):
    room_id: Optional[int] = None
    name: Optional[str] = None
    floor: Optional[int] = None
    number: Optional[int] = None
    cordinate: Optional[Cordinate] = None


@dataclass(frozen=True)
class RoomUpdateEntity(CordinateAccessor):
    room_id: Union[int, None, DomainFields] = DomainFields.EMPTY
    name: Union[str, None, DomainFields] = DomainFields.EMPTY
    floor: Union[int, None, DomainFields] = DomainFields.EMPTY
    number: Union[int, None, DomainFields] = DomainFields.EMPTY
    cordinate: Union[Cordinate, None, DomainFields] = DomainFields.EMPTY
