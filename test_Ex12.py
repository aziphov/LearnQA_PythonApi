import requests

class TestExample:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        valueslist = list(response.headers.values())
        print(valueslist[6])
        assert valueslist[6] == "Some secret value", "header не найден"