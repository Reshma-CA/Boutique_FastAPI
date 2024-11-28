from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/signup")
def signup(request:Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})