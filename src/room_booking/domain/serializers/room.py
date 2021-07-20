from pydantic import Model


class RoomSerializer(Model):
    id: int
    name: str

