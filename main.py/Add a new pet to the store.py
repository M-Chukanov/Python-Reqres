import requests

response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 168,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Adolf",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)                      

