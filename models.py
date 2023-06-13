from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Currency(Base):
    __tablename__ = 'currency'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tiker: Mapped[str] = mapped_column(nullable=False)
    index_price: Mapped[float] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
