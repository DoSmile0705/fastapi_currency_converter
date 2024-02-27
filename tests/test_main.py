from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_update_exchange_rates():
    response = client.get("/update_exchange_rates")
    assert response.status_code == 200
    assert response.json() == {"message": "Exchange rates updated successfully"}


def test_last_update():
    response = client.get("/last_update")
    assert response.status_code == 200
    assert "last_updated" in response.json()[0]


def test_convert_currency():
    response = client.post("/convert", json={"source": "USD", "target": "EUR", "amount": 100})
    assert response.status_code == 200
    assert "result" in response.json()
