class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cout = [0]*26

        for i in range(len(s)):
            cout[ord(s[i])-ord('a')]+=1
            cout[ord(t[i])-ord('a')]-=1
        
        for val in cout:
            if val!=0:
                return False
        return True
        