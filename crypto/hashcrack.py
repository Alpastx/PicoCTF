from pwn import * 
import argparse

parser = argparse.ArgumentParser(description='Hash Cracker python exploit script')
parser.add_argument('-t', '--target', type=str, required=True, help='Target IP address')
parser.add_argument('-p', '--port', type=int, default=1337, help='Target port')
args = parser.parse_args()
hash_pass = {
    "482c811da5d5b4bc6d497ffa98491e38": "password123",  
    "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3": "letmein",  
    "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745": "qwerty098"  
}

conn = remote(args.target, args.port)

while True:
    line = conn.recvline().decode('utf-8').strip()
    for known_hash in hash_pass:
            if known_hash in line:
                password = hash_pass[known_hash]
                print(f"[+] Found known hash. Sending password: {password}")
                conn.sendline(password.encode())
            if "picoCTF{" in line:
                print(f"[+] Flag found: {line.strip()}")
                conn.close()
                exit(0)
    
   
     