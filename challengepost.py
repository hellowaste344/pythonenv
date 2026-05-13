import hmac, hashlib, struct, time, base64,json

email = 'xashe107@gmail.com'
secret = (email + 'HENNGECHALLENGE004').encode('ascii')
T = int(time.time()) // 30
counter = struct.pack('>Q', T)

h = hmac.new(secret, counter, hashlib.sha512).digest()

offset = h[-1] & 0x0f
code = struct.unpack('>I', h[offset:offset+4])[0] & 0x7FFFFFFF
otp = str(code % 10**10).zfill(10)
token = base64.b64encode(f'{email}:{otp}'.encode()).decode()

print(f'T={T}, OTP={otp}')

import requests
s = requests.Session()

body = json.dumps({
    'github_url': 'https://gist.github.com/hellowaste344/e89bda6833672859ca0c5db9e6adea47',
    'contact_email': email,
    'solution_language': 'python'
}).encode()

req = s.post(
    'https://api.challenge.hennge.com/challenges/backend-recursion/004',
    data=body,
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Basic {token}'
    },
)

resp = req.json()
print(json.dumps(resp))