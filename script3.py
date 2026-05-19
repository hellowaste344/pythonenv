from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import random

cipher = "20773a1ecc72c4561eb26c037865bfe99bab18166f5e67885766551e1fb55dbee70f8f18931c28c55f58bf62da487b7f67d880acb03c3324e4a3eea51faa0d59fd7c84a06c770cae02e2a30d1056492a"
rawByte = ''.join(chr(int(cipher[i:i+2], 16)) for i in range(0, len(cipher), 2))

iv = b"\x00"*16

with open("/usr/share/wordlists/rockyou.txt", "rb") as f:
    for line in f:
        word = line.strip().decode(errors="ignore")

        attempt = f"picoCTF{{{word}}}".encode()
        key = hashlib.sha256(attempt.strip()).digest()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        enc = cipher.encrypt(pad(attempt, 16))
        if enc == rawByte:
            print(f"Found: {attempt.decode()}")
            break
        print(f"Attempt {attempt.decode()} failed")