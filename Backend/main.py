from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File, Form
from pydantic import  BaseModel
from typing import Annotated, Optional
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import util



app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# class PostCreate(BaseModel):
#     project_name: str
#     description: str

class Post(BaseModel):
    id: int
    project_name: str
    description: str 
    image_path: Optional[str] = None
    video_path: Optional[str] = None

    class config:
        orm_mode = True

class User(BaseModel):
    user_id: int
    username: str
    password: str

def get_db():
    db = SessionLocal()
    return db
    

db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/projects/",status_code= status.HTTP_201_CREATED, response_model=Post)
async def create_project(
    
    project_name: str = Form(),
    description: str = Form(), 
    
    image:UploadFile = Form(), #File(None)
    video:UploadFile = Form()#File(None)

):
    print("working")
    image_path = None
    video_path = None

    if image:
        image_path = util.save_file(image, "image")
    if video:
        video_path = util.save_file(video, "video")

    db_project = models.Post(
        project_name=project_name,
        description=description,
        image_path=image_path,
        video_path=video_path
    )
    db = get_db()
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
    
