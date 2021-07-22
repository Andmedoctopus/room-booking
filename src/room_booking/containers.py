from dependency_injector import containers, providers


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()


class Repository(containers.DeclarativeContainer):
    pass


class DomainService(containers.DeclarativeContainer):
    pass
