from fastapi import APIRouter, HTTPException
from starlette import status
from api.app import models as m
from api.app.auth.auth import db_dependency, user_dependency

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get('/me')
async def user_profile(user_auth: user_dependency):
    if user_auth is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {"User": user_auth}


@router.get('/{user_id}', response_model=m.UserBase, status_code=status.HTTP_200_OK)
async def read_get_user(user_auth: user_dependency, user_id: int, db: db_dependency):
    user = db.query(m.Users).filter(m.Users.id == user_id).first()
    if user_auth is None:
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
    return user
