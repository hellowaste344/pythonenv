from cryptography.fernet import Fernet 
import base64 

data = b"http://example.com/webhook"

url = base64.urlsafe_b64encode(data)
print("Base64 encoded url: ", url)

key = Fernet.generate_key()
print("Key: ", key)
f = Fernet(key)

token = f.encrypt(url)

print("Encrypted: ", token)

recovered = f.decrypt(token.decode())

print("Decrypted: ", recovered)

decoded = base64.urlsafe_b64decode(url).decode()

print("Webhook url: ", decoded)

print(base64.b64encode(b"hello world"))