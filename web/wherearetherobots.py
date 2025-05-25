import requests
from bs4 import BeautifulSoup as bs

url = ""
robots_url = url+"1bb4c.html"
response = requests.get(robots_url)
soup = bs(response.text, 'html.parser')
flag = soup.find('flag').text