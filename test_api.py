import requests
import json

with open("test_inputs.json") as f:
    data_list = json.load(f)

for data in data_list:
    response = requests.post("http://127.0.0.1:8000/predict_all", json=data)
    print(response.text)
    print("---------------------")