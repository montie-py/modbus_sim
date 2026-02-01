from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
import os


# ---------------------------------------------------------
# Database URL
# ---------------------------------------------------------

# Example:
# postgresql://user:password@localhost:5432/mydb
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/app")


# ---------------------------------------------------------
# SQLAlchemy engine
# ---------------------------------------------------------

# NullPool is useful in FastAPI to avoid connection reuse issues in dev
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    poolclass=NullPool
)


# ---------------------------------------------------------
# Session factory
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ---------------------------------------------------------
# Base class for models
# ---------------------------------------------------------

Base = declarative_base()


# ---------------------------------------------------------
# Dependency for FastAPI routes
# ---------------------------------------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
