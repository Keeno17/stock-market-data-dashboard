from pydantic import BaseModel
from typing import List

class StockMetrics(BaseModel):
    avg_price: float
    max_price: float
    min_price: float
    latest_price: float
    pct_change: float


class StockSummary(BaseModel):
    ticker: str
    metrics: StockMetrics

class StockTradingDay(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int


class StockHistory(BaseModel):
   ticker: str
   history: List[StockTradingDay]
