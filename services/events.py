from fastapi import FastAPI

from core.config import DBSettings

from services.db.postgres import Connection as Postgres


def connect_to_db(app: FastAPI, settings: DBSettings, models: list):
    postgres = Postgres(
        settings.user,
        settings.password,
        settings.host,
        settings.port,
        settings.database,
    )
    postgres.tortoise_fastapi_db_connection(app, models)
