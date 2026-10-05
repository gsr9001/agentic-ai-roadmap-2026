import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Learning Agentic AI",
    "body": "Day 2 - Learning HTTP and JSON",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)

print("Response:")
print(response.json())