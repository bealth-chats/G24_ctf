import requests
from bs4 import BeautifulSoup
import re

url = "https://deploylite.g24sec.space/dashboard"
cookies = {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjczODBmMTJmLWI3NTctNDU1NS04Y2ZkLWZjOTZjZDFiOTU5YSIsImVtYWlsIjoidGVzdHVzZXIxQGV4YW1wbGUuY29tIiwidXNlcm5hbWUiOiJ0ZXN0dXNlcjEiLCJyb2xlIjoidXNlciIsImlhdCI6MTc3MjIzNjg5NSwiZXhwIjoxNzcyMzIzMjk1LCJpc3MiOiJkZXBsb3lsaXRlIn0.W5PaL433SEhIa5RkX_FvTkqxYdFKajp3xNhWWbQ56vM"
}
response = requests.get(url, cookies=cookies)
print("status:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
for script in soup.find_all('script'):
    src = script.get('src')
    if src:
        print(f"Downloading: {src}")
        js_resp = requests.get(f"https://deploylite.g24sec.space{src}", cookies=cookies)
        print(f"--- {src} ---")
        print(js_resp.text[:500] + "..." if len(js_resp.text) > 500 else js_resp.text)
        print("-" * 40)
