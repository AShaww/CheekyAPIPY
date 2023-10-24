import os
import sys
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    sys.exit("ERROR: DATABASE_URL is not set.")

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    sys.exit("ERROR: SECRET_KEY is not set.")
