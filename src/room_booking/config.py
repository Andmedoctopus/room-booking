from pydantic import BaseSettings



class DatabaseSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    db: str

    class Config:
        env_prefix = "POSTGRES_APP_"


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
