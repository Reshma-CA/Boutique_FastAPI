from sqlalchemy.orm import Session
from schemas.blog import CreateBoutique,UpdateBoutique
from db.models.boutique import Boutique

def create_new_boutique(boutique: CreateBoutique, db: Session, author_id: int = 1):
    boutique_model = Boutique(
        title=boutique.title,
        slug=boutique.slug or boutique.title.lower().replace(' ', '-'),
        content=boutique.content,
        dress_picture=boutique.dress_picture,  # Store the image path
        author_id=author_id
    )
    db.add(boutique_model)
    db.commit()
    db.refresh(boutique_model)
    return boutique_model

def retrieve_boutique(id:int, db:Session):
    boutique_get = db.query(Boutique).filter(Boutique.id == id).first()
    return boutique_get

def list_boutique(db:Session):
    boutiques = db.query(Boutique).filter(Boutique.is_active == True).all()
    return boutiques

def update_boutique_by_id(id:int,boutique:UpdateBoutique,db:Session,author_id:int=1): 
    bloutique_in_db = db.query(Boutique).filter(Boutique.id == id).first()

    if not bloutique_in_db:
        return None
    
    bloutique_in_db.title = boutique.title 
    bloutique_in_db.content = boutique.content
    bloutique_in_db.dress_picture = boutique.dress_picture  # Update the image path
    db.add(bloutique_in_db)
    db.commit()
    return bloutique_in_db