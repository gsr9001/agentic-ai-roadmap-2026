import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print("Status Code:", response.status_code)

print("Response Headers:")
print(response.headers)

print("\nJSON Response:")
print(response.json())