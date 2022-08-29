from dependency_injector import containers, providers

from room_booking.domain.services import RoomService
from room_booking.infrastructure.repositories import RoomRepository
from room_booking.infrastructure.datasource import datasource_resourcer, DataSource


class Resources(containers.DeclarativeContainer):
    config = providers.Configuration()
    datasource = providers.Resource(
        datasource_resourcer,
        datasource_cls=DataSource,
        engine="postgresql",
        dialect="asyncpg",
        username=config.db.user,
        password=config.db.password,
        host=config.db.host,
        port=config.db.port,
        database=config.db.db,
    )

class Repositories(containers.DeclarativeContainer):
    resources = providers.DependenciesContainer()
    room = providers.Factory(
        RoomRepository,
        resources.datasource
    )


class Services(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()
    room = providers.Factory(RoomService, repositories.room)


class Application(containers.DeclarativeContainer):
    resources = providers.Container(Resources)
    repositories = providers.Container(Repositories, resources=resources)
    services = providers.Container(Services, repositories=repositories)
