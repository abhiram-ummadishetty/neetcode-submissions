class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        FreqS ={}
        FreqT ={}

        for i in s:
            if i in FreqS:
                FreqS[i]+=1
            else:
                FreqS[i] = 1
        
        for i in t:
            if i in FreqT:
                FreqT[i]+=1
            else:
                FreqT[i] = 1

        if FreqS == FreqT:
            return True
        else:
            return False
            
        