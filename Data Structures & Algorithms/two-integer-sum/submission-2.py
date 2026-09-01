class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i,j in enumerate(nums):
            dictt[j]=i

        for i,j in enumerate(nums):
            if target - j in dictt and dictt[target-j] != i:
                return [i,dictt[target-j]]

        return [-1,-1]

        