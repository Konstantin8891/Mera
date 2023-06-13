from datetime import datetime
from typing import List, Any

from fastapi import Depends, APIRouter
from sqlalchemy.ext import asyncio as sea

from crud import (
    get_all_currencies_crud,
    get_last_currency_crud,
    get_currency_by_date_crud
)
from database import get_async_session
from schemas import CurrencyData


router = APIRouter(prefix='', tags=['main'])


@router.get('/get_all_currencies', response_model=List[CurrencyData])
# @router.get('/get_all_currencies')
async def get_all_currencies(
    tiker: str,
    session: sea.AsyncSession = Depends(get_async_session)
) -> Any:
    return await get_all_currencies_crud(tiker, session)


@router.get('/get_last_currency', response_model=CurrencyData)
async def get_last_currency(
    tiker: str,
    session: sea.AsyncSession = Depends(get_async_session)
) -> Any:
    return await get_last_currency_crud(tiker, session)


@router.get('/get_currency_by_date', response_model=List[CurrencyData])
async def get_currency_by_date(
    tiker: str,
    date_start: datetime = None,
    date_end: datetime = None,
    session: sea.AsyncSession = Depends(get_async_session)
) -> Any:
    return await get_currency_by_date_crud(
        tiker, date_start, date_end, session
    )
