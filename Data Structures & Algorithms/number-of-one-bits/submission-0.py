class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(0,32):
            temp = n>>i
            result = temp & 1
            if result == 1:
                count+=1
            
        return count
        
        
        