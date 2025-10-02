import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

if response.status_code == 200:
    print(response.json())