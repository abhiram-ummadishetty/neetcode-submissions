class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt ={}

        for i, k in enumerate(nums):
            y = target -k
            if y in dictt:
                return [dictt[y],i]
            dictt[k] = i
        