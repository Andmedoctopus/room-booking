import pytest_factoryboy

from .room_entity_factory import CordinateFactory, RoomEntityFactory

__all_facotories__ = (
    CordinateFactory,
    RoomEntityFactory,
)

for factory_implementation in __all_facotories__:
    pytest_factoryboy.register(factory_implementation)
