from pydantic import BaseModel
from datetime import datetime
from typing import List

class TradeBase(BaseModel):
    user_id: int
    symbol: str
    action: str
    quantity: int
    price: float
    timestamp: datetime

    class Config:
        orm_mode = True

class Trade(TradeBase):
    id: int
