import json
from fastapi import APIRouter,Request,Depends,responses,status,Form,HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from db.session import get_db
from schemas.user import UserCreate
from apis.v1.route_login import login_user
from pydantic.error_wrappers import ValidationError

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/login")
def login(request:Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # Call the login_user function from the API route
        result = await login_user(email=email, password=password, db=db)
        print(result)
        
        # If login is successful, render home template
        return templates.TemplateResponse(
            "boutique/home.html", 
            {"request": request, "username": result['username']} 
        )
    
    except HTTPException as e:
        # If login fails, return to login page with error
        errors = [e.detail]
        return templates.TemplateResponse(
            "auth/login.html", 
            {"request": request, "error": errors}
        )
    
@router.get("/logout/", name="logout")
async def logout_user(request: Request):
    request.session.clear()
    return templates.TemplateResponse(
        "boutique/index.html", {"request": request}
    )
