import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "New Product",
    "content": "Empty field",
    "price": 0.00
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())