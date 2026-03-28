import logging
from fastapi import HTTPException
from starlette import status
from app.utils.calculations import calculate_stock_metrics
import yfinance as yf


logger = logging.getLogger(__name__)
_summarycache = {}
_historycache = {}

def get_stock_summary(ticker: str):

    ticker = ticker.strip().upper()

    if ticker in _summarycache:
        logger.info("Cache hit for ticker %s", ticker)
        return _summarycache[ticker]

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
        _summarycache[ticker] = metrics
        return metrics

    except HTTPException:
        raise
    except Exception as e:
        logger.warning("Unexpected server error while fetching ticker %s", ticker)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e)
                            )

def get_stock_history(ticker: str):
    ticker = ticker.strip().upper()

    if ticker in _historycache:
        logger.info("Cache hit for ticker %s", ticker)
        return _historycache[ticker]

    logger.info("Fetching stock history for ticker %s", ticker)

    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1mo")
        if df.empty:
            logger.warning("No stock history found for ticker %s", ticker)
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Stock history not found"
                                )
        
        _historycache[ticker] = df
        return df

    except HTTPException:
        raise
    except Exception as e:
        logger.warning("Unexpected server error while fetching history for ticker %s", ticker)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e)
                            )