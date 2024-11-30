
import json
from fastapi import APIRouter,Request,Depends,responses,status,Form,HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from db.session import get_db
from schemas.user import UserCreate
from apis.v1.route_login import login_user
from pydantic.error_wrappers import ValidationError
from db.repository.boutique import list_boutique,retrieve_boutique

templates = Jinja2Templates(directory="templates")
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