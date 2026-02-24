from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, String

from week_2.day_2.infrastructure.database import Base


class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)