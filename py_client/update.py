import requests

product_id = input("What Product ID would you like to update? \n")

try:
    product_id = int(product_id)
except:
    print(f'Not a valid Product ID: {product_id}')

data = {
    "title": "Juice",
    "price": 3.99
}
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/update/"

    get_response = requests.put(endpoint, json=data)
    print(get_response.json())
