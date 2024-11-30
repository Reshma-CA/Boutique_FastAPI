from fastapi import FastAPI
from core.config import settings
from db.session import engine
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles
from apis.base import api_router
from apps.base import app_router
from starlette.middleware.sessions import SessionMiddleware

# Load environment variables from .env file
load_dotenv()

def include_router(app: FastAPI):
    app.include_router(api_router)
    app.include_router(app_router)

def configure_staticfiles(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def configure_mediafiles(app: FastAPI):
    app.mount("/media", StaticFiles(directory="media"), name="media")

def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE)
    
    # Add SessionMiddleware
    app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "default-secret-key"),  # Replace with a secure key
)
    
    include_router(app)
    configure_staticfiles(app)
    configure_mediafiles(app)
    return app

app = start_application()
