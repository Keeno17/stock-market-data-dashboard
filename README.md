# Stock Market Data Dashboard

FastAPI-based backend for analysing stock market data using Pandas.

## Structure

```text
stock-market-dashboard/  
├── app/  
│   ├── main.py  
│   ├── api/routes/stocks.py  
│   ├── core/config.py  
│   ├── core/logging.py  
│   ├── models/stock.py   
│   ├── services/stock_service.py  
│   └── utils/calculations.py  
└── run.py  
```

## Endpoints
- */{ticker}/summary*: stock summary metrics
- */{ticker}/history*: stock History data analysis

## Sample requests/responses
- Summary request:
```http
http://127.0.0.1:8000/stocks/AAPL/summary
```
- History request:
```http
http://127.0.0.1:8000/stocks/AAPL/history
```

- Summary response:
```http
{
  "ticker": "AAPL",
  "metrics": {
    "avg_price": 255.38,
    "max_price": 264.72,
    "min_price": 247.99,
    "latest_price": 248.80,
    "pct_change": -6.01
  }
}
```
- History response:
```http
{
  "ticker": "AAPL",
  "history": [
    {
      "date": "2026-03-02",
      "open": 262.41,
      "high": 266.53,
      "low": 260.20,
      "close": 264.72,
      "volume": 41827900
    },
    {
      "date": "2026-03-03",
      "open": 263.48,
      "high": 265.56,
      "low": 260.13,
      "close": 263.75,
      "volume": 38568900
    }
  ]
}
```

## Caching
- Local caching
- Divided into 2 local variables:
  - **_summary_cache**
  - **_history_cache**
- Used to prevent yahoo finance rate limiting

## Testing
The project includes the following tests covering:
- Test case 1: Valid stock summary requests
- Test case 2: Valid stock history requests
- Test case 3: Invalid ticker handling

## Tech Stack
- **Python / FastAPI** - stock service
- **Pandas** - stock calculations and summaries 
- **yfinance** - live stock information
- **pytest** - automated testing

## Run Locally
```bash
uvicorn app.main:app --reload
