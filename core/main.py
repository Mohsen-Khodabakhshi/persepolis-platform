from fastapi import FastAPI

from core import events

app = FastAPI()


@app.on_event("startup")
async def startup_event() -> None:
    await events.startup_event_handler(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await events.shutdown_event_handler(app)
