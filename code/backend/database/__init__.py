from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file located in the backend directory
load_dotenv(Path(__file__).resolve().parent / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database/test.db")

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
