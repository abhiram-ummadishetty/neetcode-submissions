class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = set(nums)
        if len(dictt) ==len(nums):
            return False
        return True
            
        