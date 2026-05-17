import requests

BASE_URL = "http://127.0.0.1:8000"


def test_root():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    assert response.json()["message"] == "Hello QA"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert body["name"] == "Maria"
