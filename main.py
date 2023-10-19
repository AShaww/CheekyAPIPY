# import uvicorn
#
# if __name__ == '__main__':
#     uvicorn.run('app.app:app', port=8000, reload=True)
import uvicorn
from app.app import app  # Import the FastAPI app from app/app.py

if __name__ == '__main__':
    uvicorn.run('app.app:app', port=8000, reload=True)
