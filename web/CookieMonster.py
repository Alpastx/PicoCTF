import requests
from bs4 import BeautifulSoup as bs
import base64
import urllib.parse

url = ""
protected_url = url+"login.php"
data = {
    "username": "bla",
    "password": "blabla"
}
session = requests.Session()
response = session.post(protected_url,data)
encoded_flag = session.cookies.get('secret_recipe')
encoded_flag = urllib.parse.unquote(encoded_flag)
flag = base64.b64decode(encoded_flag).decode('utf-8')
print(flag)

