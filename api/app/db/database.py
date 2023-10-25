from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.app import config


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.engine = create_engine(config.DATABASE_URL)
            cls._instance.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
            cls._instance.Base = declarative_base()
        return cls._instance


db_manager = DatabaseManager()

engine = db_manager.engine
SessionLocal = db_manager.SessionLocal
Base = db_manager.Base
