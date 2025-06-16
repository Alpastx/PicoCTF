from pwn import * 
import argparse
from Crypto.Util.number import inverse, long_to_bytes
from sympy import factorint

parser = argparse.ArgumentParser(description='Even RSA can be broken exploit script')
parser.add_argument('-t', '--target', type=str, required=True, help='Target IP address')
parser.add_argument('-p', '--port', type=int, default=1337, help='Target port')
args = parser.parse_args()
conn = remote(args.target, args.port)



while True:
    line = conn.recvline().decode().strip()
    if line.startswith("N:"):
        N = int(line.split(":")[1].strip())
        print(f'[+] Received N: {N}')
    elif line.startswith("e:"):
        e = int(line.split(":")[1].strip())
        print(f'[+] Received e: {e}')
    elif line.lower().startswith("cyphertext:"):  
        c = int(line.split(":")[1].strip())
        print(f'[+] Received ciphertext: {c}')
        break  

print("[+] Attempting to factor N...")

factors = factorint(N)
print("[*] Factors of N:", factors)

if len(factors) != 2:
    print("[-] N does not factor into two primes. Aborting.")
    exit()
p, q = list(factors.keys())
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, N)
plaintext = long_to_bytes(m)
print("[+] Decrypted message:", plaintext.decode())

