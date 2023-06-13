from datetime import datetime
from typing import Union

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext import asyncio as sea

from models import Currency


async def get_all_currencies_crud(tiker: str, session: sea.AsyncSession):
    result = await session.execute(select(Currency).where(
        Currency.tiker == tiker
    ))
    return result.scalars().all()


async def get_last_currency_crud(
    tiker: str,
    session: sea.AsyncSession
) -> dict[str, Union[str, datetime, float]]:
    result = await session.execute(select(Currency).where(
        Currency.tiker == tiker
    ).order_by(Currency.id.desc()))
    return result.scalar()


async def get_currency_by_date_crud(
    tiker: str,
    date_start: datetime,
    date_end: datetime,
    session: sea.AsyncSession
) -> dict[str, Union[str, datetime, float]]:
    if not date_end and not date_start:
        raise HTTPException(
            detail='At least one date should be specified', status_code=404
        )
    if date_start and date_end:
        result = await session.execute(select(Currency).where(
            Currency.tiker == tiker
        ).where(Currency.date > date_start.replace(tzinfo=None)).where(
            Currency.date < date_end.replace(tzinfo=None)
        ))
    elif date_start:
        result = await session.execute(select(Currency).where(
            Currency.tiker == tiker
        ).where(Currency.date > date_start.replace(tzinfo=None)))
    else:
        result = await session.execute(select(Currency).where(
            Currency.tiker == tiker
        ).where(Currency.date < date_end.replace(tzinfo=None)))
    return result.scalars().all()
