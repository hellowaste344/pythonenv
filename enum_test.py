from enum import Enum


class Season(int, Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.AUTUMN.value)
print(Season(2).name)
print(Season(4))

for s in Season:
    print(s.value, " : ", s.name)
