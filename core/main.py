from fastapi import FastAPI

from core import events

from helper.responses import Response

app = FastAPI(
    title="Persepolis IoT Platform",
    description="""
    The core of the Internet of Things or IoT platform
<a href="https://github.com/Mohsen-Khodabakhshi/persepolis-platform">Github</a>
    """,
    default_response_class=Response,
)


@app.on_event("startup")
async def startup_event() -> None:
    await events.startup_event_handler(app)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await events.shutdown_event_handler(app)
