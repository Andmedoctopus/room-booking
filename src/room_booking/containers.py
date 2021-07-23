from dependency_injector import containers, providers

from room_booking.domain.services import RoomService
from room_booking.infrastructure.repositories import RoomRepository


class Repositories(containers.DeclarativeContainer):
    room = providers.Factory(RoomRepository)


class Services(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    room = providers.Factory(RoomService, Repositories.room)


class Application(containers.DeclarativeContainer):
    repositories = providers.Container(Repositories)
    services = providers.Container(Services, repositories=repositories)
