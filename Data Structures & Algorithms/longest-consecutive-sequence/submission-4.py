class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        answer = 0

        for i in nums:
            if i-1 not in sett:
                temp = i
                count =1

                while temp+1 in sett:
                    temp+=1
                    count+=1

                answer = max(answer, count)

        return answer