from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import TradeDB
from schemas import Trade

router = APIRouter()

@router.get("/trade-history", response_model=List[Trade])
def get_trade_history(db: Session = Depends(get_db)):
    return db.query(TradeDB).all()
