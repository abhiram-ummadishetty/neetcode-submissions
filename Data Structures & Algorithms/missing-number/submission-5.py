class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range (0,len(nums)):
            result = result^i
            result = result^nums[i]
        return result

# result = [last expected number]

# then for every index:
#     XOR expected number
#     XOR actual number

# matching numbers cancel
# missing number remains

# So yes — your observation is correct. result = len(nums) is specifically there to account for the number that isn't visited by range(len(nums)).
        