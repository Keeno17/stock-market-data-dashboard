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
