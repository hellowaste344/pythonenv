from Crypto.Util.number import inverse, long_to_bytes
from sympy import factorint

n = 8749002899132047699790752490331099938058737706735201354674975134719667510377522805717156720453193651
e = 65537
ct = 5834177939681309704189596065676685903729910303824560560929082759974421613450454803823195850471530486

factors = factorint(n )

print(factors)
phi = 1
'''
for p in factors:
    phi *= (p - 1)

d = inverse(e, phi)

m = pow(ct, d, n)

print(long_to_bytes(m))
chr()
'''