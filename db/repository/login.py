from sqlalchemy.orm import Session
from db.models.user import User
from fastapi import APIRouter, HTTPException,status

def get_user_by_email(email:str, db:Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=" No user found with this email !!!"
        )
    
    return user