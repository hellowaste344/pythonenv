#!/usr/bin/python3

import hashlib
import hmac # keyed-hashing for message authentication

digest_maker = hmac.new(b'password123', b'msg', hashlib.sha256)

clonedDigest = digest_maker.copy()
duplicateDigest = digest_maker.copy()

clonedDigest.update(b'second msg')
clonedDigest.update(b'third message')

duplicateDigest.update(b'second msg')
duplicateDigest.update(b'third message')

print("Hexadigest: " + digest_maker.hexdigest())
print("Updated Hexadigest: " + clonedDigest.hexdigest())
print("Duplicate Hexadigest: " + duplicateDigest.hexdigest())

print("Digest size: " + str(clonedDigest.digest_size) + " bytes")
print("Block size: " + str(clonedDigest.block_size) + " bytes")
print("Digest name: " + str(clonedDigest.name))
