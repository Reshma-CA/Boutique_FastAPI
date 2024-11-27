from fastapi import FastAPI
from core.config import settings
from db.session import engine
from apis.base import  api_router
import os
from fastapi.staticfiles import StaticFiles

def include_router(app):
    app.include_router(api_router)


# Define media directory
# MEDIA_DIRECTORY = "media"
# if not os.path.exists(MEDIA_DIRECTORY):
#     os.makedirs(MEDIA_DIRECTORY)  # Create media directory if it doesn't exist

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE)
    include_router(app)
    # app.mount("/media", StaticFiles(directory=MEDIA_DIRECTORY), name="media")
    return app



app = start_application()
@app.get("/")
def hello():
    return {"message": "Welcome to the Boutique API! 👗"}
