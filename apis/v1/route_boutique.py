from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBoutique, ShowBoutique
from db.repository.boutique import create_new_boutique
import os
from uuid import uuid4


router = APIRouter()


@router.post("/",response_model=ShowBoutique,status_code=status.HTTP_201_CREATED)
def create_boutique(boutique: CreateBoutique, db:Session = Depends(get_db)):
    boutique = create_new_boutique(boutique = boutique,db=db,author_id=1)
    return boutique
     