from sqlalchemy.orm import Session
from backend.schemas.blog import CreateBoutique,UpdateBoutique
from backend.db.models.boutique import Boutique

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

def update_boutique_by_id(id:int, boutique:UpdateBoutique, db:Session, author_id:int=1): 
    boutique_in_db = db.query(Boutique).filter(Boutique.id == id).first()

    if not boutique_in_db:
        return {"error" :f"Boutique with id {id} does not exist"}
    if not boutique_in_db.author_id == author_id:
        return {"error":f"Only the author can modify the boutique content"}

    
    # Update fields only if they are provided
    boutique_in_db.title = boutique.title 
    
    if boutique.content is not None:
        boutique_in_db.content = boutique.content
    
    if boutique.dress_picture is not None:
        boutique_in_db.dress_picture = boutique.dress_picture
    
    # Update slug, using existing or generating a new one
    boutique_in_db.slug = boutique.slug or boutique.title.lower().replace(' ', '-')
    
    db.add(boutique_in_db)
    db.commit()
    db.refresh(boutique_in_db)
    return boutique_in_db


def delete_boutique_by_id(id:int, db:Session,author_id:int):
    boutique_to_delete = db.query(Boutique).filter(Boutique.id == id)
    
    if not boutique_to_delete.first():
        return {"error": f"Could not find Boutique with id {id} in database"}
    if not boutique_to_delete.first().author_id == author_id:
        return {"error": "Only the author can delete the boutique"}
    
    boutique_to_delete.delete()
    db.commit()
    return {"msg": f"Deleted blog with id {id} in database"}