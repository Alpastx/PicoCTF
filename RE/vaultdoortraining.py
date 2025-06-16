print("[+] get the source code from picoCTF site and keep it in pwd")
with open("VaultDoorTraining.java", "r") as file:
    source = file.read()

flag = source.split("return password.equals(")[1].split(");")[0].strip('"')
print(f"[+] Final flag is : picoCTF{{{flag}}}")