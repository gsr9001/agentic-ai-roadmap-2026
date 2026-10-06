import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    joke = response.json()

    print("\nJoke:")
    print(joke["setup"])
    print(joke["punchline"])
else:
    print("Failed to get joke.")