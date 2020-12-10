from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


def test_languages_api():
    response = client.get("/languages/")
    assert response.status_code == 200
    _check_response_type(response.json())


def _check_response_type(json_response):
    for el in json_response:
        print(el)
        assert "name" in el
        assert "number_of_repos" in el
        assert "repos" in el
