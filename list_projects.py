import requests

url = "https://deploylite.g24sec.space/api/projects"
cookies = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjczODBmMTJmLWI3NTctNDU1NS04Y2ZkLWZjOTZjZDFiOTU5YSIsImVtYWlsIjoidGVzdHVzZXIxQGV4YW1wbGUuY29tIiwidXNlcm5hbWUiOiJ0ZXN0dXNlcjEiLCJyb2xlIjoidXNlciIsImlhdCI6MTc3MjIzNjg5NSwiZXhwIjoxNzcyMzIzMjk1LCJpc3MiOiJkZXBsb3lsaXRlIn0.W5PaL433SEhIa5RkX_FvTkqxYdFKajp3xNhWWbQ56vM"
}

response = requests.get(url, cookies=cookies)
print(response.status_code)
print(response.text)
