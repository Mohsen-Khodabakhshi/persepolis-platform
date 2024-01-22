from fastapi import FastAPI

from services import events

from core.config import db_settings, minio_settings

from apps import models


async def startup_event_handler(app: FastAPI) -> None:
    app.logger = await events.initialize_logger()
    app.logger.info("Logger initialized.")

    await events.initialize_db(app, db_settings.model_dump(), models)
    app.logger.info("Database initialized.")

    app.s3 = await events.initialize_cloud_storage(minio_settings.model_dump())
    app.logger.info("Cloud storage initialized.")


async def shutdown_event_handler(app: FastAPI) -> None:
    app.s3.client.close()
    app.logger.info("Cloud storage connection closed.")
