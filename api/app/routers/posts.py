from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from api.app import models as m
from api.app.auth.auth import db_dependency

router = APIRouter(
    prefix="/posts",
    tags=["post"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: m.PostBase, db: db_dependency):
    db_post = m.Post(**post.model_dump())
    db.add(db_post)
    db.commit()


@router.get("/{post_id}", status_code=status.HTTP_200_OK)
async def get_post(post_id: int, db: db_dependency):
    post = db.query(m.Post).filter(m.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    return post


@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(m.Post).filter(m.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()
