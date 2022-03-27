import factory
import factory.fuzzy

from room_booking.domain.entities import RoomEntity, Cordinate


class CordinateFactory(factory.Factory):
    class Meta:
        model = Cordinate

    longitude = factory.fuzzy.FuzzyDecimal(-180, 180, 4)
    latitude = factory.fuzzy.FuzzyDecimal(-180, 180, 4)

class RoomEntityFactory(factory.Factory):
    class Meta:
        model = RoomEntity

    room_id = factory.fuzzy.FuzzyInteger(0, 10_000)
    name = factory.Faker('text', max_nb_chars=20)
    floor = factory.fuzzy.FuzzyInteger(0, 20)
    number = factory.fuzzy.FuzzyInteger(0, 200)
    cordinate = factory.SubFactory(CordinateFactory)

