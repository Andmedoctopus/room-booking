from pydantic import BaseConfig, BaseSettings


class Server(BaseConfig):
    PORT: int = 5050

    class Meta:
        prefix = 'SERVER_'


class Settings(BaseSettings):
    server: Server = Server()
