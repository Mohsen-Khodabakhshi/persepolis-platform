from fastapi import FastAPI

from services import events

from core.config import db_settings

from apps import models


async def startup_event_handler(app: FastAPI) -> None:
    app.logger = await events.initialize_logger()
    app.logger.info("Logger initialized")

    await events.initialize_db(app, db_settings.model_dump(), models)
    app.logger.info("Database initialized")


async def shutdown_event_handler(app: FastAPI) -> None:
    pass
