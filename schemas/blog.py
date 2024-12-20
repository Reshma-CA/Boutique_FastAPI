from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class CreateBoutique(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None
    dress_picture: Optional[str] = None  # Now accepts file path

    # Generate slug after validating other fields
    @field_validator("slug", mode="after")
    def generate_slug(cls, slug, values):
        # Automatically generate slug if not provided
        if slug is None and values.get("title"):
            return values["title"].lower().replace(' ', '-')
        return slug

class UpdateBoutique(CreateBoutique):
    pass

class ShowBoutique(BaseModel):
    title: str
    content: Optional[str]
    dress_picture: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True