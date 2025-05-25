import requests

url = ""

response = requests.head(url)
flag = response.headers.get("flag")
print(flag)