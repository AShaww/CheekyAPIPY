from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from api.app.db.database import Base


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(500))


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    title = Column(String(50))
    content = Column(String(100))


class PostBase(BaseModel):
    user_id: int
    title: str
    content: str


class UserBase(BaseModel):
    username: str
