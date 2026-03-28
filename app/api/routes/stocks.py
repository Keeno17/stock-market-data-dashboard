from app.schemas.stock import StockSummary, StockHistory
from fastapi import APIRouter
from starlette import status
from app.services.stock_service import get_stock_summary, get_stock_history

router = APIRouter()

@router.get("/{ticker}/summary", response_model=StockSummary, status_code=status.HTTP_200_OK)
def read_stock_summary(ticker: str):
    clean_ticker = ticker.strip().upper()
    metrics = get_stock_summary(clean_ticker)
    return {"ticker": clean_ticker, 
            "metrics": metrics}

@router.get("/{ticker}/history", response_model=StockHistory, status_code=status.HTTP_200_OK)
def read_stock_history(ticker: str):
    clean_ticker = ticker.strip().upper()
    df = get_stock_history(clean_ticker)
    history = []
    for index, row in df.iterrows():
        history.append({
            "date": index.strftime("%Y-%m-%d"),
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"])
        })
    return {"ticker": clean_ticker,
            "history": history}