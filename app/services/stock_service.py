import logging
from fastapi import HTTPException
from starlette import status
from app.utils.calculations import calculate_stock_metrics
import yfinance as yf


logger = logging.getLogger(__name__)
_cache = {}

def get_stock_data(ticker: str):

    ticker = ticker.strip().upper()

    if ticker in _cache:
        logger.info("Cache hit for ticker %s", ticker)
        return _cache[ticker]

    logger.info("Fetching stock data for ticker %s", ticker)

    try:
        stock = yf.Ticker(ticker)
        
        df = stock.history(period="1mo")
        if df.empty:
            logger.warning("No stock data found for ticker %s", ticker)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Stock data not found"
                                )
        metrics = calculate_stock_metrics(df)
        _cache[ticker] = metrics

        return metrics

    except HTTPException:
        raise

    except Exception as e:
        logger.warning("Unexpected server error while fetching ticker %s", ticker)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e)
                            )