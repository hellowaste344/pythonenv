import json
import base64
from jwcrypto import jwk, jwt 
import time

key = jwk.JWK.generate(
    kty='EC',
    curve='P-256',
    kid='test',
    use='sig',
    alg='ES256',
)
privateKey = jwk.JWK.from_json(key.export_private())
publicKey = jwk.JWK.from_json(key.export_public())

t0 = int(time.time())

header = json.dumps({
    'alg':'ES256',
    'kid': 'test',
})

payload = json.dumps({
    'iss': '12345',
    'sub': 'test',
    'aud':'http://example.com',
    'iat': t0,
    'exp': t0 + 1200,
})

# handles base64 encoding internally
jwtToken = jwt.JWT(
    header = header,
    claims = payload,
)

jwtToken.make_signed_token(privateKey)
token = jwtToken.serialize()

print(f"Signature: {token}")

verified = jwt.JWT(
    jwt = token,
    key = publicKey,
)

print(verified.claims)
