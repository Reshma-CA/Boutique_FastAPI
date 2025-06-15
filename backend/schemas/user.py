from pydantic import BaseModel,EmailStr,Field


class UserCreate(BaseModel):
    username: str = Field(...,min_length=4)
    email: EmailStr
    password: str = Field(...,min_length=4)
    confirm_password: str = Field(...,min_length=4)


class ShowUser(BaseModel):
    id:int
    username: str
    email:EmailStr
    is_active:bool
    
    class Config():
        from_attributes  = True