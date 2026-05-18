import base64

with open("/home/Xashe/pentest/logs.txt", "r") as f:
    text = f.read().encode('utf-8')
    
rawByte = base64.b64decode(text)
with open("cipher.jpg", "wb") as f:
    f.write(rawByte)