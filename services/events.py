from fastapi import FastAPI

from services.db.postgres import Connection as Postgres
from services.log.config import log_config
from services.storage.minio import MinioService

import logging
from logging.config import dictConfig


async def initialize_db(app: FastAPI, settings: dict, models: list) -> None:
    postgres = Postgres(
        settings["user"],
        settings["password"],
        settings["host"],
        settings["port"],
        settings["database"],
    )
    postgres.tortoise_fastapi_db_connection(app, models)


async def initialize_logger():
    dictConfig(log_config.model_dump())
    return logging.getLogger(log_config.LOGGER_NAME)


async def initialize_storage(settings: dict):
    return MinioService(
        settings["host"], settings["access_key"], settings["secret_key"]
    )
