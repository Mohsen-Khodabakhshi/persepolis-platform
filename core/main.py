from fastapi import FastAPI

from services.events import connect_to_db
from core.config import db_settings
from apps import models

app = FastAPI()

connect_to_db(app, db_settings, models)
