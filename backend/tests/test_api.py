import pytest
from fastapi.testclient import TestClient
from backend.main import app  # adjust import if needed

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_prediction_endpoint():
    payload = {
        "timestamp": "2026-01-01 09:00:00",
        "usage_liters": 4.0
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "leak_probability" in data
    assert 0.0 <= data["leak_probability"] <= 1.0
    assert "risk_level" in data


def test_invalid_input():
    payload = {
        "timestamp": "invalid-date",
        "usage_liters": -5
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422
