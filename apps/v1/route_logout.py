
import json
from fastapi import APIRouter,Request,Depends,responses,status,Form,HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from backend.db.session import get_db
from backend.schemas.user import UserCreate
from backend.apis.v1.route_login import login_user
from pydantic import ValidationError

from backend.db.repository.boutique import list_boutique,retrieve_boutique

templates = Jinja2Templates(directory="backend/templates")
router = APIRouter()

from starlette.middleware.sessions import SessionMiddleware




@router.get("/logout/", name="logout")
async def logout_user(request: Request):
    # Clear session
    request.session.clear()

    # Pass empty username and redirect
    response = RedirectResponse(url="/home", status_code=302)
    response.set_cookie(key="username", value="")
    return response