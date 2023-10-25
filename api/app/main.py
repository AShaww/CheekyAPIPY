import uvicorn
from fastapi import FastAPI

from api.app.db.database import engine
from api.app.db.db_utils import get_db
from api.app import models
from auth import auth
from api.app.routers import user, issues, posts, todos


app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(posts.router)
app.include_router(todos.router)
app.include_router(issues.router)

models.Base.metadata.create_all(bind=engine)
get_db()


if __name__ == '__main__':
    uvicorn.run('api.app.main:app', port=8000, reload=True)
