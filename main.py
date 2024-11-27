from fastapi import FastAPI
from core.config import settings
from db.session import engine
from apis.base import  api_router
import os
from fastapi.staticfiles import StaticFiles

def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE)
    include_router(app)
    return app



app = start_application()
@app.get("/")
def hello():
    return {"message": "Welcome to the Boutique API! 👗"}
