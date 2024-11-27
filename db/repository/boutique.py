from sqlalchemy.orm import Session
from schemas.blog import CreateBoutique
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

