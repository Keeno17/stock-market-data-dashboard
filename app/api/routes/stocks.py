from app.schemas.stock import StockSummary
from fastapi import APIRouter
from starlette import status
from app.services.stock_service import get_stock_data

router = APIRouter()

@router.get("/{ticker}", response_model=StockSummary, status_code=status.HTTP_200_OK)
def read_stock(ticker: str):
    clean_ticker = ticker.strip().upper()
    metrics = get_stock_data(clean_ticker)
    return {"ticker": clean_ticker, 
            "metrics": metrics}