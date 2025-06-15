from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate
from backend.db.models.user import User
from backend.core.hashing import Hasher
from fastapi import HTTPException, status
def create_new_user(user: UserCreate, db: Session):
    # Validate passwords
    password_validation = Hasher.validate_passwords(
        user.password, 
        user.confirm_password
    )
    
    # If passwords are not valid, raise an exception
    if not password_validation["is_valid"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="\n".join(password_validation["errors"])
        )
    
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.username == user.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already exists"
        )
    
    # Create user with only password hashed
    new_user = User(
        username=user.username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        confirm_password=Hasher.get_password_hash(user.confirm_password),
        is_active=True
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user