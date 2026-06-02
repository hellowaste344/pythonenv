key = b'CSUCKS'

hex_values = [
    "41", "30", "20", "63", "4a", "45", "54", "76",
    "01", "1c", "7e", "59", "63", "e1", "61", "25",
    "7f", "5a", "60", "50", "11", "38", "1f", "3a",
    "60", "e9", "62", "20", "0c", "e6", "50", "d3",
    "35"
]

# convert hex strings to bytes
encrypted = bytes(int(x,16) for x in hex_values)

decrypted = bytes(b ^ key[i % len(key)] for i, b in enumerate(encrypted))

print(decrypted)
#print(decrypted.decode(errors="ignore"))