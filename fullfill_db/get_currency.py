import aiohttp

from datetime import datetime

from database import SessionLocal
from models import Currency


async def get_btc():
    async with aiohttp.ClientSession() as cl_session:
        try:
            async with cl_session.get(
                'https://test.deribit.com/api/v2/public/get_index_price'
                '?index_name=btc_usd'
            ) as resp:
                res = await resp.json()
                date = datetime.fromtimestamp(res['usIn'] / 1000000)
                currency_instance = Currency(
                    tiker='BTC',
                    index_price=res['result']['index_price'],
                    date=date
                )
                async with SessionLocal() as session:
                    session.add(currency_instance)
                    await session.commit()
        except Exception:
            pass


async def get_eth():
    async with aiohttp.ClientSession() as cl_session:
        try:
            async with cl_session.get(
                'https://test.deribit.com/api/v2/public/get_index_price'
                '?index_name=eth_usd'
            ) as resp:
                res = await resp.json()
                date = datetime.fromtimestamp(res['usIn'] / 1000000)
                currency_instance = Currency(
                    tiker='ETH',
                    index_price=res['result']['index_price'],
                    date=date
                )
                async with SessionLocal() as session:
                    session.add(currency_instance)
                    await session.commit()
        except Exception:
            pass
