import requests 

url = ""
cssUrl = url+"mycss.css"
jsUrl = url+"myjs.js"
response = requests.get(url)
response2 = requests.get(cssUrl)
response3 = requests.get(jsUrl)
print(response.text)
print(response2.text)
print(response3.text)