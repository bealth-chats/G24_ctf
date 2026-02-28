import requests

url = "https://deploylite.g24sec.space/api/auth/register"
headers = {"Content-Type": "application/json"}
data = {
    "email": "testadmin@example.com",
    "username": "testadmin",
    "password": "password123",
    "company": "testcompany",
    "role": "admin"
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
print(response.cookies)
