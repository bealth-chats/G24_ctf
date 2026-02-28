import requests

url = "https://deploylite.g24sec.space/api/builds/trigger"
cookies = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjczODBmMTJmLWI3NTctNDU1NS04Y2ZkLWZjOTZjZDFiOTU5YSIsImVtYWlsIjoidGVzdHVzZXIxQGV4YW1wbGUuY29tIiwidXNlcm5hbWUiOiJ0ZXN0dXNlcjEiLCJyb2xlIjoidXNlciIsImlhdCI6MTc3MjIzNjg5NSwiZXhwIjoxNzcyMzIzMjk1LCJpc3MiOiJkZXBsb3lsaXRlIn0.W5PaL433SEhIa5RkX_FvTkqxYdFKajp3xNhWWbQ56vM"
}
headers = {"Content-Type": "application/json"}
data = {
    "project_id": "8382143c-bed4-473d-ad52-145bbedc6fb8",
    "repo_url": "https://github.com/my/project",
    "build_script": "id",
    "branch": "main"
}

response = requests.post(url, cookies=cookies, headers=headers, json=data)
print(response.status_code)
print(response.text)
