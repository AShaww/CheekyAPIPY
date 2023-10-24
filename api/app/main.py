import uvicorn
from fastapi import FastAPI
from api.app import models
from api.app.db.database import engine, SessionLocal

from api.app.routers import user, issues, posts, todos
from auth import auth

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(posts.router)
app.include_router(todos.router)
app.include_router(issues.router)
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    uvicorn.run('api.app.main:app', port=8000, reload=True)
