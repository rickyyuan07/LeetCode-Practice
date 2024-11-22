class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        while b != 0:
            # XOR
            sum_ = (a ^ b) & MASK
            carry = ((a & b) << 1)
            a, b = sum_, carry
        
        return a if a <= INT_MAX else ~(a ^ MASK)