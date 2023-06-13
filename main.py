from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from fullfill_db.get_currency import get_btc, get_eth
from routers import main_router


app = FastAPI()

app.include_router(main_router.router)

scheduler = AsyncIOScheduler()
scheduler.add_job(get_btc, "interval", seconds=60)
scheduler.add_job(get_eth, "interval", seconds=60)
scheduler.start()
