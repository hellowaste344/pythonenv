import hmac, hashlib

output = hmac.new(b'password', b'msg', hashlib.sha512).digest()

print(output)