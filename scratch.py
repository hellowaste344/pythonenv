import os
import random
import sys

print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))
print(sys.executable)
print(sys.modules)
print(sys.platform)
print("#" * 50)

seed = random.randint(0, 3)

opts = ("a", "b", "c", "d")
print(type(opts))
print(opts[seed])
