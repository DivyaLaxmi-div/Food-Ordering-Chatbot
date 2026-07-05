"""
Database connection module.
Uses SQLite — zero installation required, works on any OS.
The database file (chatbot.db) is created automatically in the backend folder.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# -------------------------------------------------------------------
# SQLite database file — saved inside the backend folder automatically
# -------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "..", "..", "chatbot.db")
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_PATH)}"

# -------------------------------------------------------------------
# SQLAlchemy engine
# check_same_thread=False is required for SQLite with FastAPI
# -------------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,   # Set True to see SQL logs in terminal
)

# Session factory — each request gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """FastAPI dependency — provides a DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database_if_not_exists():
    """
    SQLite creates the .db file automatically — nothing to do here.
    Kept for compatibility with the startup lifespan in main.py.
    """
    pass
