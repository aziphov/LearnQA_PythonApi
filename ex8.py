import requests
import time
import json

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") # 1) создаем задачу
obj = json.loads(response.text)
token = obj["token"]
seconds = obj["seconds"]
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}) # 2) создаем вторую задачу до истечения времени
obj2 = json.loads(response.text)
obj2["status"] == "Job is NOT ready" # 2) убеждаемся, что статус верный
time.sleep(seconds) # 3) ждем нужное количество секунд
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}) # 4) делаем запрос c token ПОСЛЕ того, как задача готова
obj3 = json.loads(response.text)
obj3["status"] == "Job is ready" # 4) убеждаемся в правильности поля status и наличии поля result
obj3["result"] is not None
print(response.text)
