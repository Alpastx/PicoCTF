import requests as r 
from bs4 import BeautifulSoup as bs
url = ""

response = r.get(url)
soup = bs(response.text, 'html.parser')
flag = soup.find_all('p')[1].get("class")
print(flag[0])

