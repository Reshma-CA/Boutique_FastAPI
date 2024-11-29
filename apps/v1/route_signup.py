import json
from fastapi import APIRouter,Request,Depends,responses,status,Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.user import UserCreate
from db.repository.signup import create_new_user
from pydantic.error_wrappers import ValidationError


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/signup")
def signup(request:Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})

@router.post("/signup")
def signup(request:Request,username:str = Form(...),email:str = Form(...),
           password:str = Form(...),confirm_password:str = Form(...),db:Session = Depends(get_db)):
    errors = []
    try:
        user = UserCreate(username=username,email=email,password=password,confirm_password=confirm_password)
        create_new_user(user=user,db=db)
        return templates.TemplateResponse("auth/login.html", {"request": request})

    except ValidationError as e:
        error_list = json.loads(e.json())
        for item in error_list:
            errors.append(item.get("loc")[0]+":"+ item.get("msg"))
        return templates.TemplateResponse("auth/signup.html", {"request": request, "errors": errors})