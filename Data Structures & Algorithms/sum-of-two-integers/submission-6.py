class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF 
        while(b & mask):

            carry=(
                (a&b)<<1)& mask
            a=(a^b)& mask
            b=carry
        if a > 0x7FFFFFFF:  # if result exceeds max positive 32-bit
            a = ~(a ^ mask)
        return a 