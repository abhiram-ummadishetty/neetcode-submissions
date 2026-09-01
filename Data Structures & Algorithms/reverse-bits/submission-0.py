class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            lastBit = n>>i & 1
            result = result<<1 | lastBit

        return result
        
        