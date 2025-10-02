import requests 
response=requests.get("url")
print(response.status_code)
print(response.text)
print(response.json())
# Posting data
data={
    "title":"my post",
    "body":"hello world",
    "user_id": 1
}
response=requests.post("https://dog.ceo/api/breads/image/random",json=data)
