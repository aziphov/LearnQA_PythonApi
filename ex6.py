import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
second_response = response.history[1]
third_response = response.history[2]
fourth_response = response.history[3]
print(first_response.url)
print(second_response.url)
print(third_response.url)
print(fourth_response.url)
