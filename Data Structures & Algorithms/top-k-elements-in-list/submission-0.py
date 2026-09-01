class Solution:
    def freqNum(self, nums:List[int])->Dict:
        dictt= {}
        for i in nums:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        return dictt

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = sorted(self.freqNum(nums).items(),key=lambda item: item[1],reverse=True)
        result = dict(freqList)
        resultFinal = list(result.keys())
        return resultFinal[0:k]


        
        