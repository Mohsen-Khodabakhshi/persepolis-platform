from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise


class Connection:
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.db_url = f"postgres://{user}:{password}@{host}:{port}/{database}"

    def tortoise_fastapi_db_connection(self, app: FastAPI, models: list):
        register_tortoise(
            app,
            db_url=self.db_url,
            modules={"models": models},
            generate_schemas=True,
            add_exception_handlers=True,
        )
