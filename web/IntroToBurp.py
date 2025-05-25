import requests
from bs4 import BeautifulSoup as bs

base_url = ''
session = requests.Session()
response = session.get(base_url)
soup = bs(response.text, 'html.parser')
csrfToken = soup.find('input')['value']
regData ={
    'csrf_token' : csrfToken,
    'full_name': 'asd',
    'username': 'asda',
    'phone_number': 'asd',
    'city': 'asda',
    'password': 'asd',
    'submit': 'Register'
}
response = session.post(base_url, data=regData)
session.get(base_url+"dashboard")
response = session.post(base_url+"dashboard", data=regData)
print(response.text)
