import enum
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, func, text
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


class IssueStatus(enum.Enum):
    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_PROGRESS'
    CLOSED = 'CLOSED'


class Issue(Base):
    __tablename__ = 'issues'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False, server_default=text('"OPEN"'))
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=func.current_timestamp(),
    )


class PostBase(BaseModel):
    user_id: int
    title: str
    content: str


class UserBase(BaseModel):
    username: str
