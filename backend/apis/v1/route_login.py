from fastapi import APIRouter, Depends,status,HTTPException,Request
from typing import Dict
from sqlalchemy.orm import Session


from backend.core.hashing import Hasher
from backend.schemas.user import UserCreate,ShowUser
from backend.db.session import get_db
from backend.db.repository.login import get_user_by_email


router = APIRouter()



@router.post("/")
async def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_email(email=email, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email")
    if not Hasher.verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    # Set session or return token (if implementing JWT)
    return {"msg": "Login successful", "username": user.username}



def get_current_user(request: Request, db: Session = Depends(get_db)) -> ShowUser:
    # Retrieve the user's email from the session
    user_email = request.session.get("user_email")
    if not user_email:
        raise HTTPException(status_code=401, detail="User not logged in")
    
    # Fetch user details from the database
    user = get_user_by_email(email=user_email, db=db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
async def login_user(
    email: str, 
    password: str, 
    db: Session = Depends(get_db)) -> Dict[str, str]:
    # Find user by email
    user = get_user_by_email(email=email, db=db)
    
    # Check if user exists
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid email"
        )
    
    # Verify password
    if not Hasher.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid password"
        )
    
    # Return successful login response
    return {"msg": "Login successful", "username": user.username}