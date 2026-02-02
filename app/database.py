from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
import os

# -------------------------------------------------------------------
# Database URL
# -------------------------------------------------------------------
# Prefer environment variable; fallback is optional.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/modbus_sim"
)

# -------------------------------------------------------------------
# Async SQLAlchemy engine (recommended for FastAPI)
# -------------------------------------------------------------------
engine = create_async_engine(
    DATABASE_URL,
    echo=False,          # set True for SQL debugging
    future=True
)

# -------------------------------------------------------------------
# Session factory
# -------------------------------------------------------------------
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
    future=True
)

# -------------------------------------------------------------------
# Base class for all models
# -------------------------------------------------------------------
Base = declarative_base()

# -------------------------------------------------------------------
# FastAPI dependency
# -------------------------------------------------------------------
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
