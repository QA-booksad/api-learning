import requests
import allure

BASE_URL = "http://127.0.0.1:8000"


@allure.feature("Root")
@allure.story("Check root endpoint")
def test_root():

    with allure.step("Send GET request to root endpoint"):
        response = requests.get(BASE_URL)

    with allure.step("Check status code"):
        assert response.status_code == 200

    with allure.step("Check response body"):
        assert response.json()["message"] == "Hello QA"


@allure.feature("Users")
@allure.story("Get user by id")
def test_get_user():

    with allure.step("Send GET request to /users/1"):
        response = requests.get(f"{BASE_URL}/users/1")

    body = response.json()

    with allure.step("Check status code"):
        assert response.status_code == 200

    with allure.step("Check user id"):
        assert body["id"] == 1

    with allure.step("Check user name"):
        assert body["name"] == "Vasya"
