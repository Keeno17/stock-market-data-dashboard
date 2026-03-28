from pydantic import BaseModel

class StockMetrics(BaseModel):
    avg_price: float
    max_price: float
    min_price: float
    latest_price: float
    pct_change: float


class StockSummary(BaseModel):
    ticker: str
    metrics: StockMetrics