import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format) # парсим json
print(obj['answer'])

key = "answer1"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет") # конкатенация
