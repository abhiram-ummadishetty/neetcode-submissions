class Solution:
    def freqStr(self, s:str)->dict:
        dictt = {}
        for i in s:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        return dictt


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(0,len(strs)):
            dictt_i = self.freqStr(strs[i])
            key = tuple(sorted(dictt_i.items()))
            if key not in result:
                result[key] = []
            result[key].append(strs[i])
        return list(result.values())