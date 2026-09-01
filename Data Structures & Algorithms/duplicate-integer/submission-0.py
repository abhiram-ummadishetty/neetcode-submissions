class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = set()
        for i in nums:
            if i in dictt:
                return True
            dictt.add(i)
        return False

        