from datetime import datetime

from pydantic import BaseModel


class CurrencyData(BaseModel):
    id: int
    tiker: str
    index_price: float
    date: datetime

    class Config:
        orm_mode = True
