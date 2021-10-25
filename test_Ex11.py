import requests

class TestExample:
    def test_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies.values()[0])
        assert response.cookies.values()[0] == "hw_value", "Куки не найдены"