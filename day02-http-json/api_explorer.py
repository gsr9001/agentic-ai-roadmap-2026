'''import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print("Final URL:", response.url)
print("Status Code:", response.status_code)

data = response.json()

for post in data:
    print("-------------------------")
    print("Post ID:", post["id"])
    print("Title:", post["title"])'''
#######################################################
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id):
    url = f"{BASE_URL}/users/{user_id}"

    response = requests.get(url)

    print("\n--- GET USER ---")
    print("URL:", response.url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        print("Name:", data["name"])
        print("Email:", data["email"])
        print("City:", data["address"]["city"])

    else:
        print("Request failed")


def get_posts(user_id):
    url = f"{BASE_URL}/posts"

    params = {
        "userId": user_id
    }

    response = requests.get(url, params=params)

    print("\n--- GET POSTS ---")
    print("URL:", response.url)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts[:3]:
            print("\nPost ID:", post["id"])
            print("Title:", post["title"])


def create_post():
    url = f"{BASE_URL}/posts"

    payload = {
        "title": "Agentic AI",
        "body": "Learning APIs for Agentic AI",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    print("\n--- CREATE POST ---")
    print("Status Code:", response.status_code)
    print("Response:", response.json())


get_user(5)

get_posts(1)

create_post()