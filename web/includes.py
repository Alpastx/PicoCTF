import requests
from bs4 import BeautifulSoup as bs

url = ""
scripturl = url+"script.js"
cssUrl = url+"style.css"
scriptResponse = requests.get(scripturl)
cssUrl = requests.get(cssUrl)
print(cssUrl.text)
print(scriptResponse.text)
