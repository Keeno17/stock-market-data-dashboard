# Stock Market Data Dashboard

FastAPI-based backend for analysing stock market data using Pandas.

## Structure

stock-market-dashboard/  
│  
├── app/  
│   ├── main.py  
│   │  
│   ├── api/  
│   │   └── routes/  
│   │       └── stocks.py  
│   │  
│   ├── core/  
│   │   ├── config.py  
│   │   └── logging.py  
│   │  
│   ├── models/  
│   │   └── stock.py  
│   │  
│   ├── services/  
│   │   └── stock_service.py  
│   │  
│   └── utils/  
│       └── calculations.py  
│  
└── run.py  

## Endpoints
- */{ticker}/summary*: stock summary metrics
- */{ticker}/history*: stock History data analysis

## Sample requests/responses
- Summary request:
    **http://127.0.0.1:8000/stocks/AAPL/summary**  
- Summary response:  
    {  
      "ticker": "AAPL",  
      "metrics": {
        "avg_price": 255.3759994506836,  
        "max_price": 264.7200012207031,  
        "min_price": 247.99000549316406,  
        "latest_price": 248.8000030517578,  
        "pct_change": -6.013900761383137  
      }  
    }  

- History request:
    **http://127.0.0.1:8000/stocks/AAPL/history**  
- History response:  
    {  
      "ticker": "AAPL",  
      "history": [  
        {  
          "date": "2026-03-02",  
          "open": 262.4100036621094,  
          "high": 266.5299987792969,  
          "low": 260.20001220703125,  
          "close": 264.7200012207031,  
          "volume": 41827900  
        },  
        {  
          "date": "2026-03-03",  
          "open": 263.4800109863281,  
          "high": 265.55999755859375,  
          "low": 260.1300048828125,  
          "close": 263.75,  
          "volume": 38568900  
        }, ...  
      ]  
    }  

## Caching
- Local caching
- Divided into 2 local variables:
  - **_summary_cache**
  - **_history_cache**
- Used to prevent yahoo finance rate limiting

## Testing
- Test case 1: Valid stock summary
- Test case 2: Valid stock history
- Test case 3: Invalid ticker

## Tech Stack
- FastAPI
- Pandas
- yfinance

## Run Locally
```bash
uvicorn app.main:app --reload
