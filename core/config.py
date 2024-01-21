from pydantic_settings import BaseSettings as PydanticBaseSettings


class BaseSettings(PydanticBaseSettings):
    class Config:
        env_file = ".env"


class AppSettings(BaseSettings):
    secret_key: str

    class Config:
        env_prefix = "APP_"


app_settings = AppSettings()


class DBSettings(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    user: str
    password: str
    database: str

    class Config:
        env_prefix = "DB_"


db_settings = DBSettings()


class JwtSettings(BaseSettings):
    admin_token_expire_hours: int
    client_token_expire_hours: int
    algorithm: str = "HS256"

    class Config:
        env_prefix = "JWT_"


jwt_settings = JwtSettings()


class MinioSettings(BaseSettings):
    access_key: str
    secret_key: str
    default_bucket_name: str
    enable: bool

    class Config:
        env_prefix = "MINIO_"


minio_settings = MinioSettings()
