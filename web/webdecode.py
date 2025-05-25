import requests
from bs4 import BeautifulSoup as bs
import base64

url = ""
aboutpage = url+"about.html"
response = requests.get(url=aboutpage)    
soup = bs(response.text, 'html.parser')
flagsection = soup.find("section", class_="about")
encodedflag = flagsection.get("notify_true")
flag = base64.b64decode(encodedflag).decode('utf-8')
print(flag)
