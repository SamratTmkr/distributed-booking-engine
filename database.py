# accessing env
import os 
from dotenv import load_dotenv

from sqlalchemy import text
# database.pt
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
# accessing env

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo = True
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession,expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

async def test_conn():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("database conn:",result.scalars())