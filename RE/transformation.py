print("[+] get the enc file fromt picoCTF site and keep it in pwd")
with open("enc", "r") as file:
    encoded_string = file.read()
print("[+] Encoded String is : ", encoded_string)

raw = encoded_string.encode('utf-16-be')
flag = raw.decode('latin-1')
print("[+] Final flag is : ", flag.strip())
