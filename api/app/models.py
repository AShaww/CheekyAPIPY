from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from api.app.db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)


class Post(Base):
    __tablename__ = 'posts'

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
