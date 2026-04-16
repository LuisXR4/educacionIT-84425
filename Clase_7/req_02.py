import requests

params = {"q": "python", "sort":"relevance"}
response = requests.get("https://www.example.com/search", params=params)

print(response.status_code)
print(response.url)