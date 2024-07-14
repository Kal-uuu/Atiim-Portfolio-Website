from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "Login_details"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

class Post(Base):
    __tablename__ = "Project_details"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(255))
    description = Column(String(5000))
    image_path = Column(String(255), nullable=True)
    video_path = Column(String(255), nullable=True)



