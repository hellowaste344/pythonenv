""" 
AND(&) sets a result bit to 1 only if both corresponding bits are 1
OR(|) sets a result bit to 1 if at least one corresponding is 1
XOR(^) sets a result bit to 1 if the corresponding bits differ
NOT(~) inverts all bits (0 becomes 1, 1 becomes 0), using two's complement ~x = -(x+1)
Left Shift(<<) moves all bits left by the specified numbers of positions, filling right with zeros
Right Shift(>>) moves all bits right by the specified positions, filling left with sign bits
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result, power = 1, n
        if power < 0:
            x, power = 1.0/x, -power
        while power:
            if power & 1:
                result *= x
            x, power = x*x, power >> 1
        return result
    
s = Solution()
x = 2
n = 13
print(s.myPow(x, n))
