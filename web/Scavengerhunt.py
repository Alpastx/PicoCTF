import requests
from bs4 import BeautifulSoup as bs 

url = ""
robots_url = url + "robots.txt"
htaccess_url = url + ".htaccess"
css_url = url + "mycss.css"
dsstor_url = url + ".DS_Store"

response = requests.get(url)
print(response.text)
response = requests.get(css_url)
print(response.text)
response = requests.get(robots_url)
print(response.text)
response = requests.get(htaccess_url)
print(response.text)
response = requests.get(dsstor_url)
print(response.text)