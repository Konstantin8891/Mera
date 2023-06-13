import os
import pytest
import sys

from typing import Generator, AsyncGenerator

import asyncio

import pytest_asyncio

from sqlalchemy.ext import asyncio as sea
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import USER, PASSWORD, DB, HOST, PORT
from models import Base


SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}_test'
)

engine = sea.create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionTesting = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=sea.AsyncSession
)


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def _db_connection():
    async_engine = sea.create_async_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=False,
        future=True,
    )

    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
        yield conn
        await conn.run_sync(Base.metadata.drop_all)
        await conn.commit()

    await async_engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def async_session(
    _db_connection: sea.AsyncConnection
) -> AsyncGenerator:
    session = sessionmaker(
        bind=_db_connection,
        class_=sea.AsyncSession,
        expire_on_commit=False,
    )
    async with session() as s:
        yield s
        await s.rollback()
