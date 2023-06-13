from typing import AsyncGenerator

import os

from dotenv import load_dotenv
from sqlalchemy.ext import asyncio as sea
from sqlalchemy.orm import sessionmaker


load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB = os.getenv('POSTGRES_DB')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
)

engine = sea.create_async_engine(
    url=SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=sea.AsyncSession,
)


async def get_async_session() -> AsyncGenerator[sea.AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
