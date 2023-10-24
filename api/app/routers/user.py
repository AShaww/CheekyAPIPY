from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from api.app import models as m
from api.app.auth.auth import db_dependency, user_dependency

router = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router.get('/me')
async def user_index(user_auth: user_dependency, db: db_dependency):
    if user_auth is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user_auth}


@router.get('/users/{user_id}', status_code=status.HTTP_200_OK)
async def read_get_user(user_auth: user_dependency, user_id: int, db: db_dependency):
    user = db.query(m.UserBase).filter(user_id == m.Users.id).first()
    if user_auth is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user
