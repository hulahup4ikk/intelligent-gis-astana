from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "GBI-UHI" in data["service"]


def test_layers_endpoint():
    response = client.get("/api/v1/layers")
    assert response.status_code == 200
    layers = response.json()
    assert len(layers) >= 3
    layer_ids = [l["layer_id"] for l in layers]
    assert "uhi_lst_astana" in layer_ids


def test_forecast_endpoint():
    payload = {
        "bounds": [71.3, 51.1, 71.5, 51.25],
        "resolution_meters": 30
    }
    response = client.post("/api/v1/forecast", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "simulated"
    assert "mean_projected_lst_celsius" in data
