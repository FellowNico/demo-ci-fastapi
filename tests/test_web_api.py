from pathlib import Path
from demo_ci_fastapi.web_api import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_healthcheck():
    """Test healthcheck endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {}


def test_upload_file():
    """Test to upload a file."""
    filepath = Path(__file__).parent / "data" / "image.jpg"
    response = client.post(url="/uploadfile", files={"data_file": filepath.open("rb")})
    assert response.status_code == 200
    assert response.json() == {"filename": "image.jpg"}
