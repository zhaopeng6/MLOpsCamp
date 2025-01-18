import requests
import json

url = "http://localhost:8000/predict"

data = {
    "sepal_length":"0.1",
    "sepal_width":"0.2",
    "petal_length":"0.3",
    "petal_width":"0.4"
}
input_data = json.dumps(data)
headers = {"Content-Type": "application/json"}

resp = requests.post(url, input_data, headers=headers)
print(resp.text)
