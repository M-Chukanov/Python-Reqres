import requests

response = requests.get("https://petstore.swagger.io/v2/pet/168")
print(response.text) 


