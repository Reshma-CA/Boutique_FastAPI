from typing import List
from fastapi import APIRouter, Depends, status, File, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBoutique, ShowBoutique,UpdateBoutique
from db.repository.boutique import create_new_boutique,retrieve_boutique,list_boutique,update_boutique_by_id,delete_boutique_by_id
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

@router.get("/{id}",response_model=ShowBoutique,status_code=status.HTTP_200_OK)
def get_blog(id:int,db:Session = Depends(get_db)):
    get_boutique = retrieve_boutique(id=id,db=db)
    if not get_boutique:
        raise HTTPException(status_code=404, detail=f"Boutique with {id } does not found")
    return get_boutique


@router.get('', response_model=List[ShowBoutique],status_code=status.HTTP_200_OK)
def get_all_boutique(db:Session = Depends(get_db)):
    get_boutique = list_boutique(db=db)
    return get_boutique

@router.put("/{id}", response_model=ShowBoutique, status_code=status.HTTP_200_OK)
async def update_a_boutique(
    id: int,
    title: str = Form(None),
    slug: str = Form(None),
    content: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # First, retrieve the existing boutique
    existing_boutique = retrieve_boutique(id=id, db=db)
    if not existing_boutique:
        raise HTTPException(status_code=404, detail=f"Boutique with id {id} not found")

    # Handle image upload
    dress_picture = existing_boutique.dress_picture
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
            
            # Delete the old image if it exists
            if existing_boutique.dress_picture and os.path.exists(existing_boutique.dress_picture):
                os.remove(existing_boutique.dress_picture)
            
            dress_picture = file_path
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
    
    # Prepare update data
    update_data = UpdateBoutique(
        title=title or existing_boutique.title, 
        slug=slug or existing_boutique.slug, 
        content=content or existing_boutique.content, 
        dress_picture=dress_picture
    )
    
    # Update the boutique
    updated_boutique = update_boutique_by_id(id=id, boutique=update_data, db=db, author_id=1)
    return updated_boutique

@router.delete("/{id}")
def delete_a_boutique(id:int,db:Session = Depends(get_db)): 
    message = delete_boutique_by_id(id=id, db=db, author_id=1)
    if message.get('error'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message.get('error'))
    return {"msg":message.get('msg')}