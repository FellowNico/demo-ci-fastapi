from demo_ci_fastapi.web_api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_healthcheck():
    """Test healthcheck endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {}
