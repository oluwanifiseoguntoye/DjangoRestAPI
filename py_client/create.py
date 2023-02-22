import requests

headers = {"Authorization":
'Bearer fe129a07cccc17c9b1eda95cc4d92b1a0c56f5f3'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "New Product",
    "content": "Empty field",
    "price": 0.00
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())