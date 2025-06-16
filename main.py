
from fastapi import FastAPI
from backend.core.config import settings
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles
from backend.apis.base import api_router
from backend.apps.base import app_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import FileResponse
load_dotenv()


def include_router(app: FastAPI):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app: FastAPI):
    if os.path.exists("backend/static"):
        app.mount("/static", StaticFiles(directory='backend/static'), name='static')
    else:
        print("Static directory not found")

def configure_mediafiles(app: FastAPI):
    if os.path.exists("backend/media"):
        app.mount("/media", StaticFiles(directory='backend/media'), name='media')
    else:
        print("Media directory not found")

def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE)
    
    # Add SessionMiddleware
    app.add_middleware(
        SessionMiddleware,
        secret_key=os.getenv("SECRET_KEY", "default-secret-key"),
    )
    
    include_router(app)
    configure_staticfiles(app)
    configure_mediafiles(app)
    return app


app = start_application()


@app.get("/")
def root():
    return {"msg": "Welcome to the FastAPI Boutique"}
@app.get('/about')
def about():
    return FileResponse("backend/static/static_templates/about.html")

@app.get('/blog')
def about():
    return FileResponse("backend/static/static_templates/blog.html")

@app.get('/contact')
def about():
    return FileResponse("backend/static/static_templates/contact_us.html") 

# .\venv\Scripts\activate
#  uvicorn main:app --reload --port 8001
