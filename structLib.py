#!/usr/bin/python3
import struct

f = 3.14
s = struct.pack('>f', f)
print(s)

s = struct.pack('>Ih', 1000, -20)
print(s)
'''
Format Code  Data Type	    Size (bytes)
b	         Signed char	    1
B	         Unsigned char	    1
h	         Signed short	    2
H	         Unsigned short	    2
i	         Signed int	        4
I	         Unsigned int	    4
f	         Float	            4
d	         Double	            8
'''