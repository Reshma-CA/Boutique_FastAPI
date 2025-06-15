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


@router.get("/home/", name="homepage")
async def homepage(request: Request, db: Session = Depends(get_db)):
    all_boutique = list_boutique(db=db)
    print(f"Fetched boutiques: {all_boutique}")  # Debugging
    context = {"request": request, "all_boutique": all_boutique}
    return templates.TemplateResponse("boutique/home.html", context=context)




# @router.get("/home/", name="homepage")
# async def homepage(request: Request, db: Session = Depends(get_db)):
#     all_boutique = list_boutique(db=db)
#     context = {"request": request,"all_boutique": all_boutique}
#     return templates.TemplateResponse("boutique/index.html", context = context )
