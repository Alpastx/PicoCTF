import requests
from bs4 import BeautifulSoup as bs
url = ""

response = requests.get(url)   
print(response.text) 
