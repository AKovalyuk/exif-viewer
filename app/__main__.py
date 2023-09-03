from fastapi import FastAPI

from app.endpoints import routers


def get_app():
    app = FastAPI()
    for router in routers:
        app.include_router(router)
    return app


app = get_app()
