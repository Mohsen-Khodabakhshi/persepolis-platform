from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class DBSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str
    password: str
    database: str

    class Config:
        env_prefix = "DB_"


db_settings = DBSettings()
