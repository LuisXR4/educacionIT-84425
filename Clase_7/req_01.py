import requests

try:
    response = requests.get("https://www.infobaeyyyyyyyyyyyyyyy.com/")
    print(response.status_code)
except Exception as e:
    print(f"Error {e.__class__}")

