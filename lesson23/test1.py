import requests

resp = requests.get("https://example.com/")
for item in resp.headers.items():
    print(f"{item[0]}:{item[1]}")
