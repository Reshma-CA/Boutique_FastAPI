from fastapi import FastAPI
from core.config import settings
from db.session import engine

import os
from fastapi.staticfiles import StaticFiles
from apis.base import api_router
from apps.base import app_router

def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")
def configure_mediafiles(app):
    app.mount("/media", StaticFiles(directory="media"), name="media")

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE)
    include_router(app)
    configure_staticfiles(app)
    configure_mediafiles(app)
    return app



app = start_application()


