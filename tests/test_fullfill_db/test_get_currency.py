import pytest

from sqlalchemy import select
from sqlalchemy.ext import asyncio as sea

from fullfill_db.get_currency import get_btc, get_eth
from models import Currency


@pytest.mark.asyncio
async def test_get_currency(
    async_session: sea.AsyncSession
) -> None:
    await get_btc()
    result = await async_session.execute(select(Currency))
    assert result.scalar_one_or_none is not None
    await get_eth()
    result = await async_session.execute(select(Currency).where(
        Currency.tiker == 'ETH'
    ))
    assert result.scalar_one_or_none is not None
