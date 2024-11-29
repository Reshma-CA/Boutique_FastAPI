from fastapi import APIRouter
from fastapi import Request,Depends, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.boutique import list_boutique,retrieve_boutique
from db.session import get_db
from typing import Optional



templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    all_boutique = list_boutique(db=db)
    context = {"request": request,"all_boutique": all_boutique}
    return templates.TemplateResponse("boutique/home.html",context = context ) # what is meta data


@router.get("/app/boutique/{id}")
def boutique_detail(request: Request, id: int, db: Session = Depends(get_db)):
    boutique_detail = retrieve_boutique(id=id, db=db)
    if not boutique_detail:
        raise HTTPException(status_code=404, detail="Boutique item not found")
    return templates.TemplateResponse(
        "boutique/detail.html", {"request": request, "boutique_detail": boutique_detail}
    )

