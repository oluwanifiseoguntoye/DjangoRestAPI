import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "Cookies", "content": "Chocolate chips", "price": 3.99})
print(get_response.json())





