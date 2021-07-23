class RoomNotFound(Exception):
    def __init__(self, room_entity):
        message = f"{room_entity} not found"
        super().__init__(message)
