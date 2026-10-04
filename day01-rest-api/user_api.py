import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Name:", data["name"])
print("Email:", data["email"])
print("City:", data["address"]["city"])
print("Company:", data["company"]["name"])