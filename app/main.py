from fastapi import FastAPI
from app.api.routes import stocks
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="Stock Market Dashboard API", version="1.0.0")

app.include_router(stocks.router, prefix="/stocks", tags=["Stocks"])