from fastapi import APIRouter, Depends, status, File, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBoutique, ShowBoutique
from db.repository.boutique import create_new_boutique
import os
from uuid import uuid4

router = APIRouter()

# Ensure upload directory exists
UPLOAD_DIRECTORY = "media/images"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@router.post("/", response_model=ShowBoutique, status_code=status.HTTP_201_CREATED)
async def create_boutique(
    title: str = Form(...),
    slug: str = Form(None),
    content: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Handle image upload
    dress_picture = None
    if image:
        # Validate file type
        allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        if image.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
        
        # Generate unique filename
        file_extension = image.filename.split('.')[-1]
        unique_filename = f"{uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
        
        # Save the file
        try:
            contents = await image.read()
            with open(file_path, 'wb') as f:
                f.write(contents)
            dress_picture = file_path
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
    
    # Create boutique with image path
    boutique_data = CreateBoutique(
        title=title, 
        slug=slug, 
        content=content, 
        dress_picture=dress_picture
    )
    
    boutique = create_new_boutique(boutique=boutique_data, db=db, author_id=1)
    return boutique