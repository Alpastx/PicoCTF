import base64 
from caesarcipher import CaesarCipher as cc 

#encoded_string = YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==

print("[+] download the file form picoCTF site and keep it in pwd")
with open("enc_flag", "r") as file:
    encoded_string = file.read()
print("[+] Encoded flag = ", encoded_string)
print("[+] Decoding the base64 encoded string")
decoded_bytes = base64.b64decode(encoded_string)
decoded = decoded_bytes.decode('utf-8')
print("[+] layer 1 Decoded = ", decoded)
secondlayer = decoded.split("b'")[1]
secondlayer = secondlayer.split("'")[0]
secondlayer = base64.b64decode(secondlayer)
secondlayer = secondlayer.decode('utf-8')
print("[+] layer 2 Decoded = ", secondlayer)
print("[+]decoding caesar cipher")
flag = cc(secondlayer)
flag = flag.cracked
print("[+] Final flag = ", flag)
