import requests

product_id = input("What Product ID would you like to retrieve? \n")

try:
    product_id = int(product_id)
except:
    print(f'Not a valid Product ID: {product_id}')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/"

get_response = requests.get(endpoint)
print(get_response.json())
