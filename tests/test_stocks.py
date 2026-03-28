from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stock_summary():
    response = client.get("/stocks/AAPL/summary")
    assert response.status_code == 200
    assert "metrics" in response.json()

def test_stock_history():
    response = client.get("/stocks/APPL/history")
    assert response.status_code == 200

def test_invalid_ticker():
    response = client.get("/stocks/INVALIDTICKER/summary")
    assert response.status_code in [404, 500]
