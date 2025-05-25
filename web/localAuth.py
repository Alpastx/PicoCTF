import requests
from bs4 import BeautifulSoup  as bs

url = ''
loginurl = url+'login.php'
adminUrl = url+'admin.php'

data ={
    'hash': '2196812e91c29df34f5e217cfd639881'
}
response = requests.get(loginurl)
print(response.text)

response = requests.post(adminUrl,data)
response = bs(response.text, 'html.parser')
flag = response.find('body').text
print(response.text)