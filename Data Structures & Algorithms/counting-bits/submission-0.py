class Solution:

    def BrianKerninghansAlgo(self,i: int):
        count = 0
        while i!=0:
            i = i & (i-1)
            count+=1
        return count

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0,n+1):
            noOfBits = self.BrianKerninghansAlgo(i)
            result.append(noOfBits)
        return result

        