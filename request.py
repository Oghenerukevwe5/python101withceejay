import request 
response=request.get("url")
print(response.status_code)
print(response.text)
print(response.json())

response=request.get("https://dog.ceo/api/breads/image/random")