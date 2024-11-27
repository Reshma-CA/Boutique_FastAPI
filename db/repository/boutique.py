from sqlalchemy.orm import Session
from schemas.blog import CreateBoutique
from db.models.boutique import Boutique
from typing import Optional

from fastapi import UploadFile, File
import shutil

def create_new_boutique(boutique:CreateBoutique,db:Session,author_id:int = 1):
    boutique = Boutique(
        title = boutique.title,
        slug =  boutique.slug,
        content=boutique.content,
        author_id = author_id

    )
    db.add(boutique)
    db.commit()
    db.refresh(boutique)
    return boutique
