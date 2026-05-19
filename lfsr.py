'''
state = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
taps = [63,61,60,58]
cipher = "8f0e6d0f5b0dc1db201948b9e0cebd8ff0c815fd492761028be3b558fa81b72538338e7e04fbddef0c6260a4eb758417"

res = ''.join([chr(int(cipher[i:i+2], 16)) for i in range(0, len(cipher),2)])


print(res)
'''
from binascii import unhexlify

state = [
    0, 0, 1, 0, 0, 1, 0, 1,
    1, 1, 1, 0, 1, 1, 0, 0,
    1, 0, 0, 1, 0, 1, 1, 0,
    1, 0, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 0, 1, 1, 0, 1,
    1, 0, 0, 0, 1, 0, 1, 1,
    1, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 0, 1, 1
]

taps = [63, 61, 60, 58]

cipher = "8f0e6d0f5b0dc1db201948b9e0cebd8ff0c815fd492761028be3b558fa81b72538338e7e04fbddef0c6260a4eb758417"


# =========================================================
# Fibonacci LFSR
# =========================================================
def step(state):
    # XOR feedback
    new_bit = 0
    for t in taps:
        new_bit ^= state[t]

    # output bit (LSB)
    out = state[-1]

    # shift right
    state = [new_bit] + state[:-1]

    return out, state


# =========================================================
# Convert ciphertext hex -> bit array
# =========================================================
cipher_bytes = unhexlify(cipher)

cipher_bits = []

for b in cipher_bytes:
    bits = format(b, '08b')
    cipher_bits.extend([int(x) for x in bits])


# =========================================================
# Generate keystream
# =========================================================
keystream = []

for _ in range(len(cipher_bits)):
    bit, state = step(state)
    keystream.append(bit)


# =========================================================
# XOR decrypt
# =========================================================
plain_bits = [
    c ^ k for c, k in zip(cipher_bits, keystream)
]


# =========================================================
# Convert bits -> bytes
# =========================================================
plaintext = bytearray()

for i in range(0, len(plain_bits), 8):
    chunk = plain_bits[i:i+8]

    if len(chunk) < 8:
        break

    byte = int(''.join(map(str, chunk)), 2)
    plaintext.append(byte)


# =========================================================
# Output
# =========================================================
print(plaintext)
print()
print(plaintext.decode(errors="ignore"))