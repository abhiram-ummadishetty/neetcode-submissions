class Solution:
    def cleanString(self,s:str)-> str:
        result = ""
        s = s.lower()
        for i in s:
            x = ord(i)
            if (ord('a') <= x <= ord('z') or
            ord('0') <= x <= ord('9')):
                result += i
        return result

    def isPalindrome(self, s: str) -> bool:
        s = self.cleanString(s)
        first = 0
        last = len(s)-1

        while(first<last):
            if s[first]==s[last]:
                first+=1
                last-=1
            else:
                return False

        return True
        