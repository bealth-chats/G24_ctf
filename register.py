import requests
import json

url = "https://deploylite.g24sec.space/api/auth/register"
headers = {"Content-Type": "application/json"}
data = {
    "email": "testuser1@example.com",
    "username": "testuser1",
    "password": "password123",
    "company": "testcompany"
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)

print(response.cookies)
