import uvicorn
from http.client import HTTPException
from fastapi import FastAPI, Depends, status
from typing import Annotated
from api.app import models
from api.app.db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from auth import auth

app = FastAPI()

app.include_router(auth.router)


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/', tags=['root'])
async def user(user: None, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return {'Ping=': 'Pong', 'Hello': 'World'}


# @app.post("/users/", status_code=status.HTTP_201_CREATED, tags=['users'])
# async def create_user(user: models.UserBase, db: db_dependency):
#     db_user = models.Users(**user.model_dump())
#     db.add(db_user)
#     db.commit()


@app.get('/users/{user_id}', status_code=status.HTTP_200_OK, tags=['users'])
async def read_get(user_id: int, db: db_dependency):
    user = db.query(models.Users).filter(user_id == models.Users.id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

#
# @app.post("/posts/", status_code=status.HTTP_201_CREATED, tags=['posts'])
# async def create_post(post: models.PostBase, db: db_dependency):
#     db_post = models.Post(**post.model_dump())
#     db.add(db_post)
#     db.commit()
#
#
# @app.get("/posts/{post_id}", status_code=status.HTTP_200_OK, tags=['posts'])
# async def get_post(post_id: int, db: db_dependency):
#     post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if post is None:
#         raise HTTPException(status_code=404, detail='Post was not found')
#     return post
#
#
# @app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency):
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail='Post was not found')
#     db.delete(db_post)
#     db.commit()
#
#
# @app.get('/todo', tags=['todos'])
# async def get_todo() -> dict:
#     return {'data': todos}
#
#
# todos = [
#     {
#         "id": "1",
#         "Activity": "Jogging for 2 hours at 7:00 AM."
#     },
#     {
#         "id": "2",
#         "Activity": "Writing 3 pages of my new book at 2:00 PM."
#     }
# ]
#
#
# @app.post('/todo', tags=['todos'])
# async def add_todo(todo: dict) -> dict:
#     todos.append(todo)
#     return {
#         'data': 'A todo has been added !'
#     }
#
#
# @app.put('/todo/{id}', tags=['todos'])
# async def update_todo(todo_id: int, body: dict) -> dict:
#     for todo in todos:
#         if int((todo['id'])) == todo:
#             todo['Activity'] = body['Activity']
#             return {
#                 'data': f"Todo with id {todo} has been updated"
#             }
#
#     return {
#         'data': f"Todo with this id number {todo_id} was not found !"
#     }
#
#
# @app.delete('/todo/{id}', tags=['todos'])
# async def delete_todo(todo_id: int) -> dict:
#     for todo in todos:
#         if int(todo["id"]) == id:
#             todos.remove(todo)
#             return {
#                 "data": f"todo with id {todo_id} has been deleted"
#             }
#
#         return {
#             'data': f"Todo with this id number {todo_id} was not found !"
#         }


if __name__ == '__main__':
    uvicorn.run('api.app.main:app', port=8000, reload=True)
