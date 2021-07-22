from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str

    @property
    def url(self):
        return "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}".format(
            username=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            database=self.DB,
        )

    class Config:
        env_prefix = "POSTGRES_APP_"


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
