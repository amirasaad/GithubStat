from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

def test_languages_api():
    response = client.get("/languages/")
    assert response.status_code == 200
    assert response.json() == [{
        "name": "Python",
        "number_of_repos": 2,
        "repos": [
            "https://github.com/amirasaad/pastebin",
            "https://github.com/amirasaad/GDL"
        ],
    }]
