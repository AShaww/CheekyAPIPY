import enum
from datetime import datetime, timezone

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, func, text, event
from api.app.db.database import Base


class IssueStatus(enum.Enum):
    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_PROGRESS'
    CLOSED = 'CLOSED'


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(500))


class Issue(Base):
    __tablename__ = 'issues'
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False, server_default=text('"OPEN"'))
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, onupdate=func.current_timestamp())


@event.listens_for(Issue, 'before_insert')
def set_created_at(_mapper, _connection, target):
    now = datetime.now(timezone.utc)
    target.created_at = now
    target.updated_at = now


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


class IssueBase(BaseModel):
    title: str
    description: str
    status: IssueStatus
